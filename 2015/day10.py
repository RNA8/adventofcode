import sys
import numpy as np
RAW = "1113122113"
TEST_RAW = "111221"

def process_string_numpy(string):
    x = np.array(list(map(int,'0'+string+'0')))
    idx, *_ = np.nonzero(np.diff(x))
    return ''.join([str(a)+b 
                    for a,b in zip(np.diff(idx),
                                [RAW[i] for i in idx[:-1]])])

def process_string_simple(string):
    i = 0
    curr_char = string[i]
    curr_char_count = 1
    new_string = []
    while i < len(string)-1:
        if string[i+1]==curr_char:
            curr_char_count += 1
            i += 1
        else:
            new_string.append(str(curr_char_count) + curr_char)
            # reset new current char and count
            curr_char = string[i+1]
            curr_char_count = 1
            i += 1
    new_string.append(str(curr_char_count) + curr_char)
    return ''.join(new_string)

num_iters = 40
for i in range(num_iters):
    RAW = process_string_simple(RAW)
print(f"Part 1: {len(RAW)}")

num_additional_iters = 10
for i in range(num_additional_iters):
    RAW = process_string_simple(RAW)
print(f"Part 2: {len(RAW)}")
