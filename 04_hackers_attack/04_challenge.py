from input_04 import txt

for index, value in enumerate(txt.split('\n')):
    line = value.split('-')
    if index == 32:
        print(line[1])