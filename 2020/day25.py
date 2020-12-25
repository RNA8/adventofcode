from itertools import count

TEST_RAW = """5764801
17807724
"""

RAW = """1965712
19072108
"""

def get_loop_size(subj_num, 
                  target_val,
                  divisor=20201227, 
                  start_val=1):
    val = start_val
    for i in count():
        val *= subj_num
        val %= divisor
        if val == target_val:
            return i+1

def run_loop(subj_num, 
             loop_size,
             divisor=20201227, 
             start_val=1):
    val = start_val
    for i in range(loop_size):
        val *= subj_num
        val %= divisor
    return val

card_pk, door_pk = map(int,RAW.split())
card_loop_size = get_loop_size(7, card_pk)
door_loop_size = get_loop_size(7, door_pk)
print(f"Card's loop size is {card_loop_size}")
print(f"Door's loop size is {door_loop_size}")
card_ek = run_loop(door_pk, card_loop_size)
door_ek = run_loop(card_pk, door_loop_size)
print(f"Card's encryption key is {card_ek}")
print(f"Door's encryption key size is {door_ek}")

