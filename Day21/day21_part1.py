with open("input","r") as file : input = file.read().strip().split('\n')

monkeys_dict = {}

for line in input: 
    monkey, yell = line.split(': ')
    if(len(yell.split(' '))>1) :
        lmonkey, operator, rmonkey = yell.split(' ')
        monkeys_dict[monkey] = {'yell' : [lmonkey,rmonkey]  , 'function' : eval("lambda " + lmonkey + "," + rmonkey + ":" + yell)}
    else : 
        monkeys_dict[monkey] = {'yell' : int(yell)}

#Simulate what each monkey will yell
def monkey_yell(monkey):
    if type(monkeys_dict[monkey]['yell']) == int : return monkeys_dict[monkey]['yell']
    else :
        lmonkey, rmonkey = monkeys_dict[monkey]['yell']
        lmonkey_val = monkey_yell(lmonkey)
        rmonkey_val = monkey_yell(rmonkey)
    return monkeys_dict[monkey]['function'](lmonkey_val,rmonkey_val)

print("'Root' the monkey will yell '" + str(int(monkey_yell('root'))) + "'")   