from itertools import permutations

with open('inputs/day9.txt','r') as fid:
    data = fid.read().splitlines()

TEST = False
if TEST:
    data = ["London to Dublin = 464",
    "London to Belfast = 518",
    "Dublin to Belfast = 141"]
unique_places = sorted(list({x for datum in data for x in datum.split(' = ')[0].split(' to ')}))
print(f"{len(unique_places)} unique places:")
print(unique_places)


# compute distances
distances = {}
for datum in data:
    path, distance = datum.split(' = ')
    source, destination = path.split(' to ')
    distances[(source,destination)] = int(distance)
    distances[(destination,source)] = int(distance)

# enumerate all permutations, since there are only 8 places
shortest_distance = min(str(sum(distances[from_to] for from_to in zip(combo[:-1],combo[1:])))
                        for combo in permutations(unique_places, len(unique_places)))
print(f"Part 1: shortest distance = {shortest_distance}")

# enumerate all permutations, since there are only 8 places
longest_distance = max(str(sum(distances[from_to] for from_to in zip(combo[:-1],combo[1:])))
                       for combo in permutations(unique_places, len(unique_places)))
print(f"Part 2: longest distance = {longest_distance}")