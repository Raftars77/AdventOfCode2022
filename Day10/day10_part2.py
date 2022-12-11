with open("input","r") as file:
    input = file.read().strip().split(' ')
#making command addx 15 split into two elements of the list simulates 
#the 2 cycles needed as we only compute numeric elements in the list
simulation = [element for pair in input for element in pair.split('\n')]

x,i = 1,0
crt = []
for instruction in simulation:
    crt.append('#' if i%40==x or i%40==(x-1) or i%40==(x+1) else '.')
    if 'addx' not in instruction and 'noop' not in instruction: x+=int(instruction)
    i+=1

for crt_row in range(0,len(crt),40): 
    print(''.join(crt[crt_row:crt_row+40]))