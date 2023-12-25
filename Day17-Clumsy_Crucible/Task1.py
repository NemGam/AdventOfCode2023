from heapq import heappop, heappush

ROW_COUNT = 142
COLUMN_COUNT = 142
 
#Check if the directions are opposite
def is_opposite(a : int, b : int):
    #(left, right) or (right, left) or (up, down) or (down, up)
    return abs(a - b) == 2
 
directions = [(0, -1), (-1, 0), (0, 1), (1, 0)] #l, u, r, d  
grid = []
grid.append([-1] * COLUMN_COUNT)
#Fill the grid
with open("./input.txt") as f:
    s = f.read().strip().splitlines()
    for line in s:
        l = [-1]
        l.extend([int(x) for x in line])
        l.append(-1)
        grid.append(l)
grid.append([-1] * COLUMN_COUNT)

heap = [(0, (1, 1), (2, 0))]  # (heat, (x, y), (current_direction, steps)
visited : dict = {((1, 1), (2, 0)): 0}

while heap:
    heat, (x, y), (current_direction, current_steps) = heappop(heap)
    #Check all directions
    for direction, change in enumerate(directions):
        w = grid[x + change[0]][y + change[1]]

        if w != -1:
            if (direction == current_direction and current_steps == 3) or is_opposite(direction, current_direction):
                #Skip the direction check if steps are bigger than 3
                continue
            #Check if current direction is the same as the one being checked
            if direction == current_direction:
                new_steps = current_steps + 1
            else:
                new_steps = 1
            
            if ((x + change[0], y + change[1]), (direction, new_steps)) in visited:
                current_heat = visited[((x + change[0], y + change[1]), (direction, new_steps))]
            else:
                current_heat = float('inf')

            if heat + w < current_heat:
                if direction == current_direction:
                    new_steps = current_steps + 1
                else:
                    new_steps = 1

                visited[(x + change[0], y + change[1]), (direction, new_steps)] = heat + w
                heappush(heap, (heat + w, (x + change[0], y + change[1]), (direction, new_steps)))

#Looking for the paths that ended in the bottom right corner
path_ends = [heat for ((x, y), _), heat in visited.items() if x == ROW_COUNT - 1 and y == COLUMN_COUNT - 1]
print(min(path_ends))
