from input_01 import txt

lst, lst2 = [], []
for animal in txt.split():
    if animal in lst2:
        continue
    else:
        lst.append(f"{animal}{txt.count(animal)}")
        lst2.append(animal)
print("".join(lst))