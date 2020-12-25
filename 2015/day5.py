
with open('inputs/day5.txt','r') as fid:
    data = fid.read().splitlines()

def is_nice(string):
    num_vowels = sum(string.count(vowel) for vowel in 'aeiou')
    # short-circuiting checks
    if num_vowels < 3:
        return False
    # check if any 2 consecutive letters are identical
    if not any(x==y for x,y in zip(string[:-1],string[1:])):
        return False
    # check if any of the forbidden substrings are present
    if any(doublet in string for doublet in ['ab','cd','pq','xy']):
        return False
    return True
    
# part 1
num_nice_strings = sum(1 for datum in data if is_nice(datum))
print(f"Part 1: {num_nice_strings} nice strings")

def is_nice_part2(string):
    # check for rule #1 
    nice = False
    for i in range(len(string)-1):
        if string[i:i+2] in string[i+2:]:
            nice = True
            break
    if not nice:
        return False
    # check for rule #2 (xyx, efe, ...)
    if not any(x==z for x,y,z in zip(string[:-2], string[1:-1], string[2:])):
        return False
    return True

# part 2
num_nice_strings = sum(1 for datum in data if is_nice_part2(datum))
print(f"Part 2: {num_nice_strings} nice strings")