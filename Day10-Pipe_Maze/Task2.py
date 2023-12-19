import time
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

#Enclose the region
currPos = start  #(x, y)
currDir = (0, -1)
points = []
while True:
    points.append(currPos)
    currPos = (currPos[0] + currDir[0], currPos[1] + currDir[1]) #(x, y)

    if grid[currPos[1]][currPos[0]] == 'S':
        break
    currDir = get_direction_from_symbol(grid[currPos[1]][currPos[0]], currDir)

#Calculate inside area with Shoelace formula
#Learn more: https://en.wikipedia.org/wiki/Shoelace_formula
area = 0
points.append(start)
for i in range(0, len(points) - 1):
    area += points[i][0] * (points[i+1][1] - points[i-1][1])
area = area / 2

#Use Pick's theorem to calculate the number of points inside the loop
#Learn more: https://en.wikipedia.org/wiki/Pick%27s_theorem
res = area - len(points) // 2 + 1

print(res)