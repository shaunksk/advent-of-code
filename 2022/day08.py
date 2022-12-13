import os

# Read in Data
f = open(os.path.dirname(os.path.abspath(__file__)) + '/day08.txt', 'r')
content = f.read()
f.close()

# Example input
# content = """30373
# 25512
# 65332
# 33549
# 35360
# """

content = [x for x in content.split('\n')]
content = content[:-1]

num_trees_visible = 0
x_length = len(content[0])
y_length = len(content)
scenic_score= []

def is_tree_visible(y,x):
    global num_trees_visible

    # Edge Cases
    if x == 0 or x == x_length-1:
        return True
    elif y == 0 or y == y_length-1:
        return True

    # Search to look up, down, left and right for all trees lower than the curretn trees height
    else:
        column = [int(sublist[x]) for sublist in content]
        row = content[y]

        # search up
        if all(i < int(content[y][x]) for i in column[:y]): return True
        # search down
        elif all(i < int(content[y][x]) for i in column[y+1:]): return True
        # search left
        elif all(int(i) < int(content[y][x]) for i in row[:x]): return True
        # # search right
        elif all(int(i) < int(content[y][x]) for i in row[x+1:]):return True
    
    return False

def generate_scenic_score(y,x):
    # search in all directions for num of trees seen from current location and multiply together to create scenic score
    column = [int(sublist[x]) for sublist in content]
    row = content[y]

    # search up
    trees_up = next((i+1 for i,v in enumerate(reversed(column[:y])) if v >= int(content[y][x]) or i == y-1),0)
    # search down
    trees_down = next((i+1 for i,v in enumerate(column[y+1:]) if v >= int(content[y][x]) or i == y_length-y-2),0)
    # search left
    trees_left = next((i+1 for i,v in enumerate(reversed(row[:x])) if int(v) >= int(content[y][x]) or i == x-1),0)
    # search right
    trees_right = next((i+1 for i,v in enumerate(row[x+1:]) if int(v) >= int(content[y][x]) or i == x_length-x-2),0)

    scenic_score.append(trees_up*trees_down*trees_left*trees_right)

# Loop through all trees
for y in range(len(content)):
    for x in range(x_length):
        if is_tree_visible(y,x):
            num_trees_visible += 1
        
        generate_scenic_score(y,x)


print('part 1: ',num_trees_visible)
print('part 2:',max(scenic_score))