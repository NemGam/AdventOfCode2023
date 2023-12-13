import math

with open("./input.txt") as f:
    time = int("".join(f.readline()[6:]).replace(' ', ''))
    distance = int("".join(f.readline()[11:]).replace(' ', ''))

    start = (time - math.sqrt((time**2 - distance * 4))) / 2
    end = int(start + 1)
    print(time - 2*end + 1)