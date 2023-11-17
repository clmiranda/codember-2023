string = "&###@&*&###@@##@##&######@@#####@#@#@#@##@@@@@@@@@@@@@@@*&&@@@@@@@@@####@@@@@@@@@#########&#&##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@&"
result = 0
for letter in string:
    match letter:
        case "#":
            result += 1
        case "@":
            result -= 1
        case "*":
            result *= result
        case "&":
            print(result, end='')