
input = open("input","r").read().rstrip().split('\n')

pairs = [list(map(int,coordinate.replace('-',',').split(','))) for coordinate in input]

contained_pairs = 0
for pair in pairs:
    if((pair[0]<=pair[2] and pair[1]>=pair[3]) or (pair[0]>=pair[2] and pair[1]<=pair[3])): 
        contained_pairs += 1

print("Pairs fully contained by another:",contained_pairs)