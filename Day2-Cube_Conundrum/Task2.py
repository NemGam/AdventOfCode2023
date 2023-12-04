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
    red = 0
    green = 0
    blue = 0
    while start != -1:
        current = line.find(';', start + 1)
        s = re.sub("[,;]", "", line[start : current]).split()
        for i in range(0, len(s), 2):
            v = int(s[i])
            if s[i+1] == "red":
                red = max(red, v)
            elif s[i+1] == "green":
                green = max(green, v)
            else:
                blue = max(blue, v)
        start = line.find(';', current)
    res += red * green * blue
              
print(f"res: {res}")
f.close()