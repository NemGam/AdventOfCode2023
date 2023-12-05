cards = [1] * 205

def getWinningCounts(s):
    w = s[s.index(':') + 1: s.index('|')]
    winningNums = {key: '0' for key in w.split()}
    nums = s[s.index('|') + 1:].split()
    count = 0
    for num in nums:
        if num in winningNums:
            count += 1
    return count


f = open("./input.txt")


i = 0
cards[0] = 0
for line in f:
    i += 1
    n = getWinningCounts(line.strip())
    for j in range(i + 1, i + n + 1):
        cards[j] += cards[i]

    
f.close()

print(f"Result: {sum(cards)}")