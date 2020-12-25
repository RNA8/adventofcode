import numpy as np
from itertools import product
from typing import NamedTuple, List, Dict
from time import time

timer = time()
with open('inputs/day24.txt','r') as fid:
    data = fid.read().splitlines()
print("%d lines" % (len(data)))

offsets = {'e':np.array([+1,-1,0]),
           'w':np.array([-1,+1,0]),
           'nw':np.array([0,+1,-1]),
           'se':np.array([0,-1,+1]),
           'ne':np.array([+1,0,-1]),
           'sw':np.array([-1,0,+1])}
offset_matrix = np.array(list(offsets.values()))

def process_line(line):
    pt = np.array([0,0,0])
    i = 0
    while i < len(line):
        if line[i] in ['n','s']:
            action = line[i:i+2]
            i += 2
        else:
            action = line[i]
            i += 1
        pt = pt + offsets[action]
    return pt


tiles = {}
for datum in data:
    pt = process_line(datum)
    tile_color = tiles.get(tuple(pt),'white')
    if tile_color == 'white':
        tiles[tuple(pt)] = 'black'
    elif tile_color == 'black':
        tiles[tuple(pt)] = 'white'
print("Answer to Part 1 = " + str(sum(1 for val in tiles.values() if val=='black')))



def get_num_black_neighbors(tiles, min_coords, max_coords):
    possible_coords = np.array([(x,y,z) 
                                for (x,y,z) in product(range(min_coords[0],max_coords[0]+1),
                                                       range(min_coords[1],max_coords[1]+1),
                                                       range(min_coords[2],max_coords[2]+1))
                                if x+y+z==0])
    print("Possible_coords: " + str(len(possible_coords)), end=' ')
    num_black_nbrs = {}
    for coord in possible_coords:
        num_black_nbrs[tuple(coord)] = sum(tiles.get(tuple(pt),'white')=='black' for pt in coord+offset_matrix)
    return num_black_nbrs

num_days = 100
for day_num in range(num_days):
    coordinates = np.array(list(tiles.keys()))
    min_coords = coordinates.min(axis=0) - 1
    max_coords = coordinates.max(axis=0) + 1
    num_blk_nbrs = get_num_black_neighbors(tiles, min_coords, max_coords)
    for coord in num_blk_nbrs.keys():
        if tiles.get(coord,'white') == 'black' and (num_blk_nbrs[coord]==0 or num_blk_nbrs[coord]>2):
            tiles[coord] = 'white'
        elif tiles.get(coord,'white') == 'white' and num_blk_nbrs[coord]==2:
            tiles[coord] = 'black'
    print("After day %d = " % (day_num+1) + str(sum(1 for val in tiles.values() if val=='black')),
    end='\r')
print("\nAnswer to Part 2 = " + str(sum(1 for val in tiles.values() if val=='black')))
print("Elapsed time is %.2f seconds" % (time() - timer))
