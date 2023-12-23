def check_row_symmetry(grid, middle_index) -> bool:
    l = min(len(grid) - middle_index - 1, middle_index + 1)
    for j in range(l):
        if grid[middle_index - j] != grid[middle_index + j + 1]:
            return False
    return True

#Check if any two lines are equal
def check_rows(grid) -> int:   
    for i in range(len(grid) - 1):
        if grid[i] == grid[i + 1]:
            if check_row_symmetry(grid, i):
                return i + 1
    return 0


grids = []
with open("./input.txt") as f:
    grids = f.read().strip().split("\n\n")

res = 0
for line in grids:
    grid = line.splitlines()

    res += check_rows(grid) * 100
    
    #Transpose
    grid = list(zip(*grid))

    res += check_rows(grid)

print(res)