with open("input","r") as file : input = file.read().strip().split()

movements = [[0,0,1],[0,0,-1],[0,1,0],[0,-1,0],[1,0,0],[-1,0,0]]

cubes = [list(map(int,cube.split(','))) for cube in input]
cube_map = {}
for x,y,z in cubes:
    cube_map[(x,y,z)]=6
    for xx,yy,zz in movements: 
        #Check it the cube has an adjacent cube
        #If it has substract 1 face to each cube
        if (x+xx,y+yy,z+zz) in cube_map.keys() : 
            cube_map[(x+xx,y+yy,z+zz)] -= 1
            cube_map[(x,y,z)] -= 1

print("Surface area of the lava droplet:",sum(cube_map.values()))