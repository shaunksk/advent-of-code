# Day 5 - Hydrothermal vents 

# Part 1 - Track what positions have 2 or more vents located on them
from typing import TYPE_CHECKING
import pandas as pd
import numpy as np

# Data Prep
df_lines = pd.read_csv("day5-input.txt",delimiter="\n",dtype=str,header = None,names=["input"])   # convert input into dataframe
df_lines= df_lines['input'].str.split(' -> ',expand=True)                     # split numbers into seperate columns
df_lines[['x1','y1']]= df_lines[0].str.split(',',expand=True)                     # split numbers into seperate columns
df_lines[['x2','y2']]= df_lines[1].str.split(',',expand=True)                     # split numbers into seperate columns
df_lines = df_lines.drop([0,1],axis=1).apply(pd.to_numeric)

# Produce diagram (represented with dataframe) of coordinate position - default is 0
max_col = df_lines[['x1','x2']].max().max()
max_row = df_lines[['y1','y2']].max().max()
df_pos = pd.DataFrame(np.zeros((max_col+1, max_row+1))).astype(int)

# Filter for only horizontal or vertical lines (perpendicular) - x1 = x2 or y1 = y2.
df_lines_perp = df_lines[(df_lines['x1'] == df_lines['x2']) | (df_lines['y1'] == df_lines['y2'])]

# Loop through line coordinates and add 1 to all coordinates on line
for index, row in df_lines_perp.iterrows():
    for i in range(min(row['x1'], row['x2']),max(row['x1'], row['x2'])+1,1):
        for j in range(min(row['y1'], row['y2']),max(row['y1'], row['y2'])+1,1):
            df_pos.iloc[i,j] += 1

print("At how many points do at least two lines overlap? ",df_pos[(df_pos > 1 )].count().sum())

# Part 2 - Factoring in 45 degree diagonal lines

# Filter for only diagonal lines
df_lines_diag = df_lines[(df_lines['x1'] != df_lines['x2']) & (df_lines['y1'] != df_lines['y2'])]
print(df_lines_diag)

# Loop through line coordinates
for index, row in df_lines_diag.iterrows():

    # Determine steps - direction of x and y coordinates - negative or positive
    x_step = 1 if row['x1'] < row['x2'] else -1
    y_step = 1 if row['y1'] < row['y2'] else -1

    # Loop through diagonals and add 1 for every coordinate on line
    for x, y in zip(range(row['x1'], row['x2']+x_step,x_step), range(row['y1'], row['y2']+y_step,y_step)):
        df_pos.iloc[x,y] += 1
        # print(x, y)


print("At how many points do at least two lines overlap after factoring in diagonals? ",df_pos[(df_pos > 1 )].count().sum())
