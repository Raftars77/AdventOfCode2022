with open("input","r") as file : jet_pattern = [*file.read().strip()]

jet_move = { '<' : -1, '>' : 1}
rocks = [
    [[3,4],[4,4],[5,4],[6,4]],
    [[4,6],[3,5],[4,5],[5,5],[4,4]],
    [[5,6],[5,5],[3,4],[4,4],[5,4]],
    [[3,7],[3,6],[3,5],[3,4]],
    [[3,5],[4,5],[3,4],[4,4]]
]

#Function that simulates dropping a rock: -Rock: rock position
#-jet_index: actual index of the jet array, -i: actual amount of rocks dropped
#-coincidences: list of already matching patterns, -rocks_map: map of all dropped rocks
def move_rock(rock, jet_index, y_top, i, coincidences, rocks_map):
    while True:
        jet, jet_index = jet_pattern[jet_index%len(jet_pattern)], jet_index+1
        new_rock = [[x+jet_move[jet],y] for x,y in rock] #We aply the movement to a temporary rock to see if its possible to move
        if max(new_rock)[0] != x_right and min(new_rock)[0] != x_left and rocks_map.isdisjoint(set(map(tuple,new_rock))) : rock = new_rock
        for x,y in rock : 
            if (x,y-1) in rocks_map : 
                rocks_map.update(map(tuple, rock)) #Update the rock map
                y_top = max(rock,key=lambda x: x[1])[1] if max(rock,key=lambda x: x[1])[1]>y_top else y_top

                #Check if we are already in a cycle and updating cycle dict
                rock_tuple = (tuple(x for x,y in rock),i%5,jet_index%len(jet_pattern)) #Get te dicc key of the actual rock
                if rock_tuple in cycle : coincidences.append([i-cycle[rock_tuple][0],y_top-cycle[rock_tuple][2]])
                else : coincidences = []
                cycle.update({(tuple(x for x,y in rock),i%5,jet_index%len(jet_pattern)): (i,jet_index,y_top)})

                return jet_index, y_top, coincidences
        rock = [[x,y-1] for x,y in rock]

#Function that simulates dropping max_iter rocks
#if -s_cycle is True we are searching for an existing cycle
def simulation(s_cycle, max_iter=1_000_000_000_000):
    rocks_map = set(((1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0)))
    coincidences = []
    y_top, jet_index = 0, 0
    for i in range(max_iter) :
        rock = [[x,y+y_top] for x,y in rocks[i%5]] #Because we have 5 rocks and we want to repeat them
        jet_index, y_top, coincidences = move_rock(rock, jet_index, y_top, i, coincidences, rocks_map)
        if len(coincidences) >= 10 and s_cycle : #Check if at least last 10 rocks coincide
            rocks_cycle, y_cicle = coincidences.pop(0) #Get the first coincidence out of the list
            acumulated_y = (max_iter//rocks_cycle)*y_cicle
            return acumulated_y, max_iter%rocks_cycle #Return how many rocks doesn't repeat a whole cycle
    return y_top,0 

cycle = {}
x_left, x_right = 0, 8
acumulated_y, max_iter = simulation(True)
remaining_y,_ = simulation(False, max_iter)

print("The tower will be '"+str(acumulated_y+remaining_y)+"' units tall if you drop 1.000.000.000.000 rocks")