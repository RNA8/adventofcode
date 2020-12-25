

def get_instructions(instructions):
    for char in instructions:
        yield char

def process_instruction(loc, instruction):
    x,y = loc
    if instruction == '>':
        x += 1
    elif instruction == '<':
        x -= 1
    elif instruction == '^':
        y += 1
    elif instruction == 'v':
        y -= 1
    return x,y

with open('inputs/day3.txt','r') as fid:
    data = fid.read().splitlines()[0]

delivered_houses = {}
loc = (0,0)
for instruction in get_instructions(data):
    loc = process_instruction(loc, instruction)
    delivered_houses[loc] = delivered_houses.get(loc,0) + 1
num_houses = len(delivered_houses)
print(f"Part 1: Number of houses with >= 1 present = {num_houses}")



delivered_houses = {}
santa_loc = (0,0)
robo_santa_loc = (0,0)
instr_gen = get_instructions(data)
while True:
    try:
        santa_loc = process_instruction(santa_loc, next(instr_gen))
        delivered_houses[santa_loc] = delivered_houses.get(santa_loc,0) + 1
    except StopIteration:
        break
    try:
        robo_santa_loc = process_instruction(robo_santa_loc, next(instr_gen))
        delivered_houses[robo_santa_loc] = delivered_houses.get(robo_santa_loc,0) + 1
    except StopIteration:
        break

num_houses = len(delivered_houses)
print(f"Part 2: Number of houses with >= 1 present = {num_houses}")
