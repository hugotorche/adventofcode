import re

with open('runs/sources/puzzleinput_6.txt', 'r', encoding='utf-8') as puzzleinput:
    inputs = puzzleinput.read().splitlines()
    races = [[input] for input in inputs]

# Joining numbers for part 2 for keeping list format
times = [''.join(re.findall(r'(\d+)', inputs[0]))]
distances = [''.join(re.findall(r'(\d+)', inputs[1]))]

# wins_list will contains the number of wins per race
wins_list = []
for i in range(len(distances)):
    distance = int(distances[i])
    time = int(times[i])
    holding_times = range(time+1)
    wins = 0
    for holding_time in holding_times:
        speed_time = time - holding_time
        total_distance = speed_time * holding_time
        if total_distance > distance:
            wins += 1
    wins_list.append(wins)


# For part 1 multiplication
def multiplyList(myList):
    result = 1
    for x in myList:
        result = result * x
    return result


print(multiplyList(wins_list))

# For part 2
print(wins_list)
