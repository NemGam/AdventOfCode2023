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
def get_routes(grid, coords : tuple[int, int]) -> list[tuple[int,int]]:
    res = []
    if grid[coords[0]][coords[1] + 1] in ['>', '.']: res.append((coords[0], coords[1] + 1))
    if grid[coords[0]][coords[1] - 1] in ['<', '.']: res.append((coords[0], coords[1] - 1))
    if grid[coords[0] - 1][coords[1]] in ['^', '.']: res.append((coords[0] - 1, coords[1]))
    if grid[coords[0] + 1][coords[1]] in ['v', '.']: res.append((coords[0] + 1, coords[1]))
    return res

#Returns direction for the given point on the grid
def get_direction(grid, visited, pos : tuple[int, int]) -> tuple[int, int]:
    if (pos[0], pos[1] + 1) not in visited and grid[pos[0]][pos[1] + 1] in ['>', '.', '_']: return (0, 1)
    if (pos[0], pos[1] - 1) not in visited and grid[pos[0]][pos[1] - 1] in ['<', '.', '_']: return (0, -1)
    if (pos[0] - 1, pos[1]) not in visited and grid[pos[0] - 1][pos[1]] in ['^', '.', '_']: return (-1, 0)
    if (pos[0] + 1, pos[1]) not in visited and grid[pos[0] + 1][pos[1]] in ['v', '.', '_']: return (1, 0)
    raise Exception(f"Wasn't able to find the direction at {pos}")

#Converts grid path between two nodes into adjacency list entry 
def get_edge(grid, nodes, node, start_point : tuple[int, int]) -> tuple[int, int]:
    visited = set()
    current_pos : tuple[int, int] = start_point
    visited.add(current_pos)
    visited.add(node)
    steps = 0
    while True:
        if grid[current_pos[0]][current_pos[1]] == '_':
            return (nodes[current_pos], steps + 1)
        
        curr_dir = get_direction(grid, visited, current_pos)
        current_pos = (current_pos[0] + curr_dir[0], current_pos[1] + curr_dir[1])
        visited.add(current_pos)
        steps += 1


#Calculates lengths of all the paths from the start to the end
def solve(graph : dict[int, list[tuple[int,int]]], 
          node : tuple[int, int], length : int, path_lengths : list[int]):
    if node[0] == len(graph.keys()) - 1:
        path_lengths.append(length)
        return
    for neighbour in graph[node[0]]:
        solve(graph, neighbour, length + neighbour[1], path_lengths)

start_time = timer()

grid = []

with open("./input.txt") as f:
    grid = [list(x) for x in f.read().strip().splitlines()]

grid[0][1] = '#'
start = (1, 1)
grid[start[0]][start[1]] = '_'
grid[GRID_SIZE - 1][GRID_SIZE - 2] = '#'
end = (GRID_SIZE - 2, GRID_SIZE - 2)
grid[end[0]][end[1]] = '_'

nodes_coords : dict[tuple[int, int], int] = {}
nodes_coords[start] = 0

#Start by finding all intersections and creating nodes out of them
c = 1
for i, row in enumerate(grid):
    for j, col in enumerate(row):
        if col != '.':
            continue
        if is_intersection(grid, (i, j)):
            nodes_coords[(i, j)] = c
            grid[i][j] = '_' #Change intersection to _
            c += 1
nodes_coords[end] = c

adj_list : dict[int, list[tuple[int,int]]] = {}
for i in range(len(nodes_coords)):
    adj_list[i] = []

#For each node find the neighbouring nodes and the path lengths to them
for node in nodes_coords.keys():
    if node == end:
        break
    #As there is a one way route from one intersection to another, we can just iterate and count
    routes = get_routes(grid, node)
    for route in routes:
        adj_list[nodes_coords[node]].append(get_edge(grid, nodes_coords, node, route))

#Actual path finding
path_finding_start = timer()
path_lengths = []
solve(adj_list, (0, 0), 2, path_lengths)
path_lengths.sort(reverse=True)
end_time = timer()
print(path_lengths[0])
print("Time since the beginning:", end_time - start_time)
print("Time taken by the preprocessing:", path_finding_start - start_time)
print("Time taken to calculate all paths lengths:", end_time - path_finding_start)
