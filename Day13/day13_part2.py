with open("input","r") as file: input = [row for row in file.read().strip().split('\n\n')]

pairs = [eval(list_pair) for list_pairs in input for list_pair in list_pairs.split('\n')]
div1, div2 = [[2]], [[6]]
pairs.extend((div1, div2)) 

def right_order(n1,n2):
    if type(n1) == int and type(n2) == int: return n2-n1
    if type(n1) != list : n1=[n1]
    if type(n2) != list : n2=[n2]
    for nn1,nn2 in zip(n1,n2):
        comp = right_order(nn1,nn2)
        if comp != 0 : return comp
    if len(n1) < len(n2) : return 1
    if len(n1) > len(n2) : return -1
    return 0

for i in range(len(pairs),0,-1):
    for j in range(i-1):
        if right_order(pairs[j],pairs[j+1]) < 0 :
            pairs[j], pairs[j+1] = pairs[j+1], pairs[j]

print("Decoder key for the distress signal:",(pairs.index(div1)+1)*(pairs.index(div2)+1))