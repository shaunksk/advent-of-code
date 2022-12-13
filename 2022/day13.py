import os
from functools import cmp_to_key
f = open(os.path.dirname(os.path.abspath(__file__)) + '/day13.txt', 'r')
content = f.read()
f.close()

# Example
# content = """[1,1,3,1,1]
# [1,1,5,1,1]

# [[1],[2,3,4]]
# [[1],4]

# [9]
# [[8,7,6]]

# [[4,4],4,4]
# [[4,4],4,4,4]

# [7,7,7,7]
# [7,7,7]

# []
# [3]

# [[[]]]
# [[]]

# [1,[2,[3,[4,[5,6,7]]]],8,9]
# [1,[2,[3,[4,[5,6,0]]]],8,9]
# """

content_part2 = content

content = [x.split('\n') for x in content.split('\n\n')]

def is_right_order(left,right):
    # print(left,right)
    # if both integers, compare the 2 integers are higher
    if type(left) == int and type(right) == int:
        # correct order
        if left < right:
            return True
        # same value
        elif left == right:
            # print('same value, continue')
            return 'NA'
        # wrong order
        else:
            return False
    # if both lists then compare each element of list
    elif type(left) == list and type(right) == list:
        for x in range(max(len(left),len(right))):
            # print('range',x,left,right)
            # print(left,right)
            try:
                var = is_right_order(left[x],right[x])
                if var == False:
                    # print('wrong order 1')
                    return False
                elif var == True:
                    return True
            except IndexError:
                # 
                if len(left) > len(right):
                    # print('wrong order 3')

                    return False

                else:
                    return True
                print('one list is bigger')

    else:
        # print('pre edit',left,right,type(left),type(right))
        if type(left) == int: left = [left]
        if type(right) == int: right = [right]
        # print('else')
        # print('edit',left,right)
        var = is_right_order(left,right)
        if var == False:
            # print('wrong order 2')

            return False
        elif var == True:
            return True
        # print('end')

    # return True

right_order_idx = []
for pair_idx in range(len(content)):
    left, right = eval(content[pair_idx][0]), eval(content[pair_idx][1])
    # print(left,right)
    var = is_right_order(left,right)
    # print(var)
    if var:
        right_order_idx.append(pair_idx+1)
    
    # if pair_idx == 2: break

# print(right_order_idx)
print('part 1:',sum(right_order_idx))

#### Part 2
content_part2 = content_part2.replace('\n\n','\n')
content_part2 = [x for x in content_part2.split('\n')]
content_part2 = content_part2[:-1]

content_part2 = [eval(x) for x in content_part2]
content_part2.append([[2]])
content_part2.append([[6]])
def sort_order(left,right):
    if is_right_order(left,right):
        return -1
    else:
        return 1


# print(content_part2)
part2 =  sorted(content_part2, key=cmp_to_key(sort_order))
# print(part2)

first_idx = part2.index([[2]]) + 1
second_idx = part2.index([[6]]) + 1
print('part 2:',first_idx*second_idx)