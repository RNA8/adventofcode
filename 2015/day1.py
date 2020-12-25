
with open('inputs/day1.txt','r') as fid:
    data = fid.read().splitlines()[0]

# part 1
floor = data.count('(') - data.count(')')
print(f"Part 1: Floor = {floor}")

# part 2
floor = 0
for i, char in enumerate(data):
    if char == '(':
        floor += 1
    elif char == ')':
        floor -= 1
    
    if floor == -1:
        print(f"Part 2: Entered floor {floor} at char position {i+1}")
        break
