with open('inputs/day16.txt','r') as fid:
    data = fid.read().splitlines()

query = ["children: 3",
"cats: 7",
"samoyeds: 2",
"pomeranians: 3",
"akitas: 0",
"vizslas: 0",
"goldfish: 5",
"trees: 3",
"cars: 2",
"perfumes: 1"]

for i, datum in enumerate(data):
    sue_id = i + 1
    possessions = datum[datum.index(': ')+2:].split(', ')
    if all(poss in query for poss in possessions):
        print(f"Part 1: {datum}")

query = {line.split(': ')[0]:int(line.split(': ')[1]) for line in query}
class Sue:
    id = None
    possessions = {}
    def __init__(self, line):
        parts = line.replace(':','').replace(',','').split()
        self.id = int(parts[1])
        self.possessions = dict(zip(parts[2::2], map(int,parts[3::2])))

    def __repr__(self):
        return "Sue %d: " % (self.id) + str(self.possessions)

    def __str__(self):
        return "Sue %d: " % (self.id) + str(self.possessions)

    def matches_query(self, q):
        for key,value in self.possessions.items():
            if key in ['cats','trees']: # should be greater than q[key]
                if not (value > q[key]):
                    return False
            elif key in ['pomeranians','goldfish']: # should be fewer than q[key]
                if not (value < q[key]):
                    return False
            else: # should match exactly
                if not (value==q[key]):
                    return False
        return True

sues = [Sue(line) for line in data]
for sue in sues:
    if sue.matches_query(query):
        print(sue)