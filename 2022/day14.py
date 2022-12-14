import os
import numpy as np

f = open(os.path.dirname(os.path.abspath(__file__)) + '/day14.txt', 'r')
content = f.read()
f.close()

# Example input
# content = """498,4 -> 498,6 -> 496,6
# 503,4 -> 502,4 -> 502,9 -> 494,9
# """

content = [[tuple(int(z) for z in y.split(',') if len(z) > 0) for y in x.split(' -> ')] for x in content.split('\n')][:-1]

y_max = max(max(x[1] for x in y) for y in content)+1
x_max = max(max(x[0] for x in y) for y in content)+1

# Draw cave - loop from all the instructions - input is coordiantes and cave and output is new cave
def draw_cave(cave_canvas):
    for instructions in content:
        for x in range(len(instructions)):
            if x == len(instructions)-1:
                pass
            else:
                step = max(abs(instructions[x][0]-instructions[x+1][0]),abs(instructions[x][1]-instructions[x+1][1]))
                path = np.linspace(instructions[x],instructions[x+1],step+1)
                for x in path:
                    cave_canvas[int(x[1])][int(x[0])] = '#'
    return cave_canvas


def pour_sand(cave):
    sand_at_rest = 0
    y=0
    x=500
    counter = 0
    while True:
        # current state is bottom
        if y == len(cave)-1:
            print('end')
            break
        # Empty place below - empty place on the diagonal
        elif cave[y+1][x] == '.':
            cave[y+1][x] = 'x'
            cave[y][x] = '.'
            y += 1
        # empty on left diagonal
        elif cave[y+1][x-1] == '.':
            cave[y+1][x-1] = 'x'
            cave[y][x] = '.'
            y+=1
            x-=1
        # empty on right diagonal
        elif cave[y+1][x+1] == '.':
            cave[y+1][x+1] = 'x'
            cave[y][x] = '.'
            y+=1
            x+=1
        # if source of sand is blocked - for part 2
        elif y==0 and x==500:
            print('source blocked')
            sand_at_rest +=1
            break
        # sand comes to rest
        else:
            sand_at_rest += 1
            y=0
            x=500
        
        # counter += 1
        # if counter == 710: break
    
    return cave,sand_at_rest
        
def display_cave(cave,x_len):
    section = [[cave[i][j+490] for j in range(x_len)] for i in range(len(cave))]
    print('\n'.join([' '.join([str(cell) for cell in row]) for row in section]))

def write_cave_to_text(cave):
    with open('file.txt', 'w') as file:
        for row in cave:
            file.write(' '.join([str(item) for item in row]))
            file.write('\n')

# Part 1 
cave_canvas = [ [ '.' for i in range(x_max) ] for j in range(y_max) ]
cave = draw_cave(cave_canvas)
cave,part1 = pour_sand(cave)
print('part 1:',part1)
# display_cave(cave,20)

# Part 2
cave_canvas_2 = [ [ '.' if j != y_max+1 else '#' for i in range(x_max+500) ] for j in range(y_max+2) ]
cave_2 = draw_cave(cave_canvas_2)
cave_2,part2 = pour_sand(cave_2)
print('part 2:',part2)
# display_cave(cave_2,80)

write_cave_to_text(cave_2)