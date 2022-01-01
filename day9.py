import pandas as pd
import numpy as np

df = pd.read_csv("day9-input.txt",delimiter="/n",dtype=str,header = None, names=['input'],engine='python')   # convert input into dataframe
df= df['input'].str.split("",expand=True,).apply(pd.to_numeric)                    # delimit data based on ""
df = df.drop([0],axis=1)
df = df.drop([101],axis=1)
print(df)

# Part 1 - find the low points - the locations that are lower than any of its adjacent locations from the grid of provided numbers

list = []
# Loop through all rows and columns of number grid
for index, row in df.iterrows():
    # print("index",index)
    for i in range(1,len(row)+1,1):
        
        # Assign variables to the adjacent cells. If no adjecent cell found (e.g. edge cells) then assign adjacent cell to be grater than original cell  
        # right_cell = row[i+1]
        try:            right_cell = row[i+1]
        except KeyError:right_cell = row[i] + 1
        try:            left_cell = row[i-1]
        except KeyError:left_cell = row[i] + 1
        try:            up_cell = df.loc[index-1,i]
        except KeyError:up_cell = row[i] + 1
        try:            down_cell = df.loc[index+1,i]
        except KeyError:down_cell = row[i] + 1

        # if all adjacent cells are bigger, then append number to list as it is a low point (basin)     
        if row[i] < right_cell and row[i] < left_cell and row[i] < up_cell and row[i] < down_cell:
            list.append([row[i],i,index])

# Calculate risk level - 1sum of 1 above height of low points
new_list = [x[0] for x in list]
new_list = [x+1 for x in new_list] 
print(sum(new_list))

# Part 2 - find the 3 largest basins - size of basin = no. of locations that eventually flow downward to the low point (excluding number 9)

# Loop through all basins in list to find location size of each
basin_sizes = []
for basin in list:

    # Recursive function to find all adjacent locatons of adjacent locations etc. for a given basin (low point)
    # For Each adjacent cell/location, if the cell value is higher, not 9 and not a location already found, 
    # then increase location size by 1, track the cell location to prevent double counting and call the function again to be applied on all the new cells adjacent cells
    def find_location(i, index, df, location_size,location_log=[]):
        print("x:",i,"index:",index)
        try:    
            if df.loc[index,i] < df.loc[index,i+1] and df.loc[index,i+1] != 9 and (i+1,index) not in location_log:
                location_size += 1
                location_log.append((i+1,index))
                print("location size (right cell)",location_size,"value",df.loc[index,i+1])
                location_size, location_log = find_location(i+1,index,df,location_size,location_log)
            else: print("none found on the right of ", "x:",i,"index:",index )
        except KeyError: print("none found on the right of ", "x:",i,"index:",index )
        try:
            if df.loc[index,i] < df.loc[index,i-1] and df.loc[index,i-1] != 9 and (i-1,index) not in location_log:
                location_size += 1
                location_log.append((i-1,index))
                print("location size (left cell)",location_size,"value",df.loc[index,i-1])
                location_size, location_log  = find_location(i-1,index,df,location_size)
            else: print("none found on the left of ", "x:",i,"index:",index ) 
        except KeyError: print("none found on the left of ", "x:",i,"index:",index )
        try:
            if df.loc[index,i] < df.loc[index-1,i] and df.loc[index-1,i] != 9 and (i,index-1) not in location_log:
                location_size += 1
                location_log.append((i,index-1))
                print("location size (above cell)",location_size,"value",df.loc[index-1,i])
                location_size, location_log  = find_location(i,index-1,df,location_size)
            else: print("none found above of ", "x:",i,"index:",index ) 
        except KeyError: print("none found above of ", "x:",i,"index:",index )
        try:
            if df.loc[index,i] < df.loc[index+1,i] and df.loc[index+1,i] != 9 and (i,index+1) not in location_log:
                location_size += 1
                location_log.append((i,index+1))
                print("location size (below cell)",location_size,"value",df.loc[index+1,i])
                location_size, location_log  = find_location(i,index+1,df,location_size)
            else: print("none found below of ", "x:",i,"index:",index ) 
        except KeyError: print("none found below of ", "x:",i,"index:",index )
        
        return location_size, location_log 

    i = basin[1]
    index = basin[2]

    # Append location size for each basin
    loc_size, loc_log = find_location(i, index, df,1) 
    basin_sizes.append(loc_size)

# Find 3 largest basins
largest_basins = sorted(basin_sizes,reverse=True)[0:3]
print(largest_basins)

# Multiply top 3 largest basins to get the answer
answer = np.prod(largest_basins)
print(answer)


