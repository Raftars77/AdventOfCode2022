#Reorder the tree structure making human be the top node and root be 0, as left == right
#Backtracking from human node reordering the operations of the nodes that uses what the human yells
with open("input","r") as file : input = file.read().strip().split('\n')

monkeys_dict = {}
operator_dict = { '+' : '-', '-' : '+', '/' : '*', '*' : '/'} #

for line in input: 
    monkey, yell = line.split(': ')
    if(len(yell.split(' '))>1) :
        lmonkey, operator, rmonkey = yell.split(' ')
        monkeys_dict[monkey] = {'yell' : [lmonkey,rmonkey]  , 'operator' : operator, 'function' : eval("lambda " + lmonkey + "," + rmonkey + ":" + yell)}
    else :
        monkeys_dict[monkey] = {'yell' : int(yell)}

#Set which monkey uses the actual monkey yell value, this makes easier reversing the tree
for monkey in monkeys_dict: 
    if type(monkeys_dict[monkey]['yell']) != int : 
        monkeys_dict[monkeys_dict[monkey]['yell'][0]]['used_in'] = monkey
        monkeys_dict[monkeys_dict[monkey]['yell'][1]]['used_in'] = monkey

#Reorder the tree making the humn be the monkey at the top of the tree
def reorder_tree(monkey):
    if monkey == 'root' : monkeys_dict[monkey]['yell'] = 0
    else:
        used_in = monkeys_dict[monkey]['used_in']
        index = monkeys_dict[used_in]['yell'].index(monkey)
        #Check if the operators are / or -, because a = b/c not the same as a = c/b and same with -
        if (monkeys_dict[used_in]['operator'] == '/' or monkeys_dict[used_in]['operator'] == '-') and index == 1 :
            monkeys_dict[monkey]['yell'] = [monkeys_dict[used_in]['yell'][1-index],used_in]
            monkeys_dict[monkey]['operator'] =  monkeys_dict[used_in]['operator'] if used_in != 'root' else '+'
        else : 
            monkeys_dict[monkey]['yell'] = [used_in, monkeys_dict[used_in]['yell'][1-index]]
            monkeys_dict[monkey]['operator'] = operator_dict[monkeys_dict[used_in]['operator']] if used_in != 'root' else '+'
        
        #Create the new lambda function of the monkey
        monkeys_dict[monkey]['function'] = eval("lambda " + monkeys_dict[monkey]['yell'][0] + "," + monkeys_dict[monkey]['yell'][1] + ":" + monkeys_dict[monkey]['yell'][0] + monkeys_dict[monkey]['operator'] + monkeys_dict[monkey]['yell'][1])
        reorder_tree(used_in)

#Simulate what each monkey will yell
def monkey_yell(monkey):
    if type(monkeys_dict[monkey]['yell']) == int : return monkeys_dict[monkey]['yell']
    else :
        lmonkey, rmonkey = monkeys_dict[monkey]['yell']
        lmonkey_val = monkey_yell(lmonkey)
        rmonkey_val = monkey_yell(rmonkey)
    return monkeys_dict[monkey]['function'](lmonkey_val,rmonkey_val)

reorder_tree('humn')
print("Human must yell '" + str(int(monkey_yell('humn'))) + "' to pass the equality check from 'root' the monkey")