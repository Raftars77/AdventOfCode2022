
elves_data = open("input","r").read().strip().split("\n\n")

elves_data = [sum([int(calorie) for calorie in elf.split("\n")]) for elf in elves_data]

elves_data.sort(reverse=True)
top3_elves = []
for i in range(3):
    top3_elves.append(elves_data[i])

print("Sum of calories from the top 3 elves:",sum(top3_elves))
