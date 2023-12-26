import re
from copy import deepcopy, copy

class Range:
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def __str__(self) -> str:
        return f"Range({self.min}, {self.max})"
    
    def __repr__(self) -> str:
        return str(self)
    
    def get_range(self):
        return self.max - self.min + 1
    
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
    #(Range(1, 4000), Range(1, 4000), Range(1, 4000), Range(1, 4000))
    #Returns [rejected by rule, accepted by rule, next_workflow for accepted]
    #Check the value from the given list
    def check(self, range_to_check : list) -> list:
        if self.__op == '<':
            #Whole range is accepted
            if range_to_check[self.var_to_check].max < self.__value:
                return [None, range_to_check, self.out]
            #Whole range is regected
            elif range_to_check[self.var_to_check].min > self.__value:
                return [range_to_check, None, None]
            else:
            #Slice the range into two
                accepted_range = deepcopy(range_to_check)
                accepted_range[self.var_to_check].max = self.__value - 1

                rejected_range = deepcopy(range_to_check)
                rejected_range[self.var_to_check].min = self.__value

                return [rejected_range, accepted_range, self.out]
        else: #>
            #Whole range is accepted
            if range_to_check[self.var_to_check].min > self.__value:
                return [None, range_to_check, self.out]
            #Whole range is regected
            elif range_to_check[self.var_to_check].max < self.__value:
                return [range_to_check, None, None]
            else:
            #Slice the range into two
                accepted_range = deepcopy(range_to_check)
                accepted_range[self.var_to_check].min = self.__value + 1

                rejected_range = deepcopy(range_to_check)
                rejected_range[self.var_to_check].max = self.__value  

                return [rejected_range, accepted_range, self.out]
        
    def __str__(self) -> str:
        return f"(This is the rule: {self.var_to_check}, {self.__op}, {self.__value}, {self.out})"
    
    def __repr__(self) -> str:
        return str(self)


class Workflow:
    def __init__(self, workflow_rules : list[Rule], out : str):
        self.workflow_rules = workflow_rules
        self.out = out
    #Range is (Range(min, max), Range(min, max), Range(min, max), Range(min, max))
    def evaluate(self, range : tuple) -> str:
        results = []
        rejected = range
        for rule in self.workflow_rules:
            #(rejected by rule, accepted by rule, next_workflow for accepted)
            rejected, accepted, next_workflow = rule.check(rejected)
            if accepted != None:
                results.append((accepted, next_workflow))
            
            if rejected == None:
                break
        if rejected != None:
            results.append((rejected, self.out))
        return results


def parse_rule(rule_data : str) -> list:
    r = rule_data.split(',')
    rules = []
    for i in range(len(r)-1):
        x = re.split('>|<|:', r[i])
        x.insert(1, r[i][1])
        rules.append(Rule(map_var_to_value(x[0]), x[1], int(x[2]), x[3]))
    rules.append(r[-1])
    return rules

def solve(undecided_ranges):
    new_ranges = []
    accepted_ranges = []
    for range in undecided_ranges:
        if range[1] == 'A':
            accepted_ranges.append(range)
            continue
        if range[1] == 'R':
            continue
        new_ranges.extend(workflows[range[1]].evaluate(range[0]))
    if len(new_ranges) == 0:
        return accepted_ranges

    accepted_ranges.extend(solve(new_ranges))
    return accepted_ranges

with open("./input.txt") as f:
    data = f.read().strip().splitlines()
    ind = data.index('')
    w, d = [data[:ind],data[ind+1:]]

workflows = {str : Workflow}
for w_data in w:
    rules = parse_rule(w_data[w_data.index('{') + 1:-1])
    workflows[w_data[:w_data.index('{')]] = Workflow(rules[:-1], rules[-1])

accepted = []
z = solve([((Range(1, 4000), Range(1, 4000), Range(1, 4000), Range(1, 4000)), "in")])

res = 0
for ranges in z:
    res += ranges[0][0].get_range() * ranges[0][1].get_range() * ranges[0][2].get_range() * ranges[0][3].get_range() 
print(res)
