import re

scheme : list[str] = []
COLUMNS = 140
ROWS = 140

def parseNumber(numberPos):
    y = numberPos[0]
    x = numberPos[1]
    while scheme[y][x - 1].isdigit():
        x -= 1
    
    num = ""
    while scheme[y][x].isdigit():
        num += scheme[y][x]
        x += 1
    return int(num)


def evaluateGears(pos : str) -> int:
    nums = []

    #Checking the top line. 
    # If the top symbol is digit, then there is only one number in the top row.
    if scheme[pos[0] - 1][pos[1]].isdigit():
        nums.append(parseNumber([pos[0] - 1, pos[1]]))
    else:
        if scheme[pos[0] - 1][pos[1] - 1].isdigit():
            nums.append(parseNumber([pos[0] - 1, pos[1] - 1]))
        if scheme[pos[0] - 1][pos[1] + 1].isdigit():
            nums.append(parseNumber([pos[0] - 1, pos[1] + 1]))
                   
    #Checking middle line
    if scheme[pos[0]][pos[1] - 1].isdigit():
        nums.append(parseNumber([pos[0], pos[1] - 1]))
        
    if scheme[pos[0]][pos[1] + 1].isdigit():
        nums.append(parseNumber([pos[0], pos[1] + 1]))


    #Checking the bottom line. 
    # If the bottom symbol is digit, then there is only one number in the bottom row.
    if scheme[pos[0] + 1][pos[1]].isdigit():
        nums.append(parseNumber([pos[0] + 1, pos[1]]))
    else:
        if scheme[pos[0] + 1][pos[1] - 1].isdigit():
            nums.append(parseNumber([pos[0] + 1, pos[1] - 1]))
        if scheme[pos[0] + 1][pos[1] + 1].isdigit():
            nums.append(parseNumber([pos[0] + 1, pos[1] + 1]))
            
    if len(nums) == 2:
        return nums[0] * nums[1]

    return 0

def getGearRatio(line : str, lineNum):
    s = re.findall("(\*)", line)
    res = 0
    start = 0
    for _ in s:
        res += evaluateGears([lineNum, line.index('*', start)])
        start = line.index('*', start) + 1
    
    return res

f = open("./input.txt")

res = 0
scheme.append('.' * COLUMNS)
for line in f:
    scheme.append('.' + line.strip() + '.')
scheme.append('.' * COLUMNS)

f.close()
for i in range(len(scheme)):  
    res += getGearRatio(scheme[i], i)

print(f"res:{res}")