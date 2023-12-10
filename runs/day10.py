import re

puzzle_1 = '''.....
.S-7.
.|.|.
.L-J.
.....'''

puzzle_2 = '''..F7.
.FJ|.
SJ.L7
|F--J
LJ...'''

puzzle_3 = '''7||FJLJLF-J|LJ
||LJJF7|L-7L-7
||JJ.S|FJJL-7L
LJ--FJL7JF7FJF
JL-.L-7|FJLJFJ'''

with open('runs/sources/puzzleinput_10.txt', 'r', encoding='utf-8') as puzzleinput:
    puzzle_4 = puzzleinput.read()

symbols_map = {'|': 'NS',
               '-': 'EW',
               'L': 'NE',
               'J': 'NW',
               '7': 'SW',
               'F': 'NSE'}

digits_puzzle_re = re.sub('[L|J|7|F|-]', '.', puzzle_3).replace('|', '.')
digits_matrix = [list(puzzle) for puzzle in digits_puzzle_re.splitlines()]

puzzle = puzzle_3.splitlines()
print('---Init Puzzle:')
for d in puzzle:
    print(d)
lines = len(puzzle)
columns = len(puzzle[0])

for i in range(lines):
    for j in range(columns):
        if puzzle[i][j] == 'S':
            starting_coor = (i, j)
            print('---Starting point:')
            print(starting_coor)


p_coors = [(starting_coor[0], starting_coor[1]-1),
           (starting_coor[0], starting_coor[1]+1),
           (starting_coor[0]-1, starting_coor[1]),
           (starting_coor[0]+1, starting_coor[1])]
p_coors = [coor for coor in p_coors if coor[1] >= 0]
next_points = []
for coor in p_coors:
    symbol = puzzle[coor[0]][coor[1]]
    if (coor != starting_coor
            and symbol != '.'):
        digits_matrix[coor[0]][coor[1]] = '1'
        next_points.append(coor)

print('---Init Digit Matrix:')
for d in digits_matrix:
    print(d)

steps = 0

print(next_points)
for i in range(len(next_points)):
    while len(next_points) > 0:
        point = next_points[i]
        print('starting point---', point)
        point_symbol = puzzle[point[0]][point[1]]
        point_digit = int(digits_matrix[point[0]][point[1]])
        p_coors = [(point[0], point[1]-1),
                   (point[0], point[1]+1),
                   (point[0]-1, point[1]),
                   (point[0]+1, point[1])]
        p_coors = [coor for coor in p_coors if coor[1] >= 0]
        for coor in p_coors:
            try:
                symbol = puzzle[coor[0]][coor[1]]

                if (coor != point and coor != starting_coor
                        and symbol != '.'
                        and (digits_matrix[coor[0]][coor[1]] == '.'
                             or int(digits_matrix[coor[0]][coor[1]]) < point_digit)):
                    print(coor)
                    if coor == (point[0], point[1]-1):
                        if symbol in ('-', 'L', 'F') and point_symbol in ('-', 'J', '7'):
                            digits_matrix[coor[0]][coor[1]] = str(point_digit + 1)
                            steps += 1
                            next_points.append(coor)
                    elif coor == (point[0], point[1]+1):
                        if symbol in ('-', 'J', '7') and point_symbol in ('-', 'L', 'F'):
                            digits_matrix[coor[0]][coor[1]] = str(point_digit + 1)
                            steps += 1
                            next_points.append(coor)
                    elif coor == (point[0]-1, point[1]):
                        if symbol in ('|', '7', 'F') and point_symbol in ('|', 'L', 'J'):
                            print(point_digit)
                            digits_matrix[coor[0]][coor[1]] = str(point_digit + 1)
                            steps += 1
                            next_points.append(coor)
                    elif coor == (point[0]+1, point[1]):
                        if symbol in ('|', 'L', 'J') and point_symbol in ('|', '7', 'F'):
                            digits_matrix[coor[0]][coor[1]] = str(point_digit + 1)
                            steps += 1
                            next_points.append(coor)
            except IndexError:
                pass
        next_points.pop(i)
        print(next_points)


print('---Result Digit Matrix:')
for d in digits_matrix:
    print(d)

print('---Max Steps:')
print(max([int(d[i]) for i in range(len(d)) 
           for d in digits_matrix if d[i] not in ('S', '.')]))
