import re
input = open("input","r").read().rstrip().split('\n\n')

stacks, rearrangement_procedure = [data.split('\n') for data in input]

#Treatment for stacks data
stacks = [row.replace('    ',' ').split(' ') for row in stacks if " 1 " not in row]
crate_stacks = [list(a for a in reversed(x) if a!='') for x in zip(*stacks)]

#Treatment for movements data
rearrangement_procedure = [list(map(int, re.findall(r'\d+',movement))) for movement in rearrangement_procedure]

#crates_picked = []
for crates_moved,from_stack,to_stack in rearrangement_procedure:
    for movement in range(-crates_moved,0):
        crate_stacks[to_stack-1].append(crate_stacks[from_stack-1].pop(movement))
    #Another way of doing this but using list totally as a FIFO data structure (comment the two lines above to try this and uncomment crated_picked = [])
    # for _ in range(crates_moved):
    #     crates_picked.append(crate_stacks[from_stack-1].pop())
    # for _ in range(crates_moved):
    #     crate_stacks[to_stack-1].append(crates_picked.pop())
    
print("Crates on top of each stack:",''.join([re.findall(r'\[(.*?)\]',crate[-1])[0] for crate in crate_stacks]))