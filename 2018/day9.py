import operator
from time import time
RAW = '403 players; last marble is worth 71920 points'

# create a doubly-linked list with clockwise and counter-clockwise 
# pointers instead of left/right
class Marble:
    cw = None # node clockwise
    ccw = None # node counter-clockwise
    value = None

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return "Marble (%d)" % (self.value)

def play_game(max_marbles, num_players):

    circle = [Marble(i) for i in range(max_marbles+1)]

    def print_nodes(curr_node, player=None):
        if player is None:
            print("[-]", end=' ')
        else:
            print("[%d]" % (player), end=' ')
        node = circle[0]
        if node.value == curr_node.value:
            print("(%d)" % (node.value), end=' ')
        else:
            print("%d" % (node.value), end=' ')
        node = node.cw
        while node.value != 0:
            if node.value == curr_node.value:
                print("(%d)" % (node.value), end=' ')
            else:
                print("%d" % (node.value), end=' ')
            node = node.cw
        print("", end='\n')

    next_idx = 0
    curr = circle[next_idx]
    curr.ccw = curr
    curr.cw = curr
    # print_nodes(curr)
    player_scores = {x:0 for x in range(1,num_players+1)}
    for i in range(1,max_marbles+1):
        player_num = ((i-1) % num_players) + 1
        next_idx += 1
        if next_idx % 23 == 0:
            player_scores[player_num] += next_idx
            # 7-th marble counter-clockwise
            remove_marble = curr.ccw.ccw.ccw.ccw.ccw.ccw.ccw
            new_curr = curr.ccw.ccw.ccw.ccw.ccw.ccw
            player_scores[player_num] += remove_marble.value
            remove_marble.ccw.cw = new_curr
            new_curr.ccw = remove_marble.ccw
            curr = new_curr
        else:
            new_marble = circle[next_idx]
            new_marble.cw, new_marble.ccw = curr.cw.cw, curr.cw
            curr.cw.cw = new_marble
            new_marble.cw.ccw = new_marble
            curr = new_marble
        # print_nodes(curr, player_num)

    winning_player, winning_score = max(player_scores.items(), key=operator.itemgetter(1))
    return winning_score


# tests
assert play_game(max_marbles=25, num_players=9) == 32
assert play_game(max_marbles=1618, num_players=10) == 8317
assert play_game(max_marbles=7999, num_players=13) == 146373
assert play_game(max_marbles=1104, num_players=17) == 2764
assert play_game(max_marbles=6111, num_players=21) == 54718
assert play_game(max_marbles=5807, num_players=30) == 37305
# Part 1
timer = time()
part1_answer = play_game(max_marbles=71920, num_players=403)
print(f"Part 1: Answer = {part1_answer}, elapsed time is {time() - timer} seconds")
# Part 1
part2_answer = play_game(max_marbles=7192000, num_players=403)
print(f"Part 2: Answer = {part2_answer}, elapsed time is {time() - timer} seconds")