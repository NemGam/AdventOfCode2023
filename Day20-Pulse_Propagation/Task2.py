from collections import deque

LOW = 0
HIGH = 1

def gcd(a, b):
    if(b == 0):
        return abs(a)
    else:
        return gcd(b, a % b)

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
target_sender : str = "" #Module that sends signal to the "rx" module
with open("./input.txt") as f:
    for line in f:
        name, recievers = line.split("->")
        name = name.strip()
        if name == "broadcaster":
            t = "broadcaster"
        else:
            name = name[1:]
            t = line[0]
        
        module = Module(name, t, recievers.strip().split(", "))
        modules[name] = module
        if "rx" in module.recievers:
            target_sender = module.name


#After all modules are processed, reset inputs of all the conc modules
for name, mod in modules.items():
    for rec in mod.recievers:
        if rec in modules and modules[rec].type == '&':
            modules[rec].inputs[name] = LOW
dists : dict[str, int] = {}
vis = {}
count : int = 0
for name, module in modules.items():
    if target_sender in module.recievers:
        vis[name] = False

#Press the button
while True:
    count += 1

    #Start with the broadcaster
    queue = deque()
    queue.extend([("broadcaster", x, LOW) for x in modules["broadcaster"].recievers])
    while queue:
        s, dest, pulse = queue.popleft()

        if dest not in modules:
            continue

        module = modules[dest]

        if module.name == target_sender and pulse == HIGH:
            vis[s] = True

            if s not in dists:
                dists[s] = count

            #If visited everything
            if sum(vis.values()) == len(vis.values()):
                p = 1
                for l in dists.values():
                    p *= l // gcd(p, l)
                print(p)
                exit(0)

        if module.type == '%':
            if pulse == LOW:
                if module.inputs == False:
                    module.inputs = True
                    out = HIGH
                else:
                    module.inputs = False
                    out = LOW

                for rec in module.recievers:
                    queue.append((module.name, rec, out))
        else:
            module.inputs[s] = pulse
            vals = module.inputs.values()
            l = len(vals)
            if sum(vals) == l:
                out = LOW
            else:
                out = HIGH

            for rec in module.recievers:
                queue.append((module.name, rec, out))
#238420328103151