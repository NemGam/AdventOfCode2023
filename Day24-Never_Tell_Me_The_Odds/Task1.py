import re

TEST_AREA_MIN = 200000000000000
TEST_AREA_MAX = 400000000000000

def intersection_point(a : tuple[tuple[int, int], tuple[int, int]], 
                       b : tuple[tuple[int, int], tuple[int, int]]):
    (x1, y1), (dx1, dy1) = a
    (x2, y2), (dx2, dy2) = b
    m1 = dy1 / dx1
    m2 = dy2 / dx2
    if m1 == m2:
        return (-1000000, -1000000)
    return ((m2 * x2 - m1 * x1 - y2 + y1) / (m2 - m1),
            (m1 * x2 * m2 - m1 * y2 - m1 * x1 * m2 + y1 * m2) / (m2 - m1))


def is_in_future(target : tuple, relative_to : int):
    return (target[1] > 0 and target[0] < relative_to) or (target[1] < 0 and target[0] > relative_to)

heilstones = []
with open("./input.txt") as f:
    for line in f:
        x = re.split(",|@",line)
        heilstones.append(((int(x[0]), int(x[1])), 
                           (int(x[3]), int(x[4]))))

res = 0
for i in range(len(heilstones)):
    for j in range(i + 1, len(heilstones)):
        x = intersection_point(heilstones[i], heilstones[j])
        if (TEST_AREA_MIN <= x[0] <= TEST_AREA_MAX 
            and TEST_AREA_MIN <= x[1] <= TEST_AREA_MAX
            and is_in_future((heilstones[i][0][0], heilstones[i][1][0]), x[0])
            and is_in_future((heilstones[j][0][0], heilstones[j][1][0]), x[0])):
                res += 1

print(res)