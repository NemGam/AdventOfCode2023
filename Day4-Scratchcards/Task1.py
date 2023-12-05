f = open("./input.txt")

res = 0
for line in f:
    s = line.strip()
    w = s[s.index(':') + 1: s.index('|')]
    winningNums = {key: '0' for key in w.split()}
    nums = s[s.index('|') + 1:].split()
    count = 0
    for num in nums:
        if num in winningNums:
            count += 1
    if count == 0:
        continue
    else:
        res += 1 * (2 ** (count - 1))
f.close()

print(f"Result: {res}")