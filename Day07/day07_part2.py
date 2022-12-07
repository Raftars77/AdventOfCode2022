import re
with open("input","r") as file:
    input = file.read().strip().split('\n')

#Recursive function for exploring directories
def dir_explorer(line_index):
    i=line_index
    directory_size=0
    while i < len(input):
        if len(re.findall(r'\d+',input[i]))!=0: directory_size+=int(re.findall(r'\d+',input[i])[0])
        if 'cd ..' in input[i]:
            directories_sizes.append(directory_size)
            return directory_size,i
        if '$ cd' in input[i]:
            subdirectory_size,i=dir_explorer(i+1)
            directory_size+=subdirectory_size            
        i+=1

    directories_sizes.append(directory_size)   
    return directory_size,i


directories_sizes = []
dir_explorer(1)

disk_space = 70000000-directories_sizes[-1]
possible_directories = []
for size in directories_sizes:
    if disk_space+size >= 30000000:
        possible_directories.append(size)
      
print("Size of smallest directory to delete:",min(possible_directories))
