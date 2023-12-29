import re
from functools import cmp_to_key

GRID_SIZE = 10

class Block:
    def __init__(self, id : int,  x_range : tuple, y_range : tuple, z_range : tuple):
        self.id = id
        self.x_range = x_range
        self.y_range = y_range
        self.z_range = z_range
    
    def __str__(self):
        return f"|{self.id}|"
    
    def __repr__(self):
        return str(self)


def compare_blocks(a : Block, b : Block):
    if a.z_range[0] > b.z_range[0]:
        return 1
    else:
        return -1

ordered_blocks : list[Block] = []
supported_by = {} #Bottom neighbours
supports = {} #Top neighbours

block_count = 0
#To keep track of the top blocks
grid = [[(None, 0) for x in range(GRID_SIZE)] for y in range(GRID_SIZE)]

with open("./input.txt") as f:
    for id, line in enumerate(f):
        data = [int(x) for x in re.split(",|~", line)]
        block = Block(id, (data[0], data[3]), 
                                    (data[1], data[4]),
                                    (data[2], data[5]))
        ordered_blocks.append(block)
        block_count += 1
cmp_key = cmp_to_key(compare_blocks)
ordered_blocks.sort(key=cmp_key)

for block in ordered_blocks:
    maxz = 0
    #Find the highest point under the current block
    for x in range(block.x_range[0], block.x_range[1] + 1):
        for y in range(block.y_range[0], block.y_range[1] + 1):
            if grid[x][y][1] > maxz:
                maxz = grid[x][y][1]
    
    below_blocks : list[Block] = []
    #Collect all the blocks that contact the current block at the max hight
    for x in range(block.x_range[0], block.x_range[1] + 1):
        for y in range(block.y_range[0], block.y_range[1] + 1):
            if grid[x][y][1] == maxz:
                if grid[x][y][0] and grid[x][y][0] not in below_blocks:
                    below_blocks.append(grid[x][y][0])

    #Add the blocks that will support the current block to the lists
    for b_block in below_blocks:
        if b_block.id in supports:
            supports[b_block.id].append(block.id)
        else:
            supports[b_block.id] = [block.id]

        if block.id in supported_by:
            supported_by[block.id].append(b_block.id)
        else:
            supported_by[block.id] = [b_block.id]
    
    #Replace current top block references with the current block references
    for x in range(block.x_range[0], block.x_range[1] + 1):
        for y in range(block.y_range[0], block.y_range[1] + 1):
            grid[x][y] = (block, block.z_range[1] - block.z_range[0] + 1 + maxz)
                

#print("Supports: ", supports)
#print("Supported by: ", supported_by)

res = 0
for i in range(block_count):
    if i not in supports:
        res += 1
        continue
    free_blocks = 0 #Blocks that I support, but are also supported by someone else
    for supported_block in supports[i]:
        if len(supported_by[supported_block]) > 1:
            free_blocks += 1
    if free_blocks == len(supports[i]):
        res += 1
print(res)
#A - 0, B - 1, C - 2, D - 3, E - 4, F - 5, G - 6