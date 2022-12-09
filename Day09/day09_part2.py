import numpy as np
with open("input","r") as file:
    input = file.read().strip().split('\n')

movements = {
    'R' : [0,1],
    'D' : [1,0],
    'L' : [0,-1],
    'U' : [-1,0]
 }

# Function that simulates the movements of the head of the rope
def set_head_path(head_x=0, head_y=0):
    for move_set in input:
        movement,times = move_set.split(' ')
        for _ in range(int(times)):
            head_x,head_y = np.array([head_x,head_y])+movements[movement]
            head_positions.append([head_x,head_y])

head_positions = []
set_head_path()

for i in range(9):
    tail_positions = [[0,0]]
    tail_x, tail_y = 0,0
    for head_x,head_y in head_positions[1:]:
        if abs(head_x-tail_x)<=1 and abs(head_y-tail_y)<=1: continue
        tail_x += 0 if abs(head_x-tail_x)==0 else (head_x-tail_x)//abs((head_x-tail_x))
        tail_y += 0 if abs(head_y-tail_y)==0 else (head_y-tail_y)//abs((head_y-tail_y))
        tail_positions.append([tail_x,tail_y])
    head_positions=tail_positions.copy()

print("Number of positions visited by the tail:",len({tuple(pos) for pos in tail_positions}))