#This program might take ~4secs to calculate the result
with open("input","r") as file : input = list(map(int,[*file.read().strip().split('\n')]))

#As there can be repeated numbers we will asocciate each pos to a tuple (index,value)
encrypted = [tuple((x*811589153,k)) for k,x in enumerate(input)]
mixed = encrypted.copy()
l = len(mixed)

for _ in range(10):
    for x,k in encrypted:
        i = mixed.index((x,k))
        move_to = (i + x) % (l-1)
        if move_to == 0 : move_to = l
        mixed.pop(i)
        mixed.insert(move_to,((x,k)))
    
zero = [i for i, v in enumerate(mixed) if v[0] == 0][0]
print("Sum of the three numbers that form the grove coordinates:",mixed[(zero+1000)%l][0]+mixed[(zero+2000)%l][0]+mixed[(zero+3000)%l][0])