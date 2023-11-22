from input_02 import txt

result = 0
for letter in txt:
    match letter:
        case "#":
            result += 1
        case "@":
            result -= 1
        case "*":
            result *= result
        case "&":
            print(result, end='')