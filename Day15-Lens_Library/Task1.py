
def HASH(string : str) -> int:
    current_value = 0
    for char in string:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value

res = 0
with open("./input.txt") as f:
    for line in f:
        s = ""
        for char in line:
            if char != ',':
                s += char
            else:
                res += HASH(s)
                s = ""
    
    #For the last one
    res += HASH(s)

print(res)