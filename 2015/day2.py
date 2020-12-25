
with open('inputs/day2.txt','r') as fid:
    data = fid.read().splitlines()


def get_paper_area(box_size):
    length, width, height = map(int,box_size.split('x'))
    side_areas = [length*width, width*height, height*length]
    return 2*sum(side_areas) + min(side_areas)

total_area = sum(map(get_paper_area, data))
print(f"Part 1: total paper sq. ft = {total_area}") 


def get_ribbon_length(box_size):
    length, width, height = map(int,box_size.split('x'))
    volume = length * width * height
    perimeters = [2*(length+width), 2*(width+height), 2*(height+length)]
    return min(perimeters) + volume

total_ribbon_length = sum(map(get_ribbon_length, data))
print(f"Part 2: total ribbon ft = {total_ribbon_length}") 
