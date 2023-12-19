import re
COLUMN_COUNT = 140

grid : list[list[str]]= []
emptyColumns = set()


#Read file
with open("./input.txt") as f:
    allColumns = set([x for x in range(COLUMN_COUNT)])
    nonEmptyColumns = set()

    for line in f:
        line = line.strip()
        z = [int(m.start(0)) for m in re.finditer("#", line)]
        if len(z) > 0:
            for val in z:
                nonEmptyColumns.add(val)
        else:
            #Double the empty rows
            grid.append(list(line))
        grid.append(list(line))
    
    emptyColumns = allColumns.difference(nonEmptyColumns)

#Double the empty columns
emptyColumns = sorted(emptyColumns, reverse=True)
for col in emptyColumns:
    for row in grid:
        row.insert(col, '.')

galaxies = []
#Get new coordinates of the galaxies
for i in range(len(grid)):
    z = [e for e, x in enumerate(grid[i]) if x == '#']
    if len(z) > 0:
            for val in z:
                galaxies.append((i, val))

res = 0
#Calculate all the distances
for i in range(len(galaxies) - 1):
    for j in range(i + 1, len(galaxies)):
        res += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])

print(res)