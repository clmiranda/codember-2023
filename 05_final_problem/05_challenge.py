from input_05 import txt
import re

lst = []
patt = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
for i in txt.split('\n'):
    line = i.split(',')
    if line[0] and line[1] and line[2] and line[0].isalnum() and line[1].isalnum() and re.match(patt, line[2]):
        if line[-2] == "" or line[-2] and line[-2].isdigit():
            print(True)
        else:
            print(False)
            lst.append(line[1][0])
    else:
        print(False)
        lst.append(line[1][0])
        
print(''.join(lst))