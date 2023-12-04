import re

f = open("./input.txt")
res = 0
for line in f:
    s = "".join(re.findall("[0-9]", line))
    res += int(s[0] + s[-1])
print(f"res: {res}")
f.close()