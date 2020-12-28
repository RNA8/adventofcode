import sys
import re
with open('inputs/day19.txt','r') as fid:
    data = fid.read().splitlines()
# data = '''H => HO
# H => OH
# O => HH

# HOHOHO'''.splitlines()

# data = '''e => H
# e => O
# H => HO
# H => OH
# O => HH

# HOH'''.splitlines()

start_molecule = data[-1]
replacements = data[:-2]
replace_rules = {}
for line in replacements:
    key, val = line.split(' => ')
    if key in replace_rules:
        replace_rules[key].append(val)
    else:
        replace_rules[key] = [val]


# Part 1
num_combinations = 0
new_molecules = set()
for key,values in replace_rules.items():
    for k in re.finditer(key,start_molecule):
        before = start_molecule[:k.start()]
        after = start_molecule[k.end():]
        new_molecules.update([before + val + after for val in values])
print(f"Part 1: Number of unique new_molecules = {len(new_molecules)}")


# Part 2

# do reverse replacement from target replacement to 'e'
source_molecule = 'e'
reverse_transformations = {}
for line in replacements:
    p1, p2 = line.split(' => ')
    reverse_transformations[p2] = p1

from random import shuffle
max_trials = 100
max_repeats = 100
for trial in range(max_trials):
    mol = start_molecule
    keys = list(reverse_transformations.keys())
    num_replacements = 0
    for i in range(max_repeats):
        # shuffle up the keys to do substitutions in random order
        shuffle(keys)
        for key in keys:
            while key in mol:
                # replace one thing at a time
                mol = mol.replace(key,reverse_transformations[key],1)
                num_replacements += 1
                if mol == source_molecule:
                    print(f"Part 2: {num_replacements} replacements")
                    break
            if mol == source_molecule:
                break
        if mol == source_molecule:
            break
    if mol == source_molecule:
        break