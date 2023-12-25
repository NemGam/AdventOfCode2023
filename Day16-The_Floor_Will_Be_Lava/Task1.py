from collections import deque

COLUMN_COUNT = 112
ROW_COUNT = 112

class Ray:
    def __init__(self, dir, pos):
        self.dir = dir
        self.pos = pos

    def move(self):
        self.pos = (self.pos[0] + self.dir[0], self.pos[1] + self.dir[1])

#dir - direction (y, x)
def get_direction(dir : tuple, symbol : str) -> list:
    if symbol == '.':
        return [dir]
    
    if symbol == "\\":
        if dir == (0, 1): return [(1, 0)]
        if dir == (1, 0): return [(0, 1)]      
        if dir == (0, -1): return [(-1, 0)]
        if dir == (-1, 0): return [(0, -1)]
    
    if symbol == '/':
        if dir == (0, 1): return [(-1, 0)]
        if dir == (1, 0): return [(0, -1)]      
        if dir == (0, -1): return [(1, 0)]
        if dir == (-1, 0): return [(0, 1)]

    if symbol == '|':
        if dir == (-1, 0) or dir == (1, 0):
            return [dir]
        else:
            return [(1, 0), (-1, 0)]
    
    if symbol == '-':
        if dir == (0, -1) or dir == (0, 1):
            return [dir]
        else:
            return [(0, 1), (0, -1)]
    
    if symbol == '#':
        return [(0, 0)]

grid = []
grid.append(list('#' * COLUMN_COUNT))
with open("./input.txt") as f:
    s = f.read().strip().splitlines()
    for line in s:
        grid.append(list(f"#{line}#"))
grid.append(list('#' * COLUMN_COUNT))

rays = deque()
current_ray = Ray((0, 1), (1, 0))
visited = [[0 for x in range(COLUMN_COUNT)] for i in range(ROW_COUNT)]

while True:
    current_ray.move()
    symbol = grid[current_ray.pos[0]][current_ray.pos[1]]
    #If ray hits the wall or the splitter already been used, we can just disregard the ray
    if symbol == '#' or ((symbol == '|' or symbol == '-') and visited[current_ray.pos[0]][current_ray.pos[1]] == 1):       
        if len(rays) == 0:
            break
        current_ray = rays.popleft()
        continue

    new_dir = get_direction(current_ray.dir, symbol)

    visited[current_ray.pos[0]][current_ray.pos[1]] = 1
    current_ray.dir = new_dir[0]
    if len(new_dir) == 2:
        rays.append(Ray(new_dir[1], current_ray.pos))

print(sum([sum(s) for s in visited]))
