from string import ascii_letters

input = open("input","r").read().rstrip().split('\n')

letters_score = {letter : score+1 for (score, letter) in enumerate(ascii_letters)}
items=[]
for rucksack in input:
    first_compartment = rucksack[:len(rucksack)//2]
    second_compartment = rucksack[len(rucksack)//2:]
    for item in first_compartment:
        if item in second_compartment: 
            items.append(item) 
            break

print("The sum if the priorities is:",sum(letters_score[i] for i in items))