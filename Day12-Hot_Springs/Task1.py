def computeSequence(initialSequence : list, groups : list) -> int:
    if len(initialSequence) == 0 and len(groups) == 0:
        return 1
    elif len(initialSequence) == 0 and len(groups) > 0:
        return 0
    elif (len(initialSequence) > 0 and len(groups) == 0):
        for symbol in initialSequence:
            if symbol == '#':
                return 0
        return 1
    
    if len(initialSequence) < groups[0]:
            return 0
    
    if initialSequence[0] == '.':
        initialSequence.pop(0)
        return computeSequence(initialSequence.copy(), groups.copy())
            
    #If the first symbol is # - all the following symbols must be also #
    if initialSequence[0] == '#':
        for i in range(groups[0] - 1, -1, -1):
            if initialSequence[i] == '.':
                return 0
            initialSequence.pop(i)
        groups.pop(0)
        if len(initialSequence) > 0:
            if initialSequence[0] == '#':
                return 0
            initialSequence[0] = '.'
        return computeSequence(initialSequence.copy(), groups.copy())
        
    if initialSequence[0] == '?':
        cpy1 = initialSequence.copy()
        cpy2 = initialSequence.copy()
        cpy1[0] = '.'
        cpy2[0] = '#'
        return computeSequence(cpy1, groups.copy()) + computeSequence(cpy2, groups.copy())


res = 0
with open("./input.txt") as f:
    
    for line in f:
        springs, groups = line.split()
        springs = list(springs.strip('.'))
        groups = [int(x) for x in groups.split(',')]

        res += computeSequence(springs, groups)

print(res)
