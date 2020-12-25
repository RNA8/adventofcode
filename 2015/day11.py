import numpy as np
import string

RAW = 'vzbxkghb'

letters = list(string.ascii_lowercase)
next_letter = {letters[i]:letters[(i+1) % 26] for i in range(len(letters))}
# since i, o, l are not allowed, remove them from next_letter dictionary
next_letter['h'] = 'j'
next_letter['n'] = 'p'
next_letter['k'] = 'm'

triplets = [a + b + c for a,b,c in zip(letters[:-2], letters[1:-1], letters[2:])]

def is_valid_password(password):
    # short circuiting checks
    # increasing triplets
    if not any(x in password for x in triplets):
        return False
    # forbidden letters
    if any(x in password for x in ['i','o','l']):
        return False
    # 2 sets of consecutive letters are identical
    doublets = [i for i,(x,y) in enumerate(zip(password[:-1],password[1:])) if x==y]
    if len(doublets) >= 2 and np.diff(doublets).max()>=2:
        return True
    else:
        return False


assert is_valid_password('hijklmmn') is False
assert is_valid_password('abbceffg') is False
assert is_valid_password('abbcegjk') is False

def increment_password(password):
    # split and reverse
    pw_letters = list(password)[::-1]
    for i in range(len(pw_letters)):
        pw_letters[i] = next_letter[pw_letters[i]]
        # if rolls over, continue changing the next character
        # otherwise, break
        if pw_letters[i] == 'a': # just rolled over
            continue
        else:
            break
    # reverse and combine
    password = ''.join(pw_letters[::-1])

    # TODO: if password contains i,o,l directly jump to next one without i,o,l
    return password

def next_valid_password(password):
    password = increment_password(password)
    while not is_valid_password(password):
        password = increment_password(password)
    return password

assert next_valid_password('abcdefgh') == 'abcdffaa'
# assert next_valid_password('ghijklmn') == 'ghjaabcc'
new_password = next_valid_password(RAW)
print(f"Part 1: {new_password}")
new_password = next_valid_password(new_password)
print(f"Part 2: {new_password}")
