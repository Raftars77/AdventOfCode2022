from string import ascii_letters

input = open("input","r").read().rstrip().split('\n')

letters_score = {letter : score+1 for (score, letter) in enumerate(ascii_letters)}

badges=[]
for elves_group in range(len(input)//3):
    rucksack1, rucksack2, rucksack3 = input[elves_group*3:elves_group*3+3]
    for item in rucksack1:
        if item in rucksack2 and item in rucksack3: 
            badges.append(item)
            break

print("The sum if the priorities of the badges is:",sum(letters_score[i] for i in badges))