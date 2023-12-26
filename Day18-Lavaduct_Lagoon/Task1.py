def get_direction_from_symbol(symbol : str) -> tuple:
    if symbol == 'L': return (0, -1)
    if symbol == 'U': return (-1, 0)
    if symbol == 'R': return (0, 1)
    if symbol == 'D': return (1, 0)
    
directions = []
with open("./input.txt") as f:
    for line in f:
        directions.extend([line.split()])
    
points = []
curr_pos = (0, 0)
points.append(curr_pos)
for direction, length, _ in directions:
    curr_dir = get_direction_from_symbol(direction)
    for i in range(int(length)):
        curr_pos = (curr_pos[0] + curr_dir[0], curr_pos[1] + curr_dir[1])
        points.append(curr_pos)


#Calculate inside area with Shoelace formula
#Learn more: https://en.wikipedia.org/wiki/Shoelace_formula
area = 0
#points.append((0, 0))
for i in range(0, len(points) - 1):
    area += points[i][0] * (points[i+1][1] - points[i-1][1])
area = abs(area / 2)

#Use Pick's theorem to calculate the number of points inside the loop
#Learn more: https://en.wikipedia.org/wiki/Pick%27s_theorem
res = area + len(points) // 2 + 1
print(res)
