ROW_COUNT = 100
COLUMN_COUNT = 100

grid = []
with open("./input.txt") as f:
    grid = [list(x) for x in f.read().strip().splitlines()]
grid.insert(0, list('#' * COLUMN_COUNT)) #Pretend that the first row is '#'

#Find all the rocks
round_rocks = []
for count, line in enumerate(grid):
    #y, x
    round_rocks.extend([[count, x[0]] for x in enumerate(line) if x[1] == 'O'])

res = 0
active_rocks = round_rocks.copy()
#Drop all the rocks
while len(active_rocks) > 0:
    rocks_to_deactivate = []
    for i in range(len(active_rocks)):
        rock = active_rocks[i]
        if grid[rock[0] - 1][rock[1]] == '#' or grid[rock[0] - 1][rock[1]] == 'O':
            res += ROW_COUNT - rock[0] + 1
            rocks_to_deactivate.append(i)      
        else:
            #Update rock's position on the grid
            grid[rock[0]][rock[1]] = '.'
            rock[0] -= 1
            grid[rock[0]][rock[1]] = 'O'
        
    #Deactivate rocks that will not move anymore
    for i in range(len(rocks_to_deactivate) - 1, -1, -1):
        active_rocks.pop(rocks_to_deactivate[i])


print(res)