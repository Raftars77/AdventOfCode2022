
elves_data = open("input","r").read().strip().split("\n\n")

elves_data = [sum([int(calorie) for calorie in elf.split("\n")]) for elf in elves_data]

print("Most calories carried by an elf:",max(elves_data))
