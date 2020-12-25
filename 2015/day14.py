import numpy as np
with open('inputs/day14.txt','r') as fid:
    data = fid.read().splitlines()

# data = ["Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.",
# "Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."]

class Reindeer:
    name = None
    speed = None
    running_time = None
    rest_time = None

    def __init__(self, line):
        parts = line.split()
        self.name = parts[0]
        self.speed = int(parts[3])
        self.running_time = int(parts[6])
        self.rest_time = int(parts[-2])
    def __repr__(self):
        return "Reindeer(%s: %d km/s for %d seconds, rest %d seconds)" % (self.name, self.speed, self.running_time, self.rest_time)

    def distance_traveled(self, time_elapsed):
        full_cycle_time = self.running_time + self.rest_time
        num_full_cycles = time_elapsed // full_cycle_time
        distance = num_full_cycles*self.speed*self.running_time
        distance += min(self.running_time,time_elapsed % full_cycle_time) * self.speed
        return distance


reindeer = [Reindeer(line) for line in data]

target_time = 2503
max_distance = max(deer.distance_traveled(target_time) for deer in reindeer)
print(f"Part 1: maximum distance = {max_distance}")

# make an array with distances traveled for each time stamp
# array is of size num_time_steps x num_reindeer
distances_traveled = np.array([[deer.distance_traveled(time) 
                                for deer in reindeer]
                               for time in range(1,target_time+1)])
# at each time step, find furthest distance
max_distance_at_each_time = np.max(distances_traveled,axis=1,keepdims=True)
# sum up points, 1 point for each reindeer who makes it 
# to the farthest distance at that time step
total_points = np.sum(distances_traveled==max_distance_at_each_time,axis=0)
print(f"Part 2: winning score = {max(total_points)}")
