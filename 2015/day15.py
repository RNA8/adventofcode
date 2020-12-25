import numpy as np
from itertools import product
class Ingredient:
    name = None
    scores = None
    def __init__(self, line):
        self.name, parts = line.split(': ')
        parts = parts.replace(',','').split()
        assert len(parts)==10, parts
        self.scores = np.array(list(map(int,parts[1::2]))).reshape((1,-1))

    def __str__(self):
        return "%s [%d,%d,%d,%d,%d]" % (self.name, *list(self.scores[0]))

    def __repr__(self):
        return "%s [%d,%d,%d,%d,%d]" % (self.name, *list(self.scores[0]))

def get_mixture_score(weights, score_array):
    score_totals = np.maximum(np.dot(weights,score_array), 0)
    return np.product(score_totals[:-1])


data = ["Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8",
"Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"]
ingrs = [Ingredient(line) for line in data]
ingredient_score_array = np.concatenate([ingr.scores for ingr in ingrs])
assert get_mixture_score([44,56], ingredient_score_array)==62842880

with open('inputs/day15.txt','r') as fid:
    data = fid.read().splitlines()
ingrs = [Ingredient(line) for line in data]
ingredient_score_array = np.concatenate([ingr.scores for ingr in ingrs])
calories = ingredient_score_array[:,-1]

# Part 1
best_score = 0
best_combo = None
for a,b,c,d in product(range(1,101), repeat=4):
    if (a+b+c+d==100) and (2*d - 3*a > 0) and (4*c - 2*d > 0) and (3*a - 3*b - c > 0):
        score = get_mixture_score([a,b,c,d], ingredient_score_array)
        if score > best_score:
            best_score = score
            best_combo = [a,b,c,d]
print(f"Part 1: best_score={best_score}, weight={a,b,c,d}")


# Part 2
best_score = 0
best_combo = None
for a,b,c,d in product(range(1,101), repeat=4):
    if (a+b+c+d==100) and np.dot(calories,[a,b,c,d])==500 and (2*d - 3*a > 0) and (4*c - 2*d > 0) and (3*a - 3*b - c > 0):
        score = get_mixture_score([a,b,c,d], ingredient_score_array)
        if score > best_score:
            best_score = score
            best_combo = [a,b,c,d]
print(f"Part 2: best_score={best_score}, weight={a,b,c,d}")



