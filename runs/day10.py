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


def digits_matrix(puzzle):
    digits_puzzle_re = re.sub('[L|J|7|F|-]', '.', puzzle).replace('|', '.')
    digits_matrix = [list(puzzle) for puzzle in digits_puzzle_re.splitlines()]

    return digits_matrix


def starting_point(puzzle):
    lines = len(puzzle)
    columns = len(puzzle[0])

    for i in range(lines):
        for j in range(columns):
            if puzzle[i][j] == 'S':
                starting_coor = (i, j)
                return starting_coor


def first_pipe(puzzle, starting_coor, digits_matrix):
    next_points = [starting_coor]

    while len(next_points) > 0:
        for i in range(len(next_points)):
            point = next_points[i]
            point_symbol = puzzle[point[0]][point[1]]
            point_digit = 0 if point_symbol == 'S' else int(digits_matrix[point[0]][point[1]])
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
                            and digits_matrix[coor[0]][coor[1]] == '.'):
                        if coor == (point[0], point[1]-1):
                            if symbol in ('-', 'L', 'F') and point_symbol in ('S', '-', 'J', '7'):
                                digits_matrix[coor[0]][coor[1]] = str(point_digit + 1)
                                next_points.append(coor)
                        elif coor == (point[0], point[1]+1):
                            if symbol in ('-', 'J', '7') and point_symbol in ('S', '-', 'L', 'F'):
                                digits_matrix[coor[0]][coor[1]] = str(point_digit + 1)
                                next_points.append(coor)
                        elif coor == (point[0]-1, point[1]):
                            if symbol in ('|', '7', 'F') and point_symbol in ('S', '|', 'L', 'J'):
                                past_digit = 0 if '.' else int(digits_matrix[coor[0]][coor[1]])
                                digits_matrix[coor[0]][coor[1]] = str(point_digit + 1 + past_digit)
                                next_points.append(coor)
                        elif coor == (point[0]+1, point[1]):
                            if symbol in ('|', 'L', 'J') and point_symbol in ('S', '|', '7', 'F'):
                                digits_matrix[coor[0]][coor[1]] = str(point_digit + 1)
                                next_points.append(coor)
                except IndexError:
                    pass

            next_points.pop(i)
            print(next_points)

    return digits_matrix


init_digits_matrix = digits_matrix(puzzle_4)
puzzle = puzzle_4.splitlines()
starting_point = starting_point(puzzle)
final_digits_matrix = first_pipe(puzzle, starting_point, init_digits_matrix)

maxs = []
for matrice in final_digits_matrix:
    print(matrice)
    maxs.append(max([m for m in matrice if m != 'S']))

maxs = [int(m) for m in maxs if m != '.']
print(max(maxs))
