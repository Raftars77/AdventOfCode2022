import numpy as np
with open("input","r") as file:
    input = file.read().strip().split('\n')

height_map = np.asarray([list(int(tree) for tree in tree_row) for tree_row in input])

visible_trees=0
rows,columns = np.shape(height_map)

for row in range(rows):
    for column in range(columns):
        if row == 0 or row == (rows-1) or column == 0 or column == (columns-1):
            visible_trees += 1
        else:
            if np.amax(height_map[row, column+1:]) < height_map[row, column]: visible_trees += 1
            elif np.amax(height_map[row+1:, column]) < height_map[row, column]: visible_trees += 1
            elif np.amax(height_map[row, :column]) < height_map[row, column]: visible_trees += 1
            elif np.amax(height_map[:row, column]) < height_map[row, column]: visible_trees += 1

print("Number of trees visible from outside the grid:",visible_trees)