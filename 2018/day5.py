from string import ascii_uppercase, ascii_lowercase

with open('inputs/day5.txt','r') as fid:
    data = fid.read().splitlines()[0]

pairs = [a+b for a,b in zip(ascii_lowercase,ascii_uppercase)] + [b+a for a,b in zip(ascii_lowercase,ascii_uppercase)]

def process_polymer(polymer):
    string = polymer
    new_string = None
    while True:
        new_string = string
        for pair in pairs:
            new_string = new_string.replace(pair,'')
        if string==new_string:
            break
        string = new_string
    return len(string)

print(f"Part 1: Answer = {process_polymer(data)}")

shortest_polymer_length = len(data)
problem_unit = None
for char in ascii_lowercase:
    # remove this character
    datum = data.replace(char,'').replace(char.upper(),'')
    polymer_length = process_polymer(datum)
    if polymer_length < shortest_polymer_length:
        problem_unit = char
        shortest_polymer_length = polymer_length
print(f"Part 2: Removing character ({problem_unit},{problem_unit.upper()}) gives shortest polymer length of {shortest_polymer_length}")
