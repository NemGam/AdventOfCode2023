import re

scheme = []
COLUMNS = 140
ROWS = 140
def evaluateNumber(number : str, pos) -> int:
    res = int(number)

    #Checking top line
    if pos[0] > 0:
        
        if pos[1] > 0:
            if scheme[pos[0] - 1][pos[1] - 1] != '.':
                return res
        
        for i in range(len(number)):
            if scheme[pos[0]-1][pos[1] + i] != '.':
                return res
        
        if pos[1] + len(number) < COLUMNS:
            if scheme[pos[0] - 1][pos[1] + len(number)] != '.':
                return res
            
    #Checking middle line

    if pos[1] > 0:
        if scheme[pos[0]][pos[1] - 1] != '.':
            return res
        
    if pos[1] + len(number) < COLUMNS:
        if scheme[pos[0]][pos[1] + len(number)] != '.':
            return res

    #Checking bottom line
    if pos[0] + 1 < ROWS:
        
        if pos[1] > 0:
            if scheme[pos[0] + 1][pos[1] - 1] != '.':
                return res
        
        for i in range(len(number)):
            if scheme[pos[0] + 1][pos[1] + i] != '.':
                return res
        
        if pos[1] + len(number) < COLUMNS:
            if scheme[pos[0] + 1][pos[1] + len(number)] != '.':
                return res
    return 0

def getPartsNumbers(line : str, lineNum):
    s = re.findall("([0-9]+)", line)
    res = 0
    start = 0
    for num in s:
        res += evaluateNumber(num, [lineNum, line.index(num, start)])
        start = line.index(num, start) + len(num)
    
    return res

f = open("./input.txt")

res = 0
for line in f:
    scheme.append(line.strip())
f.close()
for i in range(len(scheme)):  
    res += getPartsNumbers(scheme[i], i)

print(f"res:{res}")