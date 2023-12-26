import re


class Detail:
    def __init__(self, x : int, m : int, a : int, s : int):
        self.values = [0, 0, 0, 0]
        self.values[0] = x
        self.values[1] = m
        self.values[2]= a
        self.values[3] = s
    
    def get_overall_rating(self) -> int:
        return sum(self.values)

    def __str__(self) -> str:
        return f"(x: {self.values[0]}, m: {self.values[1]}, a: {self.values[2]}, s: {self.values[3]})"
    
    def __repr__(self) -> str:
        return str(self)
    
    def map_var_to_value(var_name : str) -> int:
        if var_name == 'x': return 0
        if var_name == 'm': return 1
        if var_name == 'a': return 2
        if var_name == 's': return 3
        raise ValueError(f"Variable of name {var_name} cannot be mapped!")

class Rule:
    def __init__(self, var_to_check : int, op : str, value : int, out : str):
        self.var_to_check = var_to_check
        self.__op = op
        self.__value = value
        self.out = out
    
    #Check the value from the given list
    def check(self, value_to_check : list) -> str | None:
        if self.__op == '<':
            if value_to_check[self.var_to_check] < self.__value:
                return self.out
            return None
        else:
            if value_to_check[self.var_to_check]  > self.__value:
                return self.out
            return None
        
    def __str__(self) -> str:
        return f"(This is the rule: {self.var_to_check}, {self.__op}, {self.__value}, {self.out})"
    
    def __repr__(self) -> str:
        return str(self)


class Workflow:
    def __init__(self, workflow_rules : list[Rule], out : str):
        self.workflow_rules = workflow_rules
        self.out = out
    
    def evaluate(self, detail : Detail) -> str:
        for rule in self.workflow_rules:
            #If rule returns something -> go to the given workflow name
            if rule.check(detail.values):
                return rule.out
        return self.out

#Parse detail data and return Detail object
def parse_detail(detail_data : str) -> Detail:
    z = detail_data[1:-1].split(',')
    z = [int(x) for x in [y[2:] for y in z]]
    det = Detail(z[0], z[1], z[2], z[3])
    return det

def parse_rule(rule_data : str) -> list:
    r = rule_data.split(',')
    rules = []
    for i in range(len(r)-1):
        x = re.split('>|<|:', r[i])
        x.insert(1, r[i][1])
        rules.append(Rule(Detail.map_var_to_value(x[0]), x[1], int(x[2]), x[3]))
    rules.append(r[-1])
    return rules



with open("./input.txt") as f:
    data = f.read().strip().splitlines()
    ind = data.index('')
    w, d = [data[:ind],data[ind+1:]]

details = [parse_detail(x) for x in d]

workflows = {str : Workflow}
for w_data in w:
    rules = parse_rule(w_data[w_data.index('{') + 1:-1])
    workflows[w_data[:w_data.index('{')]] = Workflow(rules[:-1], rules[-1])

accepted = []
for detail in details:
    out = workflows["in"].evaluate(detail)
    while out != 'A' and out != 'R':
        out = workflows[out].evaluate(detail)
    
    if out == 'A':
        accepted.append(detail)

print(sum([x.get_overall_rating() for x in accepted]))
