import os
f = open(os.path.dirname(os.path.abspath(__file__)) + '/day06.txt', 'r')
content = f.read()
f.close()

# Example
# content = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'

def solve(len_marker):
    for x in range(len(content)):
        if len(content[x:x+len_marker]) == len(set(content[x:x+len_marker])):
            print(x+len_marker)
            print(content[x:x+len_marker])
            break

# Part 1
solve(44)

# Part 2
solve(14)
