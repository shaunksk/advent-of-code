import os
import sys

if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, the PyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app 
    # path into variable _MEIPASS'.
    cwd = sys._MEIPASS
else:
    cwd = os.path.dirname(os.path.abspath(__file__))


f = open(cwd+'/day1.txt', 'r')
content = f.read()
f.close()

content = content.split('\n'+'\n')
content = [x.split('\n') for x in content]
content = [sum([int(x) for x in group]) for group in content]

print(max(content))
print(sum(sorted(content)[-3:]))