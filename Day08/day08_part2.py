import numpy as np
with open("input","r") as file:
    input = file.read().strip().split('\n')

height_map = np.asarray([list(int(tree) for tree in tree_row) for tree_row in input])

rows,columns = np.shape(height_map)
visible_trees = np.zeros((rows,columns)).astype(int)

for row in range(rows):
    for column in range(columns):
        total_right, total_down, total_up, total_left = 0,0,0,0
        for tree in range(column+1,columns):
            if height_map[row, column] > height_map[row, tree]: total_right += 1
            else:
                total_right += 1
                break
        
        for tree in range(column-1,-1,-1):
            if height_map[row, column] > height_map[row, tree]: total_left += 1
            else:
                total_left += 1
                break

        for tree in range(row+1,rows):
            if height_map[row, column] > height_map[tree, column]: total_down += 1
            else:
                total_down += 1
                break

        for tree in range(row-1,-1,-1):
            if height_map[row, column] > height_map[tree, column]: total_up += 1
            else:
                total_up += 1
                break
        
        visible_trees[row,column] = total_down*total_up*total_left*total_right

print("Highest scenic score possible for any tree:",np.amax(visible_trees))