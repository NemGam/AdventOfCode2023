from timeit import default_timer as timer
GRID_SIZE = 141

#Checks if the given point on the grid is an intersection
def is_intersection(grid, coords : tuple[int, int]) -> bool:
    if coords[0] == 0 or coords[1] == 0 or coords[0] == GRID_SIZE - 1 or coords[1] == GRID_SIZE - 1:
        return False
    l = [grid[coords[0] + 1][coords[1]], grid[coords[0] - 1][coords[1]], 
         grid[coords[0]][coords[1] + 1], grid[coords[0]][coords[1] - 1]]
    return sum(1 if x != '#' else 0 for x in l) > 2

#Returns possible start points from the given node coordinates
def get_routes(grid, coords : tuple[int, int], visited) -> list[tuple[int,int]]:
    res = []
    if (coords[0], coords[1] + 1) not in visited and grid[coords[0]][coords[1] + 1] == '.': res.append((coords[0], coords[1] + 1))
    if (coords[0], coords[1] - 1) not in visited and grid[coords[0]][coords[1] - 1] == '.': res.append((coords[0], coords[1] - 1))
    if (coords[0] - 1, coords[1]) not in visited and grid[coords[0] - 1][coords[1]] == '.': res.append((coords[0] - 1, coords[1]))
    if (coords[0] + 1, coords[1]) not in visited and grid[coords[0] + 1][coords[1]] == '.': res.append((coords[0] + 1, coords[1]))
    return res

#Returns direction for the given point on the grid
def get_direction(grid, visited, pos : tuple[int, int]) -> tuple[int, int]:
    if (pos[0], pos[1] + 1) not in visited and grid[pos[0]][pos[1] + 1] in ['.', '_']: return (0, 1)
    if (pos[0], pos[1] - 1) not in visited and grid[pos[0]][pos[1] - 1] in ['.', '_']: return (0, -1)
    if (pos[0] - 1, pos[1]) not in visited and grid[pos[0] - 1][pos[1]] in ['.', '_']: return (-1, 0)
    if (pos[0] + 1, pos[1]) not in visited and grid[pos[0] + 1][pos[1]] in ['.', '_']: return (1, 0)
    raise Exception(f"Wasn't able to find the direction at {pos}")

#Converts grid path between two nodes into adjacency list entry 
def get_edge(grid, nodes, node, start_point : tuple[int, int], visited : set) -> tuple[int, int]:
    current_pos : tuple[int, int] = start_point
    visited.add(current_pos)
    visited.add(node)
    steps = 0
    while True:
        if grid[current_pos[0]][current_pos[1]] == '_':
            return (current_pos, steps + 1)
        
        curr_dir = get_direction(grid, visited, current_pos)
        current_pos = (current_pos[0] + curr_dir[0], current_pos[1] + curr_dir[1])
        visited.add(current_pos)
        steps += 1

longest_path = 0
#Calculates lengths of all the paths from the start to the end
def solve(dfs_visited : set[int], graph : dict[int, list[tuple[int,int]]], 
          node : tuple[int, int], length : int):
    global longest_path
    if node[0] not in dfs_visited:
        if node[0] == len(graph.keys()) - 1:
            if length > longest_path:
                longest_path = length
            return
        dfs_visited.add(node[0])
        for neighbour in graph[node[0]]:
            solve(dfs_visited.copy(), graph, neighbour, length + neighbour[1])

start_time = timer()

grid = []

with open("./input.txt") as f:
    grid = [list(x) for x in f.read().strip().splitlines()]

grid[0][1] = '#'
start = (1, 1)
grid[GRID_SIZE - 1][GRID_SIZE - 2] = '#'
end = (GRID_SIZE - 2, GRID_SIZE - 2)
nodes_coords : dict[tuple[int, int], int] = {}
nodes_coords[start] = 0

#Start by finding all intersections and creating nodes out of them
c = 1
for i, row in enumerate(grid):
    for j, col in enumerate(row):
        if col == '#':
            continue
        if is_intersection(grid, (i, j)):
            nodes_coords[(i, j)] = c
            grid[i][j] = '_' #Change intersection to _
            c += 1
        else:
            grid[i][j] = '.'
nodes_coords[end] = c
grid[start[0]][start[1]] = '_'
grid[end[0]][end[1]] = '_'

#print(grid)

adj_list : dict[int, list[tuple[int,int]]] = {}
for i in range(len(nodes_coords)):
    adj_list[i] = []

visited = set()
#For each node find the neighbouring nodes and the path lengths to them
for node in nodes_coords.keys():
    if node == end:
        break
    #As there is a one way route from one intersection to another, we can just iterate and count
    routes = get_routes(grid, node, visited)
    for route in routes:
        x = get_edge(grid, nodes_coords, node, route, visited)
        adj_list[nodes_coords[node]].append((nodes_coords[x[0]], x[1]))
        adj_list[nodes_coords[x[0]]].append((nodes_coords[node], x[1]))
        visited.remove(x[0])

#Actual path finding
path_finding_start = timer()
dfs_visited = set()

solve(dfs_visited, adj_list, (0, 0), 2)
end_time = timer()
print(longest_path)
print("Time since the beginning:", end_time - start_time)
print("Time taken by the preprocessing:", path_finding_start - start_time)
print("Time taken to calculate all paths lengths:", end_time - path_finding_start)
