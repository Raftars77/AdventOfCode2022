import re
from math import lcm
with open("input","r") as file:
    input = file.read().strip().split('\n\n')

rounds = 10000 #Rounds to be simulated
monkeys = []
for monkey in input:
    dict = {}
    _,items,op,div,if_true,if_false = monkey.split('\n')
    dict['items']=[int(item) for item in re.findall(r'\d+',items)]
    dict['op']=eval('lambda old:'+op.split('=')[1]) #lambda function for operation
    dict['div']=int(re.findall(r'\d+',div)[0])
    dict['if_true']=int(re.findall(r'\d+',if_true)[0])
    dict['if_false']=int(re.findall(r'\d+',if_false)[0])
    dict['inspected_items']=0
    monkeys.append(dict)

lcm_div = lcm(*[monkey['div'] for monkey in monkeys])
#Simulates 1 round for all the monkeys
def monkeys_round():
    for monkey in monkeys:
        for _ in range(len(monkey['items'])):
            item = monkey['items'].pop(0)
            item = monkey['op'](item)
            item %= lcm_div #make item value be in the interval [0,lcm]
            if item%monkey['div']==0: monkeys[monkey['if_true']]['items'].append(item)
            else: monkeys[monkey['if_false']]['items'].append(item)
            monkey['inspected_items'] += 1

for _ in range(rounds): monkeys_round()

monkey_business = [monkey['inspected_items'] for monkey in monkeys]
monkey_business.sort()
print("Level of monkey business:",monkey_business[-1]*monkey_business[-2])