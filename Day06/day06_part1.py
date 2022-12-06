with open("input","r") as file:
    datastream = file.read().strip()

marker = 4
for character in range(len(datastream)-3):
    char_pack = set(datastream[character:character+4])
    if len(char_pack) >= 4: break
    marker += 1

print("First marker after the character:",marker)