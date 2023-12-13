
with open("./input.txt") as f:
    time = int("".join(f.readline()[6:]).replace(' ', ''))
    distance = int("".join(f.readline()[11:]).replace(' ', ''))
    res = 0
    for i in range(time):
        if (time - i) * i > distance:
            res += 1
    print(res)
