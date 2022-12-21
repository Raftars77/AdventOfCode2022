with open("input","r") as file : jet_pattern = [*file.read().strip()]

jet_move = { '<' : -1, '>' : 1 }
rocks = [
    [[3,4],[4,4],[5,4],[6,4]],
    [[4,6],[3,5],[4,5],[5,5],[4,4]],
    [[5,6],[5,5],[3,4],[4,4],[5,4]],
    [[3,7],[3,6],[3,5],[3,4]],
    [[3,5],[4,5],[3,4],[4,4]]
]

def move_rock(rock, jet_index, y_top):
    while True:
        jet, jet_index = jet_pattern[jet_index%len(jet_pattern)], jet_index+1
        new_rock = [[x+jet_move[jet],y] for x,y in rock] #We aply the movement to a temporary rock to see if its possible to move
        if max(new_rock)[0] != x_right and min(new_rock)[0] != x_left and rocks_map.isdisjoint(set(map(tuple,new_rock))) : rock = new_rock
        for x,y in rock : 
            if (x,y-1) in rocks_map : 
                rocks_map.update(map(tuple, rock)) #Update the rock map
                y_top = max(rock,key=lambda x: x[1])[1] if max(rock,key=lambda x: x[1])[1]>y_top else y_top
                return jet_index, y_top
        rock = [[x,y-1] for x,y in rock]

y_top, jet_index = 0, 0
x_left, x_right = 0, 8
rocks_map = set(((1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0)))
for i in range(2022):
    rock = [[x,y+y_top] for x,y in rocks[i%5]] #Because we have 5 rocks and we want to repeat them
    jet_index, y_top = move_rock(rock, jet_index, y_top)

print("The tower will be '"+str(y_top)+"' units tall if you drop 2.022 rocks")