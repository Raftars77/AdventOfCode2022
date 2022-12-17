import re
with open("input","r") as file: input = file.read().strip().split('\n')

Y = 2000000 # Row we are looking for

def set_area(x, y, mdistance):
    if not y-mdistance <= Y <= y+mdistance : return False #This area will not affect the problem
    rango = mdistance - abs(Y - y)
    for xx in range(x-rango,x+rango+1):
        if (xx,Y) not in sensor_map: rowY.add(xx)

sensor_map = set()
rowY = set()
for line in input:
    S_x, S_y, B_x, B_y = map(int,re.findall(r'[+-]?\d+',line))
    sensor_map.add((B_x,B_y))
    sensor_map.add((S_x,S_y))
    Mdistance = abs(S_x - B_x) + abs(S_y - B_y)
    set_area(S_x, S_y, Mdistance)

print("Number of possitions that cannot contain a beacon:",len(rowY))