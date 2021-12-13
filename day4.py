### Day 4 - Bingo

## Part 1 - Find first board o get bingo from provided set of boards and sequence of numbers called out
import pandas as pd
import numpy as np
import math

# Data Prep
df = pd.read_csv("day4-input.txt",delimiter="\n",dtype=str,header = None,names=["input"])   # convert input into dataframe
num_seq = [x for x in df['input'][0].split(",")]                # configure bingo number sequence
df = df.drop([0])
df['input'] = df['input'].apply(lambda x: " ".join(x.split())) # remove double spaces in input in order to be split properly
df= df['input'].str.split(' ',expand=True)                     # split numbers into seperate columns
df['amount-marked-col'] = 0     # used to track bingo for a column
df['amount-marked-row'] = 0     # used to track bingo for a row

# Loop through numbers called out for bingo
for num in num_seq:

    # Where number in sequence matches any bingo card, mark the bingo card with 0
    df.iloc[:, 0:5] = np.where(df.iloc[:, 0:5]==num, 0, df.iloc[:, 0:5])
    
    # Keep count of number of marked numbers in a row
    df['amount-marked-row'] = (df.iloc[:, 0:5]==0).sum(axis=1)

    # Keep count of number of marked numbers in a col
    for i in range(0,len(df)-5+1,5):
        df.iloc[i:i+5,5]= (df.iloc[i:i+5, 0:5]==0).sum(axis=0)

    # Check for Bingo
    bingo = df[(df['amount-marked-row'] == 5) | (df['amount-marked-col'] == 5)]
    if len(bingo) > 0:
        bingo_index = bingo.index[0]
        start_row = 5*math.floor((bingo_index-1)/5)+1
        bingo_df = df.loc[start_row:start_row+4,0:4]    # loc referring to index and column names as opposed to integer position of cell 
        bingo_df = bingo_df.apply(pd.to_numeric)
        print(bingo_df)
        
        sum = bingo_df.values.sum()
        score = sum * int(num)
        print('BINGO! Sum of unmarked: ', sum, ', Score: ', score)
        break

## Part 2 - Anti Bingo - find the board which will "bingo" last

# Loop through numbers called out for bingo
for num in num_seq:
    # print("num: ",num)

    # Where number in sequence matches any bingo card, mark the bingo card with 0
    df.iloc[:, 0:5] = np.where(df.iloc[:, 0:5]==num, 0, df.iloc[:, 0:5])
    
    # Keep count of number of marked numbers in a row
    df['amount-marked-row'] = (df.iloc[:, 0:5]==0).sum(axis=1)
    
    # Keep count of number of marked numbers in a col
    for i in range(0,len(df)-5+1,5):
        df.iloc[i:i+5,5]= (df.iloc[i:i+5, 0:5]==0).sum(axis=0).values
        
    # Check for Bingo (full column or row)
    bingo = df[(df['amount-marked-row'] == 5) | (df['amount-marked-col'] == 5)]
    
    # If bingo found
    if len(bingo) > 0:
        
        # If only 1 board left when bingo found, calculate and print score
        if len(df) == 5:
            print("final score: ",df, bingo)
            df = df.iloc[:,0:5].apply(pd.to_numeric)
            sum = df.values.sum()
            score = sum * int(num)
            print('ANTI-BINGO! Sum of unmarked: ', sum, ', Score: ', score)
            break
        
        # Else (multiple boards are still left). get rid of boards that have bingo
        else:
            # Retrieve indexes of bingo in column or row 
            bingo_indexes = list(bingo.index)
            
            # Make all indexes refer to only starting row of bingo board
            bingo_indexes = [5*math.floor((x-1)/5)+1 for x in bingo_indexes]    

            # Remove duplicate incase of situation where both a row and a column bingo is made
            bingo_indexes = list(dict.fromkeys(bingo_indexes))  

            # Loop through starting row indexes and drop the corresponding board
            for index in bingo_indexes:
                bingo_df = df.loc[index:index+4,0:4]
                df = df.drop(list(range(index,index+5)))                
