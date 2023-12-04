import re

RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14

def isPossible(num, color):
    if color == "red":
        return int(num) <= RED_MAX
    elif color == "green":
        return int(num) <= GREEN_MAX
    else:
        return int(num) <= BLUE_MAX

f = open("./input.txt")
res = 0
for line in f:
    start = line.find(':') + 1
    possible = True
    while start != -1:
        current = line.find(';', start + 1)
        s = re.sub("[,;]", "", line[start : current]).split()
        for i in range(0, len(s), 2):
            if not isPossible(s[i], s[i+1]):
                possible = False
                break

        if not possible:
            break
        start = line.find(';', current)
    
    if possible:
        res += int(line[:line.find(':')].split()[1])
              
print(f"res: {res}")
f.close()