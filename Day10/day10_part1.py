with open("input","r") as file:
    input = file.read().strip().split(' ')
#making command addx 15 split into two elements of the list simulates 
#the 2 cycles needed as we only compute numeric elements in the list
simulation = input = [element for pair in input for element in pair.split('\n')]

x,i = 1,1
cycles = [20,60,100,140,180,220]
signal_strength = 0
for instruction in simulation:
    if i in cycles: signal_strength+=x*i
    if 'addx' not in instruction and 'noop' not in instruction: x+=int(instruction)
    i+=1

print("Sum of the signal strengths:",signal_strength)