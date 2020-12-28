import numpy as np
import operator
from itertools import product
with open('inputs/day6.txt','r') as fid:
    coords = np.array([list(map(int,line.split(', '))) for line in fid.read().splitlines()])
buffer = 2
min_x, min_y = np.min(coords,axis=0)-buffer
max_x, max_y = np.max(coords,axis=0)+buffer

X = np.array(list(product(range(min_x,max_x+1), range(min_y,max_y+1))))


L1_dist = np.abs(X[:,:1] - coords[:,:1].transpose()) + np.abs(X[:,1:] - coords[:,1:].transpose())
# initialize with -1 everywhere
output_map = -np.ones((max_x-min_x+1,max_y-min_y+1), dtype='int')
for idx,(row,coord) in enumerate(zip(L1_dist,X)):
    min_val = row.min()
    indices = np.nonzero(row==min_val)[0]
    if len(indices) == 1: # no tie, unique minimum
        output_map[coord[0]-min_x,coord[1]-min_y] = indices[0]
# output_map will be -1 in tied locations

# find IDs corresponding to the edges, which will be the segments with infinite extent
edges = np.concatenate((output_map[0,:],output_map[-1,:],output_map[:,0],output_map[:,-1]))
edges = np.unique(edges)
# find pixel counts of each value in output_map
# ignore regions with infinite extent, i.e., if this region touches any edge of the map
pix_counts = {i:np.count_nonzero(output_map==i) for i in range(len(coords)) if i not in edges}
largest_region_idx, largest_region_area = max(pix_counts.items(), key=operator.itemgetter(1))
print(f"Part 1: Answer = {largest_region_area}")

max_dist = 10000
region_size = np.count_nonzero(L1_dist.sum(axis=1)<=max_dist)
print(f"Part 2: Answer = {region_size}")
