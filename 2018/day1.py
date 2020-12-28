from time import time
import numpy as np
with open('inputs/day1.txt','r') as fid:
    data = fid.read().splitlines()
data = list(map(int,data))
start_freq = 0
print(f"Part 1: {start_freq + sum(data)}")
# plt.plot(np.cumsum(data+data+data))

timer = time()
# double the repeats of data and check at what point repeated elements occur
# a kind of "inverse binary search"
n = 2
freqs = np.cumsum(data*n)
# while no elements repeat
while len(freqs)==len(np.unique(freqs)):
    n *= 2
    freqs = np.cumsum(data*n)

# start with first half since we know they are all unique
N = (len(data)*n)//2
assert len(freqs[:N])==len(np.unique(freqs[:N]))
# look-up in dict is fastest
visited_freqs = {x:1 for x in freqs[:N]}
# now check in remaining half
for datum in freqs[N:]:
    if datum in visited_freqs:
        print(f"Part 2: {datum}")
        break
    else:
        visited_freqs[datum] = 1
print(f"Elapsed time is {time() - timer} seconds")