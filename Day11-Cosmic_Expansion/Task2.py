import re
from collections import deque
COLUMN_COUNT = 140
EXPANSION_MODIFIER = 1000000

grid : list[list[str]]= []
emptyColumns = deque()
emptyRows = deque()
#Read file
with open("./input.txt") as f:
    allColumns = set([x for x in range(COLUMN_COUNT)])
    nonEmptyColumns = set()
    i = 0
    for line in f:
        line = line.strip()
        z = [int(m.start(0)) for m in re.finditer("#", line)]
        if len(z) > 0:
            for val in z:
                nonEmptyColumns.add(val)
        else:
            emptyRows.append(i)
        grid.append(line)
        i += 1

    #Get the empty columns
    emptyColumns = deque(sorted(allColumns.difference(nonEmptyColumns)))

galaxies = []
#Get the coordinates of the galaxies
passedEmptyRows = 0
for i in range(len(grid)):
    if len(emptyRows) > 0 and i == emptyRows[0]:
        passedEmptyRows += 1
        emptyRows.popleft()
        continue
    emptCols = emptyColumns.copy() #Temp object to not modify the initial queue
    passedEmptyColumns = 0
    for j in range(len(grid[i])):
        if len(emptCols) > 0 and j == emptCols[0]:
            passedEmptyColumns += 1
            emptCols.popleft()
            continue
        if grid[i][j] == '#':
            galaxies.append((i + passedEmptyRows * (EXPANSION_MODIFIER - 1), j + passedEmptyColumns * (EXPANSION_MODIFIER - 1)))
res = 0

#Calculate all the distances
for i in range(len(galaxies) - 1):
    for j in range(i + 1, len(galaxies)):
        res += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])

print(res)