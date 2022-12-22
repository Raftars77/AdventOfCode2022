from collections import deque
with open("input","r") as file : input = file.read().strip().split()

movements = [[0,0,1],[0,0,-1],[0,1,0],[0,-1,0],[1,0,0],[-1,0,0]]

cubes = [list(map(int,cube.split(','))) for cube in input]
cubes_map = {(x,y,z): 0 for x,y,z in cubes}

#Function that returns the min/max value from the cubes_map in the index given 
def getBorder(op, index):
    return min(cubes,key=lambda x: x[index])[index]-1 if op == 'min' else max(cubes,key=lambda x: x[index])[index]+1

x_min, y_min, z_min = getBorder('min',0), getBorder('min',1), getBorder('min',2)
x_max, y_max, z_max = getBorder('max',0), getBorder('max',1), getBorder('max',2)

queue = deque([(x_min,y_min,z_min)])
outside = {(x_min,y_min,z_min)}
while queue:
    x, y, z = queue.popleft()
    for xx, yy, zz in movements:
        cx, cy, cz = x+xx, y+yy, z+zz
        #Check if the next square is inside the grid borders
        if not (x_min <= cx <= x_max and y_min <= cy <= y_max and z_min <= cz <= z_max) : continue
        #Check if in that square there is a cube
        if (cx, cy, cz) in cubes_map: cubes_map[(cx, cy, cz)] += 1
        #If there is no cube add it to the outside squares
        elif (cx, cy, cz) not in outside : 
            queue.append((cx, cy, cz))
            outside.add((cx, cy, cz))

print("Exterior surface area of the lava droplet:",sum(cubes_map.values()))