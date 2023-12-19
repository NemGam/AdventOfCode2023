def get_direction_from_symbol(symbol : str, dir):
    if symbol == '|' or symbol == '-':
        return dir
        
    elif symbol == 'L':
        if dir == (0, 1):
            return (1, 0)
        else: #if (-1, 0)
            return (0, -1)
    
    elif symbol == 'J':
        if dir == (0, 1):
            return (-1, 0)
        else: #if (1, 0)
            return (0, -1)
        
    elif symbol == '7':
        if dir == (0, -1):
            return (-1, 0)
        else: #if (1, 0)
            return (0, 1)

    elif symbol == 'F':
        if dir == (-1, 0):
            return (0, 1)
        else: #if (0, -1)
            return (1, 0)
    
def get_start_direction(start, grid):
    if grid[start[1] - 1][start[0]] == '|' or grid[start[1] - 1][start[0]] == '7' or grid[start[1] - 1] [start[0]] == 'F':
        return (0, -1)
    elif grid[start[1]][start[0] + 1] == '-' or grid[start[1]][start[0] + 1] == '7' or grid[start[1]][start[0] + 1] == 'J':
        return (1, 0)
    elif grid[start[1] + 1][start[0]] == '|' or grid[start[1] + 1] [start[0]] == 'J' or grid[start[1] + 1][start[0]] == 'L':
        return (0, 1)
    elif grid[start[1]][start[0] - 1] == '-' or grid[start[1]] [start[0] - 1] == 'L' or grid[start[1]][start[0] - 1] == 'F':
        return (-1, 0)

f = open("./input.txt")

grid = [list(line.strip()) for line in f.readlines()] #(y, x)
f.close()
start = ()
#Find coordinates of the Start
for i in range(len(grid)):
    j = 0
    try:
        j = grid[i].index('S')      
    except ValueError:
        continue
    start = (j, i)
    break


currPos = start  #(x, y)
steps = 0
currDir = get_start_direction(start, grid)
while True:
    #Move
    currPos = (currPos[0] + currDir[0], currPos[1] + currDir[1]) #(x, y)
    if grid[currPos[1]][currPos[0]] == 'S':
        break
    steps += 1
    currDir = get_direction_from_symbol(grid[currPos[1]][currPos[0]], currDir)
#Furthest point is the half of the whole loop
print(steps // 2 + 1)
