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
    return -1

def check_column_symmetry(line : str, middle_index : int) -> bool:
    l = min(len(line) - middle_index, middle_index)
    for i in range(l - 1):
        if line[middle_index - i] != line[middle_index + 1 + i]:
            return False
    return True


def get_possible_columns(first_line) -> list[int]:
    possible_columns = []
    for j in range(len(first_line) - 1):
        if first_line[j] == first_line[j + 1]:
            if check_column_symmetry(first_line, j):
                possible_columns.append(j)
    return possible_columns

#Checks columns. Should always return the result, as rows are checked before the call of this function
#and there is always just one symmetry line 
def check_columns(grid, possible_columns : list[int]):
    for i in range(1, len(grid)):
        for j in range(len(possible_columns) - 1, -1, -1):
            if not check_row_symmetry(grid[i], possible_columns[j]):
                possible_columns.pop(j)
    if len(possible_columns) == 0:
        raise Exception("It is impossible to get no columns!")
    else:
        return possible_columns[0] + 1

        

grids = []
with open("./input.txt") as f:
    grids = f.read().strip().split("\n\n")

res = 0
for line in grids:
    grid = line.split('\n')

    c = check_rows(grid)
    if c != -1:
        res += c * 100
        continue

    z = get_possible_columns(grid[0])
    if len(z) == 1:
        res += z[0]
    else:
        z = check_columns(grid, z)
        #res += check_columns(grid, z)
        res += z

print(res + 1)