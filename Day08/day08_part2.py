import numpy as np
with open("input","r") as file:
    input = file.read().strip().split('\n')

height_map = np.asarray([list(int(tree) for tree in tree_row) for tree_row in input])

movements = [[0,1],[1,0],[0,-1],[-1,0]]
rows,columns = np.shape(height_map)
visible_trees_map = np.ones((rows,columns)).astype(int)

for row in range(rows):
    for column in range(columns):
        for movement in movements:
            visible_trees = 0
            next_x, next_y = np.array([row,column])+movement
            while next_x >= 0 and next_x < columns and next_y >= 0 and next_y < rows:
                if height_map[row, column] > height_map[next_x, next_y]: visible_trees +=1
                else:
                    visible_trees += 1
                    break
                next_x, next_y = np.array([next_x,next_y])+movement
            visible_trees_map[row, column]*=visible_trees

print("Highest scenic score possible for any tree:",np.amax(visible_trees_map))