with open("input","r") as file:
    datastream = file.read().strip()

marker = 14
for character in range(len(datastream)-13):
    char_pack = set(datastream[character:character+14])
    if len(char_pack) >= 14: break
    marker += 1

print("First marker after the character:",marker)