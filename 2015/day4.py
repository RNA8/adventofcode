from hashlib import md5
from itertools import count
secret_key = "yzbqklnj"

for num in count():
    md5_hash = md5((secret_key + f'{num}').encode('utf-8')).hexdigest()
    if md5_hash.startswith('00000'):
        print(f"Part 1: Answer = {num}, hash = {md5_hash}")
        break

for num in count():
    md5_hash = md5((secret_key + f'{num}').encode('utf-8')).hexdigest()
    if md5_hash.startswith('000000'):
        print(f"Part 2: Answer = {num}, hash = {md5_hash}")
        break
