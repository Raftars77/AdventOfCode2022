#IT MIGHT TAKE A MINUTE TO GET A RESULT WHEN EXECUTING THIS PROGRAM
import re
with open("input","r") as file: input = file.read().strip().split('\n')

MIN_B = 0       #MIN LIMIT
MAX_B = 4000000 #MAX LIMIT

def set_area(x, y, mdistance, x_min, x_max, search_y):
    if not y-mdistance <= search_y <= y+mdistance : return x_min, x_max #This area will not affect the problem
    rango = mdistance - abs(search_y - y)
    if x_min == -1 and x_max == -1 : return x-rango, x+rango
    #Check if ranges overlap or the distance between them is 1
    if ((x_max >= x-rango and x_min <= x+rango) or (x_max <= x-rango and x_min >= x+rango) 
        or (abs(x_min-x-rango)==1) or (abs(x_max-x+rango)==1)) : 
        x_min = min(x_min,x-rango) if min(x_min,x-rango)>MIN_B else MIN_B
        x_max = max(x_max,x+rango) if max(x_max,x+rango)<MAX_B else MAX_B
    return x_min, x_max

sensor_map = []
for line in input:
    S_x, S_y, B_x, B_y = map(int,re.findall(r'[+-]?\d+',line))
    Mdistance = abs(S_x - B_x) + abs(S_y - B_y)
    sensor_map.append((S_x,S_y,Mdistance))

sensor_map.sort()
for y in range(MIN_B,MAX_B):
    x_min, x_max = -1,-1
    for S_x, S_y, Mdistance in sensor_map:
        x_min, x_max = set_area(S_x, S_y, Mdistance, x_min, x_max, y)
        if x_min==MIN_B and x_max==MAX_B: break
    if x_min!=MIN_B or x_max!=MAX_B : 
        beacon_x, beacon_y = x_max+1, y
        break #Beacon will be in x_max+1 position

print("Tuning frequency of the beacon:",(beacon_x*MAX_B)+beacon_y)