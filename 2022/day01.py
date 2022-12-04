import os

# Read in Data
cwd = os.path.dirname(os.path.abspath(__file__))
f = open(cwd+'/day1.txt', 'r')
content = f.read()
f.close()

# Split out number groups by 2 line carriages - split each group into list and sum groups
content = content.split('\n'+'\n')
content = [x.split('\n') for x in content]
content = [sum([int(x) for x in group]) for group in content]

# Solution - max sum and sum of 3 highest sums
print(max(content))
print(sum(sorted(content)[-3:]))