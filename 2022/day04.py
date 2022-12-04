import os

f = open(os.path.dirname(os.path.abspath(__file__)) + '/day04.txt', 'r')
content = f.read()
f.close()

part1=0
part2=0

for pair in content.split('\n'):
    if pair == '': break

    # Split numbers into readable format
    sections = [[int(y) for y in x.split('-')] for x in pair.split(',')]

    # Examples - Part 1 - Sections contain one another
    # sections = [[1,5],[2,3]]
    # sections = [[2,3],[1,5]]
    if (sections[0][0] <= sections[1][0] and sections[0][1] >= sections[1][1]) or \
       (sections[0][0] >= sections[1][0] and sections[0][1] <= sections[1][1]):
        part1+=1

    # Examples - Part 2 - Sections overlap
    # sections = [[1,3],[2,5]]
    # sections = [[2,5],[1,3]]
    if sections[0][1] >= sections[1][0] and sections[0][0] <= sections[1][1]:
        part2+=1


print(part1)
print(part2)