from itertools import permutations

with open('inputs/day13.txt','r') as fid:
    data = fid.read().splitlines()


people = list(set([name 
                   for datum in data 
                   for name in [datum[:-1].split()[0],datum[:-1].split()[0]]]))
people.sort()

# create a lookup table for happiness points for each pair of persons
happinessLUT = {}
for datum in data:
    parts = datum[:-1].split()
    person1 = parts[0]
    person2 = parts[-1]
    key = (person1,person2)
    points = int(parts[3])
    if parts[2] == 'lose':
        happinessLUT[key] = -points
    elif parts[2] == 'gain':
        happinessLUT[key] = points

def calculate_net_happiness(seating):
    value = sum(happinessLUT[(a,b)] + happinessLUT[(b,a)] 
                for a,b in zip(seating, seating[1:] + seating[:1]))
    return value

# run all possible permutations, even the ones that are circular symmetric
max_happiness = 0
best_seating = None
for seating in permutations(people,len(people)):
    happiness = calculate_net_happiness(seating)
    if happiness > max_happiness:
        max_happiness = happiness
        best_seating = seating
print(f"Part 1: Best seating = {best_seating}, best happiness = {max_happiness}")


for person in people:
    happinessLUT[('me',person)] = 0
    happinessLUT[(person,'me')] = 0

people.append('me')
# run all possible permutations, even the ones that are circular symmetric
max_happiness = 0
best_seating = None
for seating in permutations(people,len(people)):
    happiness = calculate_net_happiness(seating)
    if happiness > max_happiness:
        max_happiness = happiness
        best_seating = seating
print(f"Part 2: Best seating = {best_seating}, best happiness = {max_happiness}")
