import numpy as np
import functools

class Wiring:
    name = None
    inputs = None
    value = None
    def __init__(self, string):
        self.inputs, self.name = string.split(' -> ')
    def __str__(self):
        return f"{self.inputs} -> {self.name} ({self.value})"
    def __repr__(self):
        return f"{self.inputs} -> {self.name} ({self.value})"


with open('inputs/day7.txt','r') as fid:
    data = fid.read().splitlines()
wires = [Wiring(line) for line in data]
wires = {wire.name:wire for wire in wires}

def get_value(wire_name):
    if wire_name in wires and wires[wire_name].value is None:
        command = wires[wire_name].inputs
        if command.isnumeric():
            val = np.uint16(command)
        elif 'NOT' in command:
            val = ~(get_value(command.replace('NOT ','')))
        elif 'AND' in command:
            arg1, arg2 = map(get_value, command.split(' AND '))
            val = arg1 & arg2
        elif 'OR' in command:
            arg1, arg2 = map(get_value, command.split(' OR '))
            val = arg1 | arg2
        elif 'LSHIFT' in command:
            arg, shift_count = command.split(' LSHIFT ')
            val = get_value(arg) << int(shift_count)
        elif 'RSHIFT' in command:
            arg, shift_count = command.split(' RSHIFT ')
            val = get_value(arg) >> int(shift_count)
        else: 
            val = get_value(command)
        wires[wire_name].value = np.uint16(val)
    elif wire_name.isnumeric():
        val = np.uint16(wire_name)
        return val
    elif wires[wire_name].value is not None:
        return wires[wire_name].value
    else:
        assert False, wire_name
    return val

part1_result = get_value('a')
print(f"Part 1: Solution = {part1_result}")

# part 2 - read everything in again, since they would have been overwritten
with open('inputs/day7.txt','r') as fid:
    data = fid.read().splitlines()
wires = [Wiring(line) for line in data]
wires = {wire.name:wire for wire in wires}
# force previous output to input of b
wires['b'] = Wiring(f'{part1_result} -> b')

part2_result = get_value('a')
print(f"Part 2: Solution = {part2_result}")