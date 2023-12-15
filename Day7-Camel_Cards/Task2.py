from functools import cmp_to_key
from collections import Counter

valueConverter = {
    "J" : 1,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "T" : 10,
    "Q" : 11,
    "K" : 12,
    "A" : 13,
}

def most_common(l):
    data = Counter(l)
    return data.most_common(1)[0][0]

#Sort hands by comparing each of their cards to find the first that
#is not equal. 
def handsCompare(x, y):
    for i in range(5):
        a = valueConverter[x[0][i]]
        b = valueConverter[y[0][i]]
        if a > b:
            return -1
        if a < b:
            return 1
        

five_of_a_kind = []
four_of_a_kind = []
full_house = []
three_of_a_kind = []
two_pair = []
one_pair = []
high_card = []

with open("./input.txt") as f:
    for line in f:
        newEl = (line[:5], line[6:].strip())
        hand = list(line[:5])
        cleanHand = line[:5].replace('J', '') #hand w/o 'J's
        if (len(cleanHand) > 0):
            #Find the most common element excluding 'J'
            most = most_common(cleanHand)
            
            #Replace all the 'J' with the most common element
            for i in range(5):
                if hand[i] == 'J':
                    hand[i] = most
            
        setHand = list(set(hand))

        

        if len(setHand) == 1: #(5)
            five_of_a_kind.append(newEl)
            continue
        elif len(setHand) == 4:#(2, 1, 1, 1)
            one_pair.append(newEl)
            continue
        elif len(setHand) == 5:#(1, 1, 1, 1, 1)
            high_card.append(newEl)
            continue
        
        #At this point we have the following options:
        if (len(setHand) == 2): #(4, 1) or (2, 3)
            c = hand.count(setHand[0])
            if c == 1 or c == 4:
                four_of_a_kind.append(newEl)
            else:
                full_house.append(newEl)
        else: #(3, 1, 1) or (2, 2, 1)
            c = hand.count(setHand[0])
            if c == 1:
                c = hand.count(setHand[1])
                if c == 1 or c == 3:
                    three_of_a_kind.append(newEl)
                else:
                    two_pair.append(newEl)
                continue
            elif c == 3:
                three_of_a_kind.append(newEl)
            else:
                two_pair.append(newEl)
            continue

cmp_key = cmp_to_key(handsCompare)
five_of_a_kind.sort(key=cmp_key)
four_of_a_kind.sort(key=cmp_key)
full_house.sort(key=cmp_key)
three_of_a_kind.sort(key=cmp_key)
two_pair.sort(key=cmp_key)
one_pair.sort(key=cmp_key)
high_card.sort(key=cmp_key)

final = five_of_a_kind + four_of_a_kind + full_house + three_of_a_kind + two_pair + one_pair + high_card
l = len(final)
res = 0
for i in range(l - 1, -1, -1):
    res += (i + 1) * int(final[l - i - 1][1])

print(res)