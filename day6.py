# Day 6 - Exponential growth of lanternfish
import pandas as pd
import numpy as np

df = pd.read_csv("day6-input.txt",delimiter=",",dtype=int,header = None)   # convert input into dataframe
print(df)

# Part 1 - how many lanternfish after 80 days

# Loop through 80 days and 
for i in range(80):
    # Count number of zeroes in last day
    new_fish = (df.iloc[-1, :]==0).sum()    
    print(i," ",new_fish)

    # If last day has value 0 then, change to 6, else minus 1 from value
    df.loc[len(df)] = np.where(df.iloc[-1, :]==0, 6, df.iloc[-1, :]-1)  # 

    # Append new fish values as 8, to the end of the dataframe (make new fish)
    new_fish_range = list(range(len(df.columns),len(df.columns)+new_fish))
    df.loc[len(df)-1, new_fish_range]=8

print(df)
print(len(df.columns))

# Part 2 - how many lanternfish after 256 days - due to the exponential growth and amount of time taken to run, we need to optimise

# Create table showcasing how many of each internal timer values there are
df = df.T
table = df[0].value_counts()
table = table.append(pd.Series([0, 0, 0, 0], index=[6,7,8,0]))
table = table.sort_index()
print(table)

# Replicate lantern spawning process by updating counts of each internal timer value - this method is alot faster
for i in range(256):
    temp_table = table.copy()
    for i in table.index:
        if i == 8:  table[i] = temp_table[0]
        elif i == 6:table[i] = temp_table[i+1] + temp_table[0]
        else:       table[i] = temp_table[i+1]   
            
print(table)
print(table.sum())
