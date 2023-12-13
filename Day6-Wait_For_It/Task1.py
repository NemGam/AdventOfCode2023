
res = 1
with open("./input.txt") as f:
    times = [int(x) for x in f.readline()[6:].split()]
    distances = [int(x) for x in f.readline()[11:].split()]
    for time, distance in zip(times, distances):
        subres = 0
        for i in range(time):
            if (time - i) * i > distance:
                subres += 1
        res *= subres
print(res)
