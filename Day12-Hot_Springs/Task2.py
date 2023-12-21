#The solution is to use memorization/dp

LENGTH_MULT = 5

possibleSequences = {}

#Check if the given arguments have been computed before. Return the result if it exists.
def getResult(seq, groups):
    if seq + groups in possibleSequences:
        return possibleSequences[seq + groups]

    val = computeSequence(seq, groups)
    possibleSequences[seq + groups] = val
    return val

def computeSequence(sequence : str, groups : str) -> int:
    if len(sequence) == 0 and len(groups) == 0:
        return 1
    elif len(sequence) == 0 and len(groups) > 0:
        return 0
    elif (len(sequence) > 0 and len(groups) == 0):
        for symbol in sequence:
            if symbol == '#':
                return 0
        return 1
    
    firstGroup = int(groups.split(',', 1)[0])
    if len(sequence) < firstGroup:
        return 0
    
    if sequence[0] == '.':
        return computeSequence(sequence[1:], groups)
            
    #If the first symbol is # - all the following symbols must be also #
    if sequence[0] == '#':
        for i in range(firstGroup):
            if sequence[i] == '.':
                return 0
         
        sequence = sequence[firstGroup:]
        groups = groups[2:].lstrip(',')
        if len(sequence) > 0:
            #Next element must be '.' to separate groups
            if sequence[0] == '#':
                return 0
            sequence = '.' + sequence[1:]
        return computeSequence(sequence, groups)
        
    if sequence[0] == '?':
        seq = sequence[1:]
        return getResult('.' + seq, groups) + getResult('#' + seq, groups)


res = 0
with open("./input.txt") as f:
    x = 0
    for line in f:
        x += 1
        possibleSequences.clear()
        springs, groups = line.split()
        #Multiply springs
        finalSprings = springs
        springs = '?' + springs
        for i in range(LENGTH_MULT - 1):
            finalSprings += springs
        
        #Multiply groups
        finalGroups = groups
        groups = ',' + groups
        for i in range(LENGTH_MULT - 1):
            finalGroups += groups

        res += computeSequence(finalSprings, finalGroups)

print(res)