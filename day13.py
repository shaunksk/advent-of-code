import pandas as pd
import numpy as np

# Data Prep
xy_values = []
instructions = []
for line in open("day13-input.txt","r"):
    if line.strip() == "": 
        pass
    elif line[:10] == "fold along":
        instructions.append(line.strip()[11:].split("="))
    else:
        xy_values.append(line.strip().split(","))

x_max = pd.DataFrame(xy_values,dtype=int).apply(pd.to_numeric)[0].max()
y_max = pd.DataFrame(xy_values,dtype=int).apply(pd.to_numeric)[1].max()
paper = np.full((y_max+1, x_max+1), ".")

for coordinate in xy_values:
    paper[int(coordinate[1])][int(coordinate[0])] = "#"

for fold in instructions:
    y_len = len(paper)
    x_len = len(paper[0])
    fold_coord = int(fold[1])

    if fold[0] == "y":
        for y in range(fold_coord+1,y_len):
            for x in range(x_len):
                if paper[y][x] == "#":
                    y_reflect = fold_coord-(y-fold_coord)
                    try:
                        paper[y_reflect][x] = "#"
                    except IndexError:
                        pass
        paper = np.delete(paper, range(fold_coord,y_len), axis=0)

    elif fold[0] == "x":
        for y in range(y_len):
            for x in range(fold_coord+1,x_len):
                if paper[y][x] == "#":
                    x_reflect = fold_coord-(x-fold_coord)
                    try:
                        paper[y][x_reflect] = "#"
                    except IndexError:
                        pass
        paper = np.delete(paper, range(fold_coord,x_len), axis=1)
    
    if fold == instructions[0]:
        print("Dots visible after first fold",np.count_nonzero(paper == "#"))

print(pd.DataFrame(paper))
        
# Answer = HLBUBGFR