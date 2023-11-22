from input_03 import txt

counter = 1
for i in txt.split('\n'):
    line = i.split()
    n_range = line[0].split('-')
    letter = line[-1].count(line[1][0])
    if int(n_range[1]) < letter or letter < int(n_range[0]):
        if counter == 42:
            print(line[-1])
            break
        counter += 1