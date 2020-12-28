with open('inputs/day23.txt','r') as fid:
    data = fid.read().splitlines()


def process_instructions(a_init=0, b_init=0):
    registers = {'a':a_init,'b':b_init}
    ptr = 0
    while ptr < len(data):
        # print(f"{ptr}:{data[ptr]}")
        parts = data[ptr].replace(',','').split()
        if parts[0] == 'hlf':
            registers[parts[1]] *= 0.5
            ptr += 1
        elif parts[0] == 'tpl':
            registers[parts[1]] *= 3
            ptr += 1
        elif parts[0] == 'inc':
            registers[parts[1]] += 1
            ptr += 1
        elif parts[0] == 'jmp':
            ptr += int(parts[1])
        elif parts[0] == 'jie':
            if registers[parts[1]] % 2 == 0:
                ptr += int(parts[2])
            else:
                ptr += 1
        elif parts[0] == 'jio':
            if registers[parts[1]] == 1:
                ptr += int(parts[2])
            else:
                ptr += 1
    return registers

registers = process_instructions(a_init=0, b_init=0)
print(f"Part 1: Register b value = {registers['b']}")
registers = process_instructions(a_init=1, b_init=0)
print(f"Part 2: Register b value = {registers['b']}")
            