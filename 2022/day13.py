import os
from functools import cmp_to_key

# Read in Data
f = open(os.path.dirname(os.path.abspath(__file__)) + '/day13.txt', 'r')
content = f.read()
f.close()

content_part2 = content
content = [[eval(y) for y in x.split('\n')] for x in content.split('\n\n')]


def is_right_order(left,right):
    # if both integers, compare the 2 integers are higher. Correct order if left < right, futher comparison needed if equal, else incorrect order
    if type(left) == int and type(right) == int:
        if left < right:    return True
        elif left == right: return 'NA'
        else:               return False

    # combination of lists of lits and integer     
    else:
        # if left or right is integer then convert to list for comparison
        if type(left) == int: left = [left]
        if type(right) == int: right = [right]

        # loop through left and right lists and compare values
        for x in range(max(len(left),len(right))):
            try:
                order_bool = is_right_order(left[x],right[x])
                if order_bool in (True,False):
                    return order_bool

            except IndexError:
                # error due to referencing index bigger than list. if left is bigger than right then wrong order
                if len(left) > len(right):
                    return False
                else:
                    return True

# Loop through pair and record index if correct order
right_order_idx = []
for pair_idx in range(len(content)):
    left, right = content[pair_idx][0], content[pair_idx][1]
    order_bool = is_right_order(left,right)
    if order_bool: right_order_idx.append(pair_idx+1)
    
print('part 1:',sum(right_order_idx))

#### Part 2

# Format Data and add [[2]] and [[6]] to list
content_part2 = content_part2.replace('\n\n','\n')
content_part2 = [eval(x) for x in content_part2.split('\n')]
content_part2 = content_part2[:-1]
content_part2.extend([[[2]],[[6]]])

def sort_order(left,right):
    if is_right_order(left,right):
        return -1
    else:
        return 1

# Sort list based on sort_order and is_right_order function
part2 =  sorted(content_part2, key=cmp_to_key(sort_order))

first_idx = part2.index([[2]]) + 1
second_idx = part2.index([[6]]) + 1
print('part 2:',first_idx*second_idx)
