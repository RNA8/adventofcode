from itertools import combinations
RAW = '''Hit Points: 104
Damage: 8
Armor: 1'''

class Player:
    name = None
    hit_points = 100
    damage = 0
    armor = 0
    def __init__(self, name, hit_points, damage, armor):
        self.name = name
        self.hit_points = hit_points
        self.damage = damage
        self.armor = armor

    def __str__(self):
        return f"{self.name}: Hit points = {self.hit_points}, damage = {self.damage}, armor = {self.armor}"
    
    def __repr__(self):
        return f"{self.name}: Hit points = {self.hit_points}, damage = {self.damage}, armor = {self.armor}"

    def play_turn(self, other):
        # played by other on self
        # returns True if self "dies", i.e. hit_points <= 0
        self.hit_points -= max(1, other.damage-self.armor)
        return self.hit_points <= 0

    def is_dead(self):
        return self.hit_points <= 0


# Weapons:    Cost  Damage  Armor
shop_weapons = {'Dagger':[8,4,0],
'Shortsword':[10,5,0],
'Warhammer':[25,6,0],
'Longsword':[40,7,0],
'Greataxe':[74,8,0]}
# Armor:      Cost  Damage  Armor
shop_armors = {'Leather':[13,0,1],
'Chainmail':[31,0,2],
'Splintmail':[53,0,3],
'Bandedmail':[75,0,4],
'Platemail':[102,0,5]}
# Rings:      Cost  Damage  Armor
shop_rings = {'Damage +1':[25,1,0],
'Damage +2':[50,2,0],
'Damage +3':[100,3,0],
'Defense +1':[20,0,1],
'Defense +2':[40,0,2],
'Defense +3':[80,0,3]}

def find_spending(purchases):
    player_spending = 0
    if purchases['weapon'] is not None:
        player_spending += shop_weapons[purchases['weapon']][0]
    if purchases['armor'] is not None:
        player_spending += shop_armors[purchases['armor']][0]
    for ring in purchases['rings']:
        player_spending += shop_rings[ring][0]
    return player_spending

def play_game(purchases):
    # purchases['weapon'] is None or name of weapon
    # purchases['armor'] is None or name of armor
    # purchases['rings'] is list of len 0/1/2 names

    # initialize player and boss
    player = Player('me',100,0,0)
    boss = Player('boss',104,8,1)

    # player will buy something here
    # Can buy:
    # 1 weapon
    # 0-1 armor
    # 0-2 rings
    player_spending = find_spending(purchases=purchases)
    if purchases['weapon'] is not None:
        weapon = shop_weapons[purchases['weapon']]
        player.damage += weapon[1]
        player.armor += weapon[2]
    if purchases['armor'] is not None:
        armor = shop_armors[purchases['armor']]
        player.damage += armor[1]
        player.armor += armor[2]
    for ring in purchases['rings']:
        player.damage += shop_rings[ring][1]
        player.armor += shop_rings[ring][2]
        
    # rounds of play
    winner = None
    while True:
        if boss.play_turn(player):
            winner = 'player'
            # print(f"Player wins! Spent {player_spending} gold")
            break
        if player.play_turn(boss):
            winner = 'boss'
            # print("Boss wins!")
            break
    return winner, player_spending

# pick at most 2 rings
max_rings = 2
ring_combos = [x for num_rings in range(max_rings+1)
               for x in combinations(shop_rings,num_rings)]
# pick at most one armor
armor_combos = list(shop_armors.keys()) + [None]


# Part 1
max_gold = 100
lowest_winning_gold = max_gold
lowest_winning_purchases = None
for weapon in shop_weapons.keys(): # pick exactly one weapon
    for armor in armor_combos: # pick at most one armor
        for rings in ring_combos: # pick at most 2 rings
            purchases = {'weapon':weapon,
                        'armor':armor,
                        'rings':list(rings)}
            if find_spending(purchases) > max_gold:
                continue
            # play the game
            winner, spent_gold = play_game(purchases=purchases)
            if winner == 'player' and spent_gold < lowest_winning_gold:
                lowest_winning_gold = spent_gold
                lowest_winning_purchases = purchases

print(f"Part 1: Lowest winning gold = {lowest_winning_gold}")

# Part 1
highest_losing_gold = 0
highest_losing_purchases = None
for weapon in shop_weapons.keys(): # pick exactly one weapon
    for armor in armor_combos: # pick at most one armor
        for rings in ring_combos: # pick at most 2 rings
            purchases = {'weapon':weapon,
                        'armor':armor,
                        'rings':list(rings)}
            # play the game
            winner, spent_gold = play_game(purchases=purchases)
            if winner == 'boss' and spent_gold > highest_losing_gold:
                highest_losing_gold = spent_gold
                highest_losing_purchases = purchases

print(f"Part 2: Highest losing gold = {highest_losing_gold}")
