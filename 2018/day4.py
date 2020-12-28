import numpy as np
import operator
from datetime import datetime, timedelta
import re

with open('inputs/day4.txt','r') as fid:
    data = fid.read().splitlines()
# sort the data first
data = sorted(data)
# anything that is 23:xx, round up to next day 00:00, since 0-hour is the only thing that matters
# this only happens for 'begins shift', so doesn't affect minutes asleep
refined_data = []
for datum in data:
    line = datum.replace('[','').replace(']','')
    date, time, *rest = line.split()
    if time.startswith('23'):
        # verify that this only happens for 'begins shift'
        assert line.endswith('begins shift')
        new_date_time = (datetime.strptime(date,'%Y-%m-%d')+timedelta(1)).strftime('%Y-%m-%d %H:%M')
        line = ' '.join([new_date_time]+rest)
    refined_data.append(line)

# get unique dates, need to re-sort since list(set(x)) seems to shuffle 
dates = sorted(list(set(line.split()[0] for line in refined_data)))

# create a date x minute matrix
date_time_matrix = np.zeros((len(dates),60))

reg = re.compile(r'Guard #\d+')
reg_minute = re.compile(r':\d+')
date_guards = np.zeros(len(dates), dtype='int')
for i,date in enumerate(dates):
    subset = [datum for datum in refined_data if date in datum]
    guard_id = [int(x.replace('Guard #','')) for s in subset for x in reg.findall(s)][0]
    date_guards[i] = guard_id
    assert len(subset) % 2 == 1
    fall_asleep_times = subset[1::2]
    wake_up_times = subset[2::2]
    assert all('falls asleep' in x for x in fall_asleep_times)
    assert all('wakes up' in x for x in wake_up_times)
    for fa,wu in zip(fall_asleep_times,wake_up_times):
        fall_asleep_minute = int(reg_minute.findall(fa)[0][1:])
        wake_up_minute = int(reg_minute.findall(wu)[0][1:])
        date_time_matrix[i,fall_asleep_minute:wake_up_minute] = 1
unique_guards = np.unique(date_guards)

guard_sleep_time = {}
for guard_id in unique_guards:
    guard_sleep_time[guard_id] = int(date_time_matrix[date_guards==guard_id].sum())
    # print(f"Guard #{guard_id}: total sleep time = {guard_sleep_time[guard_id]}")
most_asleep_guard, most_asleep_guard_sleep_time = max(guard_sleep_time.items(), key=operator.itemgetter(1))
print(f"Guard #{most_asleep_guard} sleeps the most, for {most_asleep_guard_sleep_time} minutes")
most_asleep_minute = date_time_matrix[date_guards==most_asleep_guard].sum(axis=0).argmax()
print(f"Most asleep minute is {most_asleep_minute}")
print(f"Part 1: Answer = {most_asleep_minute * most_asleep_guard}")


max_most_asleep_times = 0
chosen_most_asleep_minute = None
chosen_guard = None
for guard_id in unique_guards:
    guard_minute_histogram = date_time_matrix[date_guards==guard_id].sum(axis=0)
    most_asleep_minute = guard_minute_histogram.argmax()
    most_asleep_times = guard_minute_histogram.max()
    if most_asleep_times > max_most_asleep_times:
        max_most_asleep_times = most_asleep_times
        chosen_guard = guard_id
        chosen_most_asleep_minute = most_asleep_minute
print(f"Most asleep on same minute: guard #{chosen_guard}, minute = {chosen_most_asleep_minute}")
print(f"Part 2: Answer = {chosen_guard*chosen_most_asleep_minute}")
