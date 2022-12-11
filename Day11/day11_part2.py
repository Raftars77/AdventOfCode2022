import re
import operator
from math import lcm
with open("input","r") as file:
    input = file.read().strip().split('\n\n')

operator_dicc ={
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul
}

rounds = 10000 #Rounds to be simulated
monkeys = []
for monkey in input:
    dict = {}
    _,items,op,div,if_true,if_false = monkey.split('\n')
    dict['items']=[int(item) for item in re.findall(r'\d+',items)]
    dict['op']=op.split('  Operation: new = old ')[1].split(' ')
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
            item = operator_dicc[monkey['op'][0]](item,item) if 'old' in monkey['op'] else operator_dicc[monkey['op'][0]](item,int(monkey['op'][1]))
            #make item value be in the interval [0,lcm]
            item = item-lcm_div*(item//lcm_div)
            if item%monkey['div']==0: monkeys[monkey['if_true']]['items'].append(item)
            else: monkeys[monkey['if_false']]['items'].append(item)
            monkey['inspected_items'] += 1

for _ in range(rounds): monkeys_round()

monkey_business = [monkey['inspected_items'] for monkey in monkeys]
monkey_business.sort()
print("Level of monkey business:",monkey_business[-1]*monkey_business[-2])