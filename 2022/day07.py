import os
f = open(os.path.dirname(os.path.abspath(__file__)) + '/day07.txt', 'r')
content = f.read()
f.close()

## Part 1

# instruct what actions done for each terminal command
total = {}

def process_struct(current_loc, command,overall_dict = {},sum_val_dict ={}):
    cmd_pt1 = command.split(" ")[0] 
    cmd_pt2 = command.split(" ")[-1]

    # If command ic cd .. then write filepath value to final value dictionary and get rid of current path value in sum_val_dcit as we have finished counting files in that dictionary
    if command == "$ cd ..":
        total['/'.join(current_loc)] = sum_val_dict['/'.join(current_loc)]
        sum_val_dict.pop('/'.join(current_loc))
        current_loc.pop()
    
    # if command is cd into directory then append to current_loc for tracking and add file path with corresponding value
    elif command[:4] == "$ cd":
        current_loc.append(cmd_pt2)
        sum_val_dict['/'.join(current_loc)] = 0

    # if ls or dir command then do nothing
    elif cmd_pt2 == "ls" or cmd_pt1 == "dir":
        pass

    # else the command output is referencing a file. add file size to size of each directory
    else:
        for key, value in sum_val_dict.items():
            sum_val_dict[key] = value + int(cmd_pt1)

    return current_loc, overall_dict, sum_val_dict

## loop through all commands
overall_dict = {}
loc = []
sum_val_dict = {}

for line in content.split("\n"):
    if line == "$ cd /": line = "$ cd root"
    loc, overall_dict, sum_val_dict = process_struct(loc, line, overall_dict, sum_val_dict)

total.update(sum_val_dict)

# sum all values in each directory
sum = 0
for key, value in total.items():
    if value < 100000:
        sum +=  value 

print(sum)

# Part 2
unused_space = 70000000 - total['root']
space_to_be_freed = 30000000 - unused_space

stats = {k: v for k, v in total.items() if v >= space_to_be_freed}
print(stats[min(stats, key=stats.get)])