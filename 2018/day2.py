from time import time
import numpy as np
from itertools import combinations
from string import ascii_lowercase
with open('inputs/day2.txt','r') as fid:
    data = fid.read().splitlines()
data = [np.array(list(x)) for x in data]
histograms = [{i:np.count_nonzero(x==i) for i in ascii_lowercase} for x in data]
n2 = 0
n3 = 0
for h in histograms:
    if any(val==2 for val in h.values()):
        n2 += 1
    if any(val==3 for val in h.values()):
        n3 += 1
print(f"Part 1: Answer = {n2*n3}")

for i,j in combinations(data,2):
    if np.count_nonzero(i!=j)==1:
        i_idx = np.nonzero(i!=j)[0][0]
        final_string = ''.join(list(i[:i_idx]) + list(i[i_idx+1:]))
        print(f"Part 2: {final_string}")