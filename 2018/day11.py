import numpy as np

grid_serial_num = 5468

num_rows = num_cols = 300
fuel_cells = np.zeros((num_rows+1,num_cols+1))
for row in range(1,num_rows+1):
    for col in range(1,num_cols+1):
        rack_id = col + 10
        power_level = (rack_id * row + grid_serial_num) * rack_id
        power_level = (power_level // 100) % 10
        fuel_cells[row,col] = power_level - 5

total_power = np.zeros((num_rows+1,num_cols+1))
for row in range(1,num_rows+1-2):
    for col in range(1,num_cols+1-2):
        total_power[row,col] = fuel_cells[row:row+3,col:col+3].sum()
best_total_power = np.max(total_power)
rows, cols = np.nonzero(total_power==best_total_power)
print(f"Part 1: Answer = {cols[0]},{rows[0]}")

# Part 2
results = []
for sz in range(1,num_rows+1):
    total_power = np.zeros((num_rows+1,num_cols+1))
    for row in range(1,num_rows+1-(sz-1)):
        for col in range(1,num_cols+1-(sz-1)):
            total_power[row,col] = fuel_cells[row:row+sz,col:col+sz].sum()
    best_total_power = np.max(total_power)
    if best_total_power==0:
        break
    rows, cols = np.nonzero(total_power==best_total_power)
    if len(rows)==1:
        results.append([cols[0],rows[0],sz,best_total_power])

results = np.array(results).astype('int')
best_results = results[np.argmax(results[:,-1])]
x,y,size,power = best_results
print(f"Part 2: Answer = {x,y,size}, max power = {power}")