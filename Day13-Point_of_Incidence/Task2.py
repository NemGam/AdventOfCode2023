global_diffs = 0

def check_row_symmetry(grid, middle_index, max_diffs) -> bool:
    global global_diffs
    l = min(len(grid) - middle_index - 1, middle_index + 1)
    for j in range(l):
        global_diffs += sum(0 if a == b else 1 for a,b in zip(grid[middle_index - j], grid[middle_index + j + 1]))
    if global_diffs != max_diffs:
        return False
    return True

#Check if any two lines are equal
def check_rows(grid, max_diffs) -> int:   
    global global_diffs
    for i in range(len(grid) - 1):
        global_diffs = 0
        if check_row_symmetry(grid, i, max_diffs):
            return i + 1
    return 0


grids = []
with open("./input.txt") as f:
    grids = f.read().strip().split("\n\n")

res = 0
for line in grids:
    global_diffs = 0
    grid = line.splitlines()
    c = check_rows(grid, 1) * 100
    if c != 0:
        res += c
        continue
    
    #Transpose
    grid = list(zip(*grid))

    res += check_rows(grid, 1)
print(res)