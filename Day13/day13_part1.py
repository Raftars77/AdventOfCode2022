with open("input","r") as file: input = [row for row in file.read().strip().split('\n\n')]

pairs = [[eval(list_pair) for list_pair in list_pairs.split('\n')] for list_pairs in input]    

#Returns 0 if equal, -n if lower and +n if greater
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

right_order_index = []
for index in range(len(pairs)):
    if right_order(pairs[index][0],pairs[index][1]) > 0 : right_order_index.append(index+1)

print("Sum of the index of the pairs in right order:",sum(right_order_index))