"""
You can model the energy levels and flashes of light in steps. During a single step, the following occurs:

First, the energy level of each octopus increases by 1.

Then, any octopus with an energy level greater than 9 flashes. This increases the energy level of all 
adjacent octopuses by 1, including octopuses that are diagonally adjacent. If this causes an octopus to 
have an energy level greater than 9, it also flashes. This process continues as long as new octopuses keep 
having their energy level increased beyond 9. (An octopus can only flash at most once per step.)

Finally, any octopus that flashed during this step has its energy level set to 0, as it used all of its energy to flash.
"""

import pandas as pd
import numpy as np

# Data Prep
content = []
for line in open("day11-input.txt","r"):
    content.append([int(x) for x in line.strip()])

len_x = len(content[0])
len_y = len(content)
flash_no = 0

# Part 1

def flash(x,y):
    # Change centre cell to -1 so that it is not accidentally flashed again
    content[y][x] = -1
    global flash_no
    flash_no +=1

    #  Add 1 to adjacent cells and flash any that become 10
    for i,j in [(x+u,y+v) for u in (-1,0,1) for v in (-1,0,1) if u != 0 or v != 0]:
        if i in range(len_x) and j in range(len_y) and content[j][i] != -1:
            content[j][i] += 1
            if content[j][i] > 9:
                flash(i,j)

for step in range(1,101): 
    # First Part - Add one to all elements
    for x in range(len_x):
        for y in range(len_y):
            content[y][x] += 1

    # Second Part - energy level greater than 9 increases adjacent points by 1 (flashes)
    for x in range(len_x):
        for y in range(len_y):
            if content[y][x] == 10:
                flash(x,y)

    # Third Part - Everything that is bigger than 9 goes to 0
    for x in range(len_x):
        for y in range(len_y):
            if content[y][x] > 9 or content[y][x] == -1: 
                content[y][x] = 0

print(pd.DataFrame(content))   
print("num of flashes:",flash_no)

# Part 2 - Find the Step where all points flash at the same time
content = []
for line in open("day11-input.txt","r"):
    content.append([int(x) for x in line.strip()])

step = 0
while True: 
    step += 1

    # First Part - Add one to all elements
    for x in range(len_x):
        for y in range(len_y):
            content[y][x] += 1

    # Second Part - energy level greater than 9 increases adjacent points by 1 (flashes)
    for x in range(len_x):
        for y in range(len_y):
            if content[y][x] == 10:
                flash(x,y)

    # Third Part - Everything that is bigger than 9 goes to 0
    for x in range(len_x):
        for y in range(len_y):
            if content[y][x] > 9 or content[y][x] == -1: 
                content[y][x] = 0

    # If all values are 0 (all flash at same time) then break and return step
    if (np.array(content)==0).all():
        break

print("All points flash at:",step)


###############################################################################
# Attempt to do logic in pandas dataframe #

df = pd.read_csv("day11-input.txt",delimiter="/n",dtype=str,header = None, names=['input'],engine='python')   # convert input into dataframe
df= df['input'].str.split("",expand=True,).apply(pd.to_numeric)                    # delimit data based on ""
df = df.drop([0],axis=1)
df = df.drop([df.columns[-1]],axis=1)
# df = df.drop([6],axis=1)
# print(df)
flash_no = 0

def flash(columnIndex,index):
    global df, flash_no
    # Change centre cell to -1 so that it is not accidentally flashed again
    df.iloc[index,columnIndex-1] = -1
    flash_no +=1
    
    for x,y in [(columnIndex-1+i,index+j) for i in (-1,0,1) for j in (-1,0,1) if i != 0 or j != 0]:
        if 0 <= x <= len(df.index)-1 and 0 <= y <= len(df.index)-1 and df.iloc[y,x] != -1:
            df.iloc[y,x] += 1 
            if df.iloc[y,x] > 9:
                flash(x+1,y)

for step in range(1,101):    
    # First Part - add one
    df = df + 1

    # Second Part - energy level greater than 9 increases adjacent points by 1
    if (df<=9).all().all():        pass
    else:
        for index, row in df.iterrows():
            for columnIndex, value in row.items():
                if value == 10:
                    flash(columnIndex,index)
                            
    # Part 3 - Everything that is bigger than 9 goes to 0
    df.iloc[:] = np.where(df>9,0,df)
    df.iloc[:] = np.where(df==-1,0,df)
    
print("flash num (pandas):", flash_no)

# Part 2 
df = pd.read_csv("day11-input.txt",delimiter="/n",dtype=str,header = None, names=['input'],engine='python')   # convert input into dataframe
df= df['input'].str.split("",expand=True,).apply(pd.to_numeric)                    # delimit data based on ""
df = df.drop([0],axis=1)
df = df.drop([df.columns[-1]],axis=1)
flash_no = 0
step = 0

while True:    
    step += 1
    # First Part - add one to all points
    df = df + 1

    # Second Part - energy level greater than 9 increases adjacent points by 1
    if (df<=9).all().all():        pass
    else:
        for index, row in df.iterrows():
            for columnIndex, value in row.items():
                if value == 10:
                    flash(columnIndex,index)
                            
    # Third Part - Everything that is bigger than 9 goes to 0
    df.iloc[:] = np.where(df>9,0,df)
    df.iloc[:] = np.where(df==-1,0,df)

    # If all values are 0 (all flash at same time) then break and return step
    if (df==0).all().all(): break

print("All points flash at (pandas):",step)
