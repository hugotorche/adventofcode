with open('runs/sources/puzzleinput_15.txt', 'r', encoding='utf-8') as puzzleinput:
    steps = puzzleinput.read()

# steps = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'
boxes = {i: [] for i in range(256)}
all_values = []
for step in steps.split(','):
    current_value = 0
    for i in range(len(step)):
        current_value += ord(step[i])
        current_value = current_value * 17
        current_value = current_value % 256
        if (i != len(step) - 1 and step[i+1] in ['=', '-']):
            box_value = current_value
    if '-' in step:
        label = step.split('-')[0]
        for i, val in enumerate(boxes[box_value]):
            if label in val:
                boxes[box_value].remove(val)
    elif '=' in step:
        label = step.split('=')[0]
        flag = 0
        for i, val in enumerate(boxes[box_value]):
            if label in val:
                flag += 1
                boxes[box_value][i] = step
        if flag == 0:
            boxes[box_value].append(step)

    all_values.append(current_value)

# print(sum(all_values))

focusing_powers = []
for key in list(boxes.keys()):
    for i, el in enumerate(boxes[key]):
        power = (key+1) * (i+1) * int(el[-1])
        focusing_powers.append(power)

# print(sum(focusing_powers))
