TEST_RAW = ['""',
'"abc"',
'"aaa\\"aaa"',
'"\\x27"']
data = TEST_RAW

with open('inputs/day8.txt','r') as fid:
    data = fid.read().splitlines()


def count_parse_string(string):
    # remove the end quotes
    string = string[1:-1]
    output_string_count = 0
    i = 0
    while i < len(string):
        if string[i]=='\\':
            # if \xNN, one char for 4 input chars
            if string[i+1]=='x':
                i += 4
            else: # otherwise, one char for 2 input chars
                i += 2
        else: # for everything else, one char per input char
            i += 1
        output_string_count += 1
    return output_string_count


num_char_code = sum(map(len,data))
num_char_value = sum(map(count_parse_string, data))
print(f"Part 1: Answer = {num_char_code - num_char_value}")

def count_unparse_string(string):
    # count 2 chars for \ and ", 1 for all others
    # add 2 more extra for starting and ending "
    return sum([2 if x in ['"','\\'] else 1 for x in string]) + 2

num_char_code = sum(map(len,data))
num_new_char_value = sum(map(count_unparse_string, data))
print(f"Part 2: Answer = {num_new_char_value - num_char_code}")