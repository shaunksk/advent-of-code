import pandas as pd
import numpy as np

df = pd.read_csv("day10-input.txt",delimiter="/n",dtype=str,header = None, names=['input'],engine='python')   # convert input into dataframe
print(df)

# Part 1 - Bracket syntax checker - find first illegal character in each corrupted line (eg. "{([(<{}[<>[]}>{[]{[(<()>" ) 
# then add up points of all lines according to the points system below. 
# The next closing bracket should corresponding last opened bracket
"""
): 3 points.
]: 57 points.
}: 1197 points.
>: 25137 points.
"""

def corrupted_score(x):
    open_brackets = '([{<'
    close_brackets = ')]}>'
    bracket_dict = {"(": ")", "[": "]", "{": "}", "<": ">"}
    bracket_score_dict = {")":3, "]":57, "}":1197, ">":25137}
    unresolved_brackets = ''

    # Loop through all brackets in the line and apply logic
    for char in x:
        # if open bracket then record bracket
        if char in open_brackets:
            unresolved_brackets += char
        # if close bracket then check that it correpsonds to the last opening bracket if not then error
        elif char in close_brackets:
            if bracket_dict[unresolved_brackets[-1]] == char:
                unresolved_brackets = unresolved_brackets[:-1]
            else:
                print("Expected ", bracket_dict[unresolved_brackets[-1]] ,", but found", char ,"instead.")
                print("Score:",bracket_score_dict[char])
                return bracket_score_dict[char]
    return 0

df["Score"] = df["input"].apply(corrupted_score)

print(df)
print(df["Score"].sum())

# Part 2 - Auto complete Incomplete Lines - Calculate score from autocomplete char string
"""
Start with a total score of 0. Then, for each character, multiply the total score by 5 
and then increase the total score by the point value given for the character in the following table:
): 1 point.
]: 2 points.
}: 3 points.
>: 4 points.
"""

# Filter for only incomplete lines
df = df[df["Score"]==0]

def autocomplete_score(x):
    open_brackets = '([{<'
    close_brackets = ')]}>'
    bracket_dict = {"(": ")", "[": "]", "{": "}", "<": ">"}
    bracket_score_dict = {")":1, "]":2, "}":3, ">":4}
    unresolved_brackets = ''
    score = 0
    
    # Loop through all brackets in the line and apply logic
    for char in x:
        # if open bracket then record bracket
        if char in open_brackets:
            unresolved_brackets += char
        # if close bracket then check that it correpsonds to the last opening bracket if not then error
        elif char in close_brackets:
            if bracket_dict[unresolved_brackets[-1]] == char:
                unresolved_brackets = unresolved_brackets[:-1]

    # Find Autocomplete string and calculate score
    autocomplete_chars = [bracket_dict[x] for x in unresolved_brackets[::-1]]
    for char in autocomplete_chars:
        score = (score*5) + bracket_score_dict[char]
    return score

df["auto_score"] = df["input"].apply(autocomplete_score)
df = df.sort_values(by=['auto_score'])

print(df)
print("Middle Score for incomplete lines",df.iloc[int((len(df)/2)+0.5-1)])