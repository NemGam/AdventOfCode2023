import numpy as np
import copy
ROW_COUNT = 102
COLUMN_COUNT = 102
ITERATION_COUNT = 1000000000

class Rock:
    #Pass coords as (x, y)
    def __init__(self, coords):
        self.x : int = coords[0]
        self.y : int = coords[1]

    def __str__(self):
        return f"{self.x};{self.y}"

    def __repr__(self):
        return str(self)
    
    #Pass as (x, y)
    def move(self, x_dir, y_dir):
        self.x += x_dir
        self.y += y_dir

def slide_rocks(active_rocks : list):
    while len(active_rocks) > 0:
        rocks_to_deactivate = []
        for i in range(len(active_rocks)):
            rock = active_rocks[i]
            if grid[rock.y + gravity[0]][rock.x + gravity[1]] == '#':
                rocks_to_deactivate.append(i)     
            elif grid[rock.y + gravity[0]][rock.x + gravity[1]] == 'O':
                z = 1
                #Check if all the next rocks are stuck. If so, I'm also stuck
                while True:
                    c = grid[rock.y + gravity[0] * z][rock.x + gravity[1] * z]
                    if c == '#':
                        rocks_to_deactivate.append(i)
                        break
                    elif c == '.':
                        break
                    z += 1
            else:
                #Update rock's position on the grid
                grid[rock.y][rock.x] = '.'
                rock.move(gravity[1], gravity[0])
                grid[rock.y][rock.x] = 'O'
            
        #Deactivate rocks that will not move anymore
        for i in range(len(rocks_to_deactivate) - 1, -1, -1):
            active_rocks.pop(rocks_to_deactivate[i])


grid = []
grid.append(list('#' * COLUMN_COUNT))
with open("./input.txt") as f:
    s = f.read().strip().splitlines()
    for line in s:
        grid.append(list(f"#{line}#"))
grid.append(list('#' * COLUMN_COUNT))

#Find all the rocks
round_rocks : list[Rock] = []
for count, line in enumerate(grid):
    rocks = [[x[0], count] for x in enumerate(line) if x[1] == 'O']
    for rock in rocks:
        #y, x
        round_rocks.append(Rock(rock))

seen_dict = {}
ordered_states = []
loop_size = 0
gravity = (-1, 0) #y,x
final_state = ""

#Drop all the rocks
for _ in range(ITERATION_COUNT):
    state = "".join(repr(grid))

    #Found the repetition
    if state in seen_dict:
        loop_size = _
        final_state = state
        break

    active_rocks = round_rocks.copy()
    
    slide_rocks(active_rocks)
    
    ordered_states.append(copy.deepcopy(grid))
    seen_dict[state] = _

    #Flip gravity 90 degrees clockwise
    gravity = (-gravity[1], gravity[0])

loop_start = seen_dict[final_state] + 1

grid = ordered_states[(ITERATION_COUNT) % (loop_size + 1 - loop_start) + loop_start]

res = 0
for count, line in enumerate(grid):
    res += sum(1 if a == 'O' else 0 for a in line) * (ROW_COUNT - count - 1)

print(res)