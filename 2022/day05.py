import re
import os 

# Read in Data
f = open(os.path.dirname(os.path.abspath(__file__)) + '/day05.txt', 'r')
content = f.read()
f.close()

## Split into instructions and create stack
content = [x for x in content.split('\n\n')]

## Format Instructions 
instructions = content[1]
# instructions example
# instructions = """move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2
# """
instructions = [x for x in instructions.split('\n')]
instructions = [[int(y) for y in re.findall(r'\d+', x)] for x in instructions]

## Format Stack
stack=content[0]
stack = [
    ['H','R','B','D','Z','F','L','S'],
    ['T','B','M','Z','R'],
    ['Z','L','C','H','N','S'],
    ['S','C','F','J'],
    ['P','G','H','W','R','Z','B'],
    ['V','J','Z','G','D','N','M','T'],
    ['G','L','N','W','F','S','P','Q'],
    ['M','Z','R'],
    ['M','C','L','G','V','R','T']
]

# stack example
# stack = [
#     ['z','n'],
#     ['m','c','d'],
#     ['p']
# ]

for x in range(len(instructions)):
    if len(instructions[x]) == 0: break
    
    move = instructions[x][0]
    origin = instructions[x][1]-1
    destination = instructions[x][2]-1

    # Move from origin to destination reversing order - delete end of list where origin is
    moving = stack[origin][-move:]

    # Reverse list if part 1 
    # moving.reverse() 

    stack[destination] = stack[destination] + moving
    stack[origin] = stack[origin][:-move]


print(''.join([x[-1] for x in stack]))
