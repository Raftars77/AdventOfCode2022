import heapq
with open("input","r") as file: input = file.read().strip().split('\n')

board = [[column for column in row ] for row in input]
rows,columns = len(board), len(board[0])

for row in range(rows):
    for column in range(columns):
        if board[row][column] == 'S': 
            board[row][column] = 'a' #Problem says to take S as a a
            S_x, S_y = row, column
        elif board[row][column] == 'E': 
            board[row][column] = 'z' #Problem says to take E as a z
            E_x, E_y = row, column
    
visited = [[False] * columns for _ in range(rows)]
visited[S_x][S_y] = True
movements = [[0,1],[1,0],[0,-1],[-1,0]]
path_queue = []
heapq.heappush(path_queue,(0, S_x, S_y))
#function that adds all posible steps from a position x,y to heap
def path(x, y, steps):
    for movement in movements:
        next_x, next_y = movement[0]+x, movement[1]+y
        if not ((0 <= next_x < rows) and (0 <= next_y < columns)): continue
        elif visited[next_x][next_y]: continue
        elif ord(board[next_x][next_y])-ord(board[x][y])>1: continue

        visited[next_x][next_y] = True
        heapq.heappush(path_queue,(steps+1, next_x, next_y))

while True:
    steps, x, y = heapq.heappop(path_queue)
    if x==E_x and y==E_y: break
    #As we are always keeping track of the shortest path we can simply 'restart'
    #the steps each time we found an a in our heap because it will be from where
    #our new path will start
    elif board[x][y]=='a': steps=0 
    path(x, y, steps)

print("Fewest steps required to go from any \'a\' to \'E\':",steps)