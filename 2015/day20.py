from math import sqrt

RAW = '29000000'

def get_factors(num):
    '''
    get all factors of num, including 1 and num
    '''
    factors = [i for i in range(1,int(sqrt(num))) if num % i == 0]
    factors.extend([num//i for i in factors])
    if int(sqrt(num))**2 == num:
        factors.append(int(sqrt(num)))
    return factors

target_presents = int(RAW)
house_num_part1 = None
house_num_part2 = None
for house_num in range(1,target_presents//10):
    factors = get_factors(house_num)
    # part 1, 10 presents per elf
    num_presents_part1 = 10*sum(factors)
    # part 2, 11 presents per elf up to 50 houses
    num_presents_part2 = 11*sum(factor for factor in factors 
                                       if house_num/factor <= 50)

    if not house_num_part1 and num_presents_part1 >= target_presents:
        house_num_part1 = house_num
        print(f"Part 1: House num = {house_num_part1}")

    if not house_num_part2 and num_presents_part2 >= target_presents:
        house_num_part2 = house_num
        print(f"Part 2: House num = {house_num_part2}")

    # stop when both parts are solved
    if house_num_part1 and house_num_part2:
        break
    if house_num % 10000 == 0:
        print(f"Checked {house_num} houses...", end='\r')