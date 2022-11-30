# Day 8: Seven Segment Search

import pandas as pd
import numpy as np

df = pd.read_csv("day8-input.txt",delimiter="/n",dtype=str,header = None, names=['input'],engine='python')   # convert input into dataframe
df= df['input'].str.split(" | ",expand=True,)                     # delimit data based on "|"
print(df)

# Part 1 - In the output values, how many times do digits 1, 4, 7, or 8 appear? - 1 = 2 segments, 4 = 4 segments, 7 = 3 segments, 8 = 7 segments

df_1478 = df.loc[:,11:14]

for col in df_1478:
    df_1478[col+4] = df_1478[col].str.len()
    # pass

# df_1478[15:18]

# df_1478['1478_appear'] = (df.loc[:,15:18]==6) | (df.loc[:,15:18]==5) 
# print((df.loc[:,15:18]==6) | (df.loc[:,15:18]==5) )


count_1478 = ((df_1478.loc[:, 15:18]==2) 
            | (df_1478.loc[:, 15:18]==4) 
            | (df_1478.loc[:, 15:18]==3) 
            | (df_1478.loc[:, 15:18]==7)).sum().sum()

print(count_1478)

# Part 2 
"""
  0:      1:      2:      3:      4:     5:      6:      7:      8:      9:
 aaaa    ....    aaaa    aaaa    ....   aaaa    aaaa    aaaa    aaaa    aaaa
b    c  .    c  .    c  .    c  b    c  b   .  b    .  .    c  b    c  b    c
b    c  .    c  .    c  .    c  b    c  b   .  b    .  .    c  b    c  b    c
 ....    ....    dddd    dddd    dddd   dddd    dddd    ....    dddd    dddd
e    f  .    f  e    .  .    f  .    f  .   f  e    f  .    f  e    f  .    f
e    f  .    f  e    .  .    f  .    f  .   f  e    f  .    f  e    f  .    f
 gggg    ....    gggg    gggg    ....   gggg    gggg    ....    gggg    gggg


 Using the diagram
 and a more generalised segment naming:

 xxxx  
z    y 
z    y 
 wwww  
t    v 
t    v 
 uuuu    

and we know:        number | 0  1  2  3  4  5  6  7  8  9
            no. of segments| 6  2  5  5  4  5  6  3  7  6
and we know what 1,4,7 and 8 are
x  - we can find what segments are in 1 but not 7 to get x
u  - we can find what number has segments from zwxyv (segments from 4 - 1 sgements + 7 segments) plus one other segment. that segment will be u
t  - segment that is not in (4 or 7) and is not u is t
9  - signal pattern for 9 is all letters apart from t
0,6- only 2 6-segment signal patterns left, 0 and 6. 0 is the pattern that has as segments from 1 in it, the other is 6
3  - 3 5-segement patterns left (2,3 and 5), 3 is the one that intersect with 1
2,5- 2 5-segment patterns left, 5 is the 1 without t, the other is 2

now we have all segment patterns identified
"""

df_seg = df.loc[:,0:9]
for col in df_seg:
    df_seg["len"+str(col)] = df_seg[col].str.len()


def logic(x):
    return x.len0

df_seg_final = df_seg.apply(lambda x: logic(x))
print(df_seg_final)