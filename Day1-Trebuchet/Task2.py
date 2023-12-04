import re

dict = {
    "1" : "1",
    "2" : "2",
    "3" : "3",
    "4" : "4",
    "5" : "5",
    "6" : "6",
    "7" : "7",
    "8" : "8",
    "9" : "9",
    "one" : "1",
    "two" : "2",
    "three" : "3",
    "four" : "4",
    "five" : "5",
    "six" : "6",
    "seven" : "7",
    "eight" : "8",
    "nine" : "9"
}

f = open("./input.txt")
res = 0
i = 0
for line in f:
    i += 1
    print(line[:-1], end=", ")
    s = re.findall("(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))", line)
    s[0] = dict[s[0]]
    ss = s[0]
    if (len(s) != 1):
        s[-1] = dict[s[-1]]
        ss += s[-1]
    else:
        ss += ss
    print(int(ss))
    res += int(ss)
print(f"res: {res}")
f.close()