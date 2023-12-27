from collections import deque

class Module:
    def __init__(self, name : str, type : str, recievers : list[str]):
        self.name = name
        self.recievers = recievers
        self.type = type
        if self.type == '%':
            self.inputs = False  
        else: 
            self.inputs = {}

modules : dict [str, Module]= {}
with open("./input.txt") as f:
    for line in f:
        name, recievers = line.split("->")
        name = name.strip()
        if name == "broadcaster":
            t = "broadcaster"
        else:
            name = name[1:]
            t = line[0]
            
        modules[name] = Module(name, t, recievers.strip().split(", "))

#After all modules are processed, reset inputs of all the conc modules
for name, mod in modules.items():
    for rec in mod.recievers:
        if rec in modules and modules[rec].type == '&':
            modules[rec].inputs[name] = 0

lows = 0
highs = 0

#Press the button
for i in range(1000):
    lows += 1

    #Start with the broadcaster
    queue = deque()
    queue.extend([("broadcaster", x, 0) for x in modules["broadcaster"].recievers])
    while queue:
        s, dest, pulse = queue.popleft()

        if pulse == 0: lows += 1       
        else: highs += 1

        if dest not in modules:
            continue

        module = modules[dest]

        if module.type == '%':
            if pulse == 0:
                if module.inputs == False:
                    module.inputs = True
                    out = 1
                else:
                    module.inputs = False
                    out = 0

                for rec in module.recievers:
                    queue.append((module.name, rec, out))
        else:
            module.inputs[s] = pulse
            vals = module.inputs.values()
            l = len(vals)
            if sum(vals) == l:
                out = 0
            else:
                out = 1

            for rec in module.recievers:
                queue.append((module.name, rec, out))

print(lows * highs)
