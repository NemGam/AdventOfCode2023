from collections import deque
COLUMN_COUNT = 132
ROW_COUNT = 132
STEP_COUNT = 64

def get_neighbours(pos : tuple[int, int]) -> list:
    return [(pos[0], pos[1] - 1), (pos[0] - 1, pos[1]), (pos[0], pos[1] + 1), (pos[0] + 1, pos[1])]

def bfs(grid : list[list[str]], visited : list[int], start : tuple[int, int]):
    queue : deque[tuple[int, int]] = deque()
    queue.append(start)
    visited[start[0]][start[1]] = 0

    while len(queue) > 0:
        node = queue.popleft()
        if grid[node[0]][node[1]] == '#':
            continue

        curr_steps = visited[node[0]][node[1]]
        if curr_steps >= STEP_COUNT:
            continue
        neighbours = get_neighbours(node)
        for neighbour in neighbours:
            #print(neighbour)
            if grid[neighbour[0]][neighbour[1]] == '#':
                continue
            if curr_steps + 1 >= visited[neighbour[0]][neighbour[1]]:
                continue
            
            visited[neighbour[0]][neighbour[1]] = curr_steps + 1
            queue.append(neighbour)

    #print(visited)


visited = [[10001 for i in range(COLUMN_COUNT)] for j in range(ROW_COUNT)]

grid = []
grid.append('#' * COLUMN_COUNT)
with open("./input.txt") as f:
    s = f.read().strip().splitlines()
    for line in s:
        grid.append(f"#{line}#")
grid.append('#' * COLUMN_COUNT)

for y, line in enumerate(grid):
    if line.find('S') != -1:
        start = (y, line.find('S'))

bfs(grid, visited, start)

print(sum([sum([1 if x % 2 == 0 else 0 for x in i]) for i in visited]))
#44 - not right