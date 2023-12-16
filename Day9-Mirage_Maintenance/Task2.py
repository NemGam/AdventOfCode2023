
res = 0
with open("./input.txt") as f:
    for line in f:
        li = [[int(i) for i in line.split()]]
        
        #Iterate through all the values
        for i in range(len(li[0])):
            l = []
            rowSum = 0
            #Get differences from the current row
            for j in range(len(li[i]) - 1):
                s = li[i][j+1] - li[i][j]
                rowSum += s
                l.append(s)
            if rowSum == 0:
                break
            li.append(l)
        x = 0

        #Extrapolate the values
        for i in range(len(li) - 1, -1, -1):
            x = li[i][0] - x               
        res += x
print(res)