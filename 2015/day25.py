
def iterate_code():
    start = 20151125
    value = start
    while True:
        yield value
        value = (value * 252533) % 33554393

    raise StopIteration

target_row = 2947
target_col = 3029

# in i-th diagonal, the row+col = i+1
# so for element in (row,col), we should 
# look at the (row+col-1)th diagonal
# for nth diagonal, indices go from 
#   start_index = int(n*(n-1)/2) + 1 = offset + 1
#   stop_index = int((n+1)*n/2) = offset + n
#       where offset = int(n*(n-1)/2)
# k-th number on that diagonal corresponds to column k

diagonal_num = target_row + target_col - 1
offset = int(diagonal_num*(diagonal_num-1)/2)
target_idx = offset + target_col
# find the target_idx-th number of the sequence
print(f"Find the {target_idx}-th number of the sequence")
gen = iterate_code()
for i in range(target_idx):
    val = next(gen)
print(f"Part 1: Answer = {val}")