import numpy as np
from itertools import product
import re

with open('inputs/day3.txt','r') as fid:
    data = fid.read().splitlines()

reg = re.compile(r'\d+')
claims = np.array([list(map(int,reg.findall(line))) for line in data])
# make a dictionary of grid points
# key is point (x,y)
# value is claim IDs
grid = {}
for idx, x, y, w, h in claims:
    for point in product(range(x,x+w),range(y,y+h)):
        if point in grid:
            grid[point].append(idx)
        else:
            grid[point] = [idx]
num_ge_2 = sum(map(lambda x:len(x)>1,grid.values()))
print(f"Part 1: {num_ge_2}")

# find which claim has single claim IDs in all its grid coordinates
for idx, x, y, w, h in claims:
    if all(len(grid[point])==1 for point in product(range(x,x+w),range(y,y+h))):
        print(f"Part 2: Clean claim = {idx}")
        break

