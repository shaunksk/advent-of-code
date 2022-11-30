"""
--- Day 3: Binary Diagnostic ---
The submarine has been making some odd creaking noises, so you ask it to produce a diagnostic report just in case.

The diagnostic report (your puzzle input) consists of a list of binary numbers which, when decoded properly, 
can tell you many useful things about the conditions of the submarine. 
The first parameter to check is the power consumption.

You need to use the binary numbers in the diagnostic report to generate 
two new binary numbers (called the gamma rate and the epsilon rate). 
The power consumption can then be found by multiplying the gamma rate by the epsilon rate.

Each bit in the gamma rate can be determined by finding the most common bit 
in the corresponding position of all numbers in the diagnostic report. 
For example, given the following diagnostic report:

00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
Considering only the first bit of each number, there are five 0 bits and seven 1 bits. 
Since the most common bit is 1, the first bit of the gamma rate is 1.

The most common second bit of the numbers in the diagnostic report is 0, so the second 
bit of the gamma rate is 0.

The most common value of the third, fourth, and fifth bits are 1, 1, and 0, respectively, 
and so the final three bits of the gamma rate are 110.

So, the gamma rate is the binary number 10110, or 22 in decimal.

The epsilon rate is calculated in a similar way; rather than use the most common bit, 
the least common bit from each position is used. So, the epsilon rate is 01001, or 9 in decimal. 
Multiplying the gamma rate (22) by the epsilon rate (9) produces the power consumption, 198.

Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, 
then multiply them together. What is the power consumption of the submarine? 
(Be sure to represent your answer in decimal, not binary.)

To begin, get 
"""
import pandas as pd

my_file = open("day3-input.txt","r")
content = my_file.read()
content_list = content.split("\n")
my_file.close()

# Data Prep


# Part 1 - loop method
"""
sum = [0] * 12

for num in content_list:
    for char_position in range(len(num)):
        sum[char_position] += int(num[char_position])

most_common_digit = []
for x in sum:
    if x < len(content_list)/2:     most_common_digit.append(0)
    elif x > len(content_list)/2:   most_common_digit.append(1)
    else:                           most_common_digit.append("equal")

most_common_digit = [str(x) for x in most_common_digit]

gamma_rate_bin = ''.join(most_common_digit)
gamma_rate = int(gamma_rate_bin, 2)
epsilon_rate_bin = ''.join('1' if x == '0' else '0' for x in gamma_rate_bin)
epsilon_rate = int(epsilon_rate_bin, 2)

print("gamma rate: ",gamma_rate)
print("epsilon rate: " ,epsilon_rate)
print("power consumption: ", epsilon_rate*gamma_rate)
"""

# Part 1 - Data Frame method

# content_list = [x.split(" ") for x in content_list]

df = pd.read_csv("day3-input.txt",delimiter="\n",dtype=str,header = None,names=["binum"])   # convert inout into dataframe
df= df['binum'].str.split('',expand=True)                                                   # split digits into seperate columns
df = df.apply(pd.to_numeric)        
df = df.drop(columns = [13, 0])     #drop unnessessary NaN columns

most_common_digit = []
for col in df:
    sum = df[col].sum()
    if sum < len(df.index)/2:     most_common_digit.append(str(0))  # 0 is most common if sum is less than half of number of entries
    elif sum > len(df.index)/2:   most_common_digit.append(str(1))  # 1 is most common if sum is more than half of number of entries
    else:                         most_common_digit.append("equal") # equal number of both

# most_common_digit = [str(x) for x in most_common_digit]

gamma_rate_bin = ''.join(most_common_digit)
gamma_rate = int(gamma_rate_bin, 2)
epsilon_rate_bin = ''.join('1' if x == '0' else '0' for x in gamma_rate_bin)
epsilon_rate = int(epsilon_rate_bin, 2)

print("gamma rate: ",gamma_rate)
print("epsilon rate: " ,epsilon_rate)
print("power consumption: ", epsilon_rate*gamma_rate)


# Part 2 - using dataframe method

# oxygen generator rating
df_o2 = df
for col in df_o2:
    sum = df_o2[col].sum()
    if sum < len(df_o2.index)/2:    df_o2 = df_o2.loc[df_o2[col] == 0]  # 0 is most common so filter for only 0 values 
    elif sum > len(df_o2.index)/2:  df_o2 = df_o2.loc[df_o2[col] == 1]  # 1 is most common so filter for only 1 values 
    else:                           df_o2 = df_o2.loc[df_o2[col] == 1]  # equal amounts so filter for only 1 values 

    if len(df_o2) == 1:
        break

#CO2 scrubber rating
df_co2 = df
for col in df_co2:
    sum = df_co2[col].sum()
    if sum < len(df_co2.index)/2:   df_co2 = df_co2.loc[df_co2[col] == 1]  # 0 is least common so filter for only 1 values 
    elif sum > len(df_co2.index)/2: df_co2 = df_co2.loc[df_co2[col] == 0]  # 1 is least common so filter for only 0 values 
    else:                           df_co2 = df_co2.loc[df_co2[col] == 0]  # equal amounts so filter for only 0 values 

    if len(df_co2) == 1:
        break

o2_bin = ''.join(str(df_o2[col].values[0]) for col in df_o2)
co2_bin = ''.join(str(df_co2[col].values[0]) for col in df_co2)
co2 = int(co2_bin, 2)
o2 = int(o2_bin, 2)

print("Oxygen generator rating: ",o2)
print("CO2 scrubber rating: " , o2)
print(co2 * o2)