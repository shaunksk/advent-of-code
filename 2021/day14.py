import string
import collections

# Data Prep
template = ""
pair_dict = {}

for line in open("day14-input.txt","r"):
    print(line)
    break

for line in open("day14-input.txt","r"):
    line = line.strip()
    if line == "":
        pass
    elif len(line) == 7:
        pair_dict[line[:2]] = line[-1:]
    else:
        template = line

print(template)


# Part 1 - Apply 10 steps of pair insertion to the polymer template 
# and find the most and least common elements in the result. 
# What do you get if you take the quantity of the most common element 
# and subtract the quantity of the least common element?

# Loop through steps
for step in range(10):
    temp_template = ''

    # Loop through each char in template
    for char_num in range(len(template)-1):
        pair = template[char_num:char_num+2] 

        # If first char then intialise first 3 chars of template after insertion, else add on next new pair after insertion
        if char_num == 0:
            temp_template = pair[0] + pair_dict[pair] + pair[1]
        else:
            temp_template = temp_template + pair_dict[pair] + pair[1]

    template = temp_template


# Find most/least common chars and claculate answer
most_common = collections.Counter(temp_template).most_common(1)[0]
least_common = collections.Counter(temp_template).most_common()[-1]
ans = most_common[1]-least_common[1]

print("Part 1 Answer: ", ans)


# Part 2 - Apply 40 steps of pair insertion with the same logic
# Same method cant be used as polymer increases in size exponentially
# causing performance issues

# Data Prep
template = ""
pair_dict = {}
pair_count = {}

for line in open("day14-input.txt","r"):
    line = line.strip()
    if line == "":
        pass
    elif len(line) == 7:
        pair_dict[line[:2]] = line[-1:]
        pair_count[line[:2]] = 0
    else:
        template = line

print(template)
print(pair_dict)
print(pair_count)

# Store counts of each pair in pair_count dictionary
for char_num in range(len(template)-1):
    pair_count[template[char_num:char_num+2]] +=1

# Loop through steps
for step in range(40):
    # print("step",step+1)
    
    # Create dictionary to store current values of pair counts
    temp_dict = {k: v for k, v in pair_count.items() if v >0}
    
    # Loop through pair counts and increase/decrease tally as chars are inserted
    for pair in temp_dict:
        # Record count of pair
        temp_count = temp_dict[pair]
        
        # Add count of pair to 2 different pairs - e.g. if inserting C in between AB, need to add count to AC and CB
        pair_count[pair[0] + pair_dict[pair]] += temp_count
        pair_count[pair_dict[pair] + pair[1]] += temp_count
        
        # Subtract the recorded count from the current pair as the pair no longer exists
        pair_count[pair] -= temp_count

# Create dictionary of all letters
element_dict = dict.fromkeys(string.ascii_uppercase, 0)

# Count individual letters in the pair counts
for pair in pair_count:
    element_dict[pair[0]] += pair_count[pair]
    element_dict[pair[1]] += pair_count[pair]

# Add 1 to count of first and last letter in template and then divide all counts by 2 as they have been counted twice in pairs
element_dict[template[0]] += 1
element_dict[template[-1]] += 1
element_dict = {k: v/2 for k, v in element_dict.items() if v >0}
print(element_dict)

# Find most/least common chars and claculate answer
max = element_dict[max(element_dict, key=element_dict.get)]
min = element_dict[min(element_dict, key=element_dict.get)]
print("Part 2 Answer: ",max - min)

