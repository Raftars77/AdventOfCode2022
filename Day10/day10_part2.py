with open("input","r") as file:
    input = file.read().strip().split('\n')

simulation = []
for cycle in input:
    if 'addx' in cycle:
        name,x = cycle.split(' ')
        simulation.append(name)
        simulation.append(x)
    else: simulation.append(cycle)

x,i = 1,0
crt = []
for instruction in simulation:
    crt.append('#' if i%40==x or i%40==(x-1) or i%40==(x+1) else '.')
    if 'addx' not in instruction and 'noop' not in instruction: x+=int(instruction)
    i+=1

for crt_row in range(0,len(crt),40): 
    print(''.join(crt[crt_row:crt_row+40]))