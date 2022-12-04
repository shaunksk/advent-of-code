import os 
f = open(os.path.dirname(os.path.abspath(__file__)) + '/day05.txt', 'r')
content = f.read()
print(content)
f.close()
