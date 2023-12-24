boxes = [[] for _ in range(256)]

def calculate_result() -> int:
    res = 0
    for ind, box in enumerate(boxes):
        if len(box) == 0:
            continue
        res += sum([(ind + 1) * lense[1] * (slot + 1) for slot, lense in enumerate(box)])
    return res

def HASH(string : str) -> int:
    current_value = 0
    for char in string:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value

def remove_from_box(box_num : int, lens_label : str):
    for ind, lense in enumerate(boxes[box_num]):
        if lense[0] == lens_label:
            boxes[box_num].pop(ind)
            break

def modify_box(box_num : int, new_lense : tuple):
    for ind, lense in enumerate(boxes[box_num]):
        if lense[0] == new_lense[0]:
            boxes[box_num][ind] = new_lense
            return
    boxes[box_num].append(new_lense)

res = 0
with open("./input.txt") as f:
    for line in f:
        label = ""
        fl = -1
        op = ''
        FocalLength = False
        for char in line:
            if FocalLength == True:
                fl = int(char)
                FocalLength = False
                continue

            if char == ',':
                if op == '-':
                    remove_from_box(HASH(label), label)
                else:
                    modify_box(HASH(label), (label, fl))
                label = ""
                
            elif char == '-':
                op = char
            elif char == '=':
                op = char
                FocalLength = True
            else:
                label += char

        if op == '-':
            remove_from_box(HASH(label), label)
        else:
            modify_box(HASH(label), (label, fl))
            

print(calculate_result())