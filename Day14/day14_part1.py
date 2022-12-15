with open("input","r") as file: input = file.read().strip().split('\n')

rows = [[list(map(int,a.split(','))) for a in x.split(' -> ')] for x in input]

#Function that add all points between 2 to the cave map
def cave_mapping(x1, y1, x2, y2):
    if x1 == x2: cave_map.update([tuple((x1,y)) for y in range(min(y1,y2),max(y1,y2)+1)])
    if y1 == y2: cave_map.update([tuple((x,y1)) for x in range(min(x1,x2),max(x1,x2)+1)])

cave_map = set()
for row in rows:
    for i in range(len(row)-1): 
        cave_mapping(row[i][0],row[i][1],row[i+1][0],row[i+1][1])

#Function that simulates the path of one sand element
def sand_falling(x,y):
    while True:
        y = y+1
        if (y > y_max) : return False
        if (x, y) in cave_map : x = x-1 #If Collision bellow
        if (x, y) in cave_map : x = x+2 #If Collision left diagonal
        if (x, y) in cave_map : #If Collision rigth diagonal
            cave_map.add((x-1,y-1))
            return True

_,y_max = max(cave_map, key = lambda x: x[1])
sand = 0
while True: 
    if not sand_falling(500,0) : break
    sand += 1

print("Sand placed before starting to flow into abyss:",sand)