import numpy as np
from itertools import permutations
from time import time
with open('inputs/day24.txt','r') as fid:
    data = sorted(list(map(int,fid.read().splitlines())))


def get_all_subsets_with_target_sum(input_data, target_sum):
    N = len(input_data)
    DP = np.zeros((N, target_sum+1)).astype('bool')
    for i in range(N):
        DP[i,0] = True
    if input_data[0] <= target_sum:
        DP[0,input_data[0]] = True
    for i in range(1, N):
        for j in range(target_sum+1):
            if input_data[i] <= j:
                DP[i,j] = DP[i-1,j] or DP[i-1,j-input_data[i]]
            else:
                DP[i,j] = DP[i-1,j]
    if DP[N-1,target_sum] is False:
        print(f"Cannot reach sum {target_sum} with subset of array")

    all_combos = []
    def printSubsetsRec(arr, i, isum, p):

        if i==0 and isum != 0 and DP[0,isum]:
            p.append(arr[i])
            # print("P: = " + str(len(p)))
            # assert sum(p)==target_sum
            # print(p)
            all_combos.append(p)
            return

        if i==0 and isum==0:
            # print("P: = " + str(len(p)))
            # assert sum(p)==target_sum
            # print(p)
            all_combos.append(p)
            return

        if DP[i-1,isum]:
            b = p.copy()
            printSubsetsRec(input_data, i-1, isum, b)

        if isum>=input_data[i] and DP[i-1,isum-input_data[i]]:
            p.append(input_data[i])
            printSubsetsRec(input_data, i-1, isum-input_data[i], p)
        
    my_list = []
    printSubsetsRec(input_data, N-1, target_sum, my_list)
    all_combos = [set(combo) for combo in all_combos]
    return all_combos

# part 1
group_sum = sum(data)//3
assert group_sum*3 == sum(data)
grp1_candidates = get_all_subsets_with_target_sum(data, group_sum)
print(f"Number of candidates for group 1 = {len(grp1_candidates)}")
smallest_g1_size = min(map(len,grp1_candidates))
grp1_candidates = [g1 for g1 in grp1_candidates if len(g1)==smallest_g1_size]
print(f"Number of candidates of least size {smallest_g1_size} for group 1 = {len(grp1_candidates)}")
least_QE = min(map(lambda x:np.prod(list(x)), grp1_candidates))
print(f"Part 1: minimum QE = {least_QE}")


# part 2
group_sum = sum(data)//4
assert group_sum*4 == sum(data)
grp1_candidates = get_all_subsets_with_target_sum(data, group_sum)
print(f"Number of candidates for group 1 = {len(grp1_candidates)}")
smallest_g1_size = min(map(len,grp1_candidates))
grp1_candidates = [g1 for g1 in grp1_candidates if len(g1)==smallest_g1_size]
print(f"Number of candidates of least size {smallest_g1_size} for group 1 = {len(grp1_candidates)}")
least_QE = min(map(lambda x:np.prod(list(x)), grp1_candidates))
print(f"Part 2: minimum QE = {least_QE}")