nodes = {}

def fill_nodes():
    with open("./input.txt") as f:
        instructions = f.readline().strip()
        f.readline()
        for line in f:
            nodes[line[:3]] = (line[7:10], line[12:15])
    return instructions



instructions = fill_nodes()
l = len(instructions)
current_node = "AAA"
current_options = nodes[current_node]
steps = 0
while current_node != "ZZZ":
    instr = instructions[steps % l]
    if instr == 'L':
        current_node = current_options[0]
        current_options = nodes[current_options[0]]
    else:
        current_node = current_options[1]
        current_options = nodes[current_options[1]]
    steps += 1
print(steps)
    