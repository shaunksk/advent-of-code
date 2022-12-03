from collections import Counter
import os 

f = open(os.path.dirname(os.path.abspath(__file__)) + '/day3.txt', 'r')
content = f.read()
print(content)
f.close()

########## PART 1 ##########
char_priority = {chr(y):y-96 for y in range(97,123)} | {chr(y):y-38 for y in range(65,91)}

sum_priorities = 0
for line in content.split('\n'):
    if line == '': break
    section_len = int(len(line)/2)

    first_section = line[:section_len]
    second_section = line[section_len:]

    strings = [first_section, second_section]
    counters = [Counter(s) for s in strings]
    common_letter = list(counters[0] & counters[1])[0]
    item_priority = char_priority[common_letter]

    sum_priorities += item_priority

print(sum_priorities)


########## PART 2 ###########

sum_priorities =0
strings = []
counter = 0
for line in content.split('\n'):
    counter+=1
    strings.append(line)
    if line == '': break

    if counter%3 == 0:
        counters = [Counter(s) for s in strings]
        common_letter = list(counters[0] & counters[1] & counters[2])[0]
        item_priority = char_priority[common_letter]

        sum_priorities += item_priority
        strings = []

print(sum_priorities)