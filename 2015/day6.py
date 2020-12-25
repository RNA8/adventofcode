import numpy as np


commands = ['turn on','turn off','toggle']
class Instruction:
    command = None
    x1 = None
    y1 = None
    x2 = None
    y2 = None

    def __init__(self, line):
        for command in commands:
            if line.startswith(command):
                self.command = command
                break
        *_, start_coords, _, stop_coords = line.split()
        self.x1, self.y1 = map(int,start_coords.split(','))
        self.x2, self.y2 = map(int,stop_coords.split(','))
       
with open('inputs/day6.txt','r') as fid:
    data = fid.read().splitlines()

GRID_SIZE = 1000

# part 1
lights = np.zeros((GRID_SIZE,GRID_SIZE), dtype='bool')
for line in data:
    instr = Instruction(line)
    if instr.command == 'turn off':
        lights[instr.y1:instr.y2+1, instr.x1:instr.x2+1] = False
    elif instr.command == 'turn on':
        lights[instr.y1:instr.y2+1, instr.x1:instr.x2+1] = True
    elif instr.command == 'toggle':
        lights[instr.y1:instr.y2+1, instr.x1:instr.x2+1] = ~lights[instr.y1:instr.y2+1, instr.x1:instr.x2+1]
print(f"Part 1: Number of lit lights = {np.count_nonzero(lights)}")

# part 2
lights = np.zeros((GRID_SIZE,GRID_SIZE), dtype='int')
for line in data:
    instr = Instruction(line)
    if instr.command == 'turn off':
        lights[instr.y1:instr.y2+1, instr.x1:instr.x2+1] = np.maximum(lights[instr.y1:instr.y2+1, instr.x1:instr.x2+1]-1,0)
    elif instr.command == 'turn on':
        lights[instr.y1:instr.y2+1, instr.x1:instr.x2+1] += 1
    elif instr.command == 'toggle':
        lights[instr.y1:instr.y2+1, instr.x1:instr.x2+1] += 2
print(f"Part 2: Total brightness = {np.sum(lights)}")
