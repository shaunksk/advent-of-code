import os
f = open(os.path.dirname(os.path.abspath(__file__)) + '/day07.txt', 'r')
content = f.read()
# print(content)
f.close()


## assign value dictionary using location list tree
def write_value(overall_dict, loc_list, new_value):
    #tobe_eval = "overall_dict['"+"']['".join(loc_list) +"']"+ "=new_value"
    # exec(tobe_eval)
    #print(overall_dict,loc_list)
    if len(loc_list) == 1:
        print("assigning value", new_value,"with key", loc_list, "in", overall_dict)
        if type(new_value) == list:
            overall_dict[loc_list[0]] = new_value
        else:
            overall_dict[loc_list[0]].append(new_value)

    else:
        print(overall_dict, loc_list, new_value)
        overall_dict[loc_list[0]] = write_value({},loc_list[1:], new_value)
    #for key, value in overall_dict.items():
    #    if key == loc_list[0]:
    #        if type(value) == dict:
    #            write(value, loc_list[1:],new_value)
    #        else:
    #            print("bottom value")
    #            value = new_value

   # dict['root'] = value
    return overall_dict

## instruct what actions done for each command
total = {}

def process_struct(current_loc, command,overall_dict = {},sum_val_dict ={}):
    cmd_pt1 = command.split(" ")[0] 
    cmd_pt2 = command.split(" ")[-1] 

    if command == "$ cd ..":
        print(total,current_loc,sum_val_dict)
        total[current_loc[-1]] = sum_val_dict[current_loc[-1]]
        current_loc.pop()
        sum_val_dict.pop( current_loc[-1])
    elif command[:4] == "$ cd":
        #overall_dict = write_value(overall_dict, current_loc + [cmd_pt2],[])
        sum_val_dict[cmd_pt2] = 0
        current_loc.append(cmd_pt2)
    elif cmd_pt2 == "ls" or cmd_pt1 == "dir":
        pass
    else:
        #overall_dict = write_value(overall_dict, current_loc + [cmd_pt2], cmd_pt1)
        for key, value in sum_val_dict.items():
            value += int(cmd_pt1)
       

    return current_loc, overall_dict, sum_val_dict

## loop through all commands
overall_dict = {}
loc = []
sum_val_dict = {}
counter =0
for line in content.split("\n"):
    counter +=1
    if line == "$ cd /": line = "$ cd root"
    print(line)
    loc, overall_dict, sum_val_dict = process_struct(loc, line, overall_dict, sum_val_dict)
    #print(overall_dict)
    #if counter == 4: break
#print(overall_dict)
print(total)
# sum all values in each directory
sum = 0
for key, value in total.items():
    if value < 100000:
        sum +=  value 

print(sum)
