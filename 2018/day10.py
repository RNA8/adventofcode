from time import time
import numpy as np
import re
import matplotlib.pyplot as plt
%matplotlib inline

with open('inputs/day10.txt','r') as fid:
    data = fid.read().splitlines()
reg = re.compile(r'-?\d+')
X = np.double([list(map(int,reg.findall(datum))) for datum in data])
positions = X[:,:2]
velocities = X[:,2:]

timer = time()
x = positions
area = []
area.append(np.prod(np.max(x,axis=0)-np.min(x,axis=0)))
for i in range(100000):
    x += velocities
    area.append(np.prod(np.max(x,axis=0)-np.min(x,axis=0)))
    if area[-1] > area[-2]:
        x -= velocities
        break

# Part 1
plt.figure(figsize=(10,2))
plt.scatter(x[:,0],-x[:,1])
# ZZCBGGCJ

# Part 2:
print(f"Part 2: Answer = {i}")