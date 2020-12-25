from itertools import combinations
with open('inputs/day17.txt','r') as fid:
    data = fid.read().splitlines()
containers = list(map(int,data))

target = 150
num_total_combinations = 0
min_num_containers_combos = 0
for num_containers in range(1,len(containers)+1):
    num_combinations = sum(sum(x)==target for x in combinations(containers,num_containers))
    num_total_combinations += num_combinations
    if min_num_containers_combos == 0 and num_combinations > 0:
        min_num_containers_combos = num_combinations
        print(f"Part 2: min num containers combo = {min_num_containers_combos}")
    print(f"Num containers = {num_containers}", end=', ')
    print(f"num combinations = {num_combinations}")
print(f"Part 1: {num_total_combinations} combinations")
