import os

f = open(os.path.dirname(os.path.abspath(__file__)) + '/day01.txt', 'r')
content = f.read()
print(content)
f.close()

content = [int(x) for x in content.split('\n')]
print(content)

# Part 1
for num in content:
    if (2020-num) in content:
        print(num*(2020-num))
        break
# Part 2

content = sorted(content)
for x in range(len(content)):
    value = 2020-content[x]
    for y in content[x:]:
        if (value-y) in content[x:]:
            print(content[x],y,(value-y))
            
            print(content[x]*y*(value-y))
            
            break
