from collections import defaultdict, deque

def count_paths(graph : defaultdict, visited : set, first_mod):
    paths = 0
    for module in graph[first_mod]:
        if module == comp:
            paths += 1
            continue
        q = set()
        queue = deque()
        queue.append((module, [module]))
        found = False
        while queue and not found and paths < 4:
            mod, path = queue.popleft()
            for m in graph[mod]:
                if comp == m:
                    paths += 1
                    visited.update(path)
                    found = True
                    break
                elif (m not in q
                      and m not in path 
                      and m not in visited):
                    queue.append([m, path + [m]])
                    q.add(m)
    return paths
adj_list = defaultdict(lambda:set())


with open("./input.txt") as f:
    for line in f:
        module, connected_modules = line.strip().split(': ')
        connected_modules = connected_modules.split()
        for conn in connected_modules:
            adj_list[module].add(conn)
            adj_list[conn].add(module)
    

graph1 = 1
graph2 = 0

start = list(adj_list.keys())[0]

for comp in list(adj_list.keys())[1:]:
    visited = {start}
    paths = count_paths(adj_list, visited, start)

    if paths >= 4: graph1 += 1   
    else: graph2 += 1
        

print(graph1 * graph2)