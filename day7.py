# Day 7 - The Treachery of Whales - find a way to make all crab submarines horizontal positions match while requiring them to spend as little fuel as possible.

import pandas as pd
import numpy as np

df = pd.read_csv("day7-input.txt",delimiter=",",dtype=int,header = None)   # convert input into dataframe
df = df.T
print(df)

# Part 1 - How much fuel must they spend to align to that position?

# Find total fuel cost for each horizontal position and then find the minimum total fuel cost
# Note: fuel cost is absolute difference between position we are evaluating and position of crab

df_fuel_track = pd.DataFrame(data={'position': [], 'total_fuel': []})
for x in range(df.min()[0],df.max()[0]+1,1):
    total_fuel_cost = abs(df-x).sum()[0]
    df_fuel_track = df_fuel_track.append(pd.DataFrame([[x,total_fuel_cost]],columns=['position','total_fuel']))
    
print(df_fuel_track)
print("Part 1 - Minimum Total fuel:",df_fuel_track['total_fuel'].min())

# Part 2 - Fuel cost is changed 
"""
Now fuel cost corresponds to triangle numbers relative to absolute difference
Eg.  1st step costs 1, the 2nd step costs 2 (total of 3), the third step costs 3 (total of 6), and so on.
Formula for the nth number in a triangular number sequence is n(n+1)/2 so we can use this to calculate fuel cost 
"""

df_fuel_track = pd.DataFrame(data={'position': [], 'total_fuel': []})
for x in range(df.min()[0],df.max()[0]+1,1):
    total_fuel_cost = (abs(df-x)*(abs(df-x)+1)/2).sum()[0]
    # print(total_fuel_cost)
    df_fuel_track = df_fuel_track.append(pd.DataFrame([[x,total_fuel_cost]],columns=['position','total_fuel']))
    
print(df_fuel_track)
print("Part 2 - Minimum Total fuel:",df_fuel_track['total_fuel'].min())