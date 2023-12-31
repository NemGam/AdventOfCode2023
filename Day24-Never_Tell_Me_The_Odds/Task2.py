import re
from timeit import default_timer as timer
#This solution was inspired by 
#https://www.reddit.com/r/adventofcode/comments/18pnycy/comment/keqf8uq

BRUTEFORCE_LIMIT = 200 #Very sensitive value. Better start high

def find_set(a : int, b : int, Δa : int, existing_set : set):
    new_set = set()
    distance = b - a
    for velocity in range(-BRUTEFORCE_LIMIT, BRUTEFORCE_LIMIT):
        if velocity == Δa:
            continue

        if distance % (velocity - Δa) == 0:
            new_set.add(velocity)

    if existing_set: return existing_set.intersection(new_set)
    else: return new_set
        
heilstones = []
with open("./input.txt") as f:
    for line in f:
        x = re.split(",|@",line)
        heilstones.append([int(z) for z in x])

start_time = timer()

#Iterate through all the pairs of heilstones and create sets of suitable heilstones
x_set : set = None
y_set : set = None
z_set : set = None
for i in range(len(heilstones)):
    for j in range(i + 1, len(heilstones)):
        x1, y1, z1, dx1, dy1, dz1 = heilstones[i]
        x2, y2, z2, dx2, dy2, dz2 = heilstones[j]

        if dx1 == dx2:
            x_set = find_set(x1, x2, dx1, x_set)
            if len(x_set) == 1:
                break
            
        if dy1 == dy2:
            y_set = find_set(y1, y2, dy1, y_set)
            if len(y_set) == 1:
                break
        
        if dz1 == dz2:
            z_set = find_set(z1, z2, dz1, z_set)
            if len(z_set) == 1:
                break

rock_velocity = (x_set.pop(), y_set.pop(), z_set.pop())

x1, y1, z1, dx1, dy1, dz1 = heilstones[0]
x2, y2, z2, dx2, dy2, dz2 = heilstones[1]

#Find the line that will intersect all the heilstones
m1 = (dy1 - rock_velocity[1]) / (dx1 - rock_velocity[0])
m2 = (dy2 - rock_velocity[1]) / (dx2 - rock_velocity[0])
x = (m2 * x2 - m1 * x1 - y2 + y1) // (m2 - m1)
y = m1 * x + y1 - m1 * x1
t = (x - x1) // (dx1 - rock_velocity[0])
z = z1 + (dz1 - rock_velocity[2]) * t

print("Finished at", timer() - start_time)
print(x + y + z)