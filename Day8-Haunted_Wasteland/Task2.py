nodes = {}

startNodes = []
def fill_nodes():
    with open("./input.txt") as f:
        instructions = f.readline().strip()
        f.readline()
        for line in f:
            nodes[line[:3]] = (line[7:10], line[12:15])
            if line[2] == 'A':
                startNodes.append(line[:3])
    return instructions

def gcd(a, b): 
      
    if (a == 0): 
        return b 
    return gcd(b % a, a) 
  
def lcm(a, b): 
      
    return (a * b) / gcd(a, b) 


instructions = fill_nodes()
l = len(instructions)
stepList = []
for i in range(len(startNodes)):
    current_node = startNodes[i]
    current_options = nodes[current_node]
    steps = 0
    while current_node[2] != "Z":
        instr = instructions[steps % l]
        if instr == 'L':
            current_node = current_options[0]
            current_options = nodes[current_options[0]]
        else:
            current_node = current_options[1]
            current_options = nodes[current_options[1]]
        steps += 1
    stepList.append(steps)
print(stepList)
print(lcm(stepList[0], lcm(stepList[1], lcm(stepList[2], lcm(stepList[3], lcm(stepList[4], stepList[5]))))))