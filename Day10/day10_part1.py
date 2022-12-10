with open("input","r") as file:
    input = file.read().strip().split('\n')

simulation = []
for cycle in input:
    if 'addx' in cycle:
        name,x = cycle.split(' ')
        simulation.append(name)
        simulation.append(x)
    else: simulation.append(cycle)

x,i = 1,1
cycles = [20,60,100,140,180,220]
signal_strength = 0
for instruction in simulation:
    if i in cycles: signal_strength+=x*i
    if 'addx' not in instruction and 'noop' not in instruction: x+=int(instruction)
    i+=1

print("Sum of the signal strengths:",signal_strength)