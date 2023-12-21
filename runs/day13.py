with open('runs/sources/puzzleinput_13.txt', 'r', encoding='utf-8') as puzzleinput:
    puzzle_1 = puzzleinput.read()

puzzle = '''#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#'''


def read_input(puzzle):
    puzzle_split = puzzle.split('\n\n')

    return puzzle_split


def find_matching_rows(matrix):

    matching_rows = []
    for row1 in range(len(matrix)):
        for row2 in range(row1 + 1, len(matrix)):
            if matrix[row1] == matrix[row2]:
                matching_rows.append((row1+1, row2+1))

    reflexion = []
    for i in range(len(matching_rows)):
        a, b = matching_rows[i]
        if a == b - 1:
            reflexion.append((a, b))
            break

    return reflexion


def find_matching_columns(matrix):

    matching_columns = []
    for col1 in range(len(matrix[0])):
        for col2 in range(col1 + 1, len(matrix[0])):
            if all(row[col1] == row[col2] for row in matrix):
                matching_columns.append((col1+1, col2+1))

    reflexion = []
    for i in range(len(matching_columns)):
        a, b = matching_columns[i]
        if a == b - 1:
            reflexion.append((a, b))
            break

    return reflexion


def get_final_match(matrix):
    matching_rows = find_matching_rows(matrix)
    matching_columns = find_matching_columns(matrix)

    match = 0
    if len(matching_columns) > 0:
        match += [mc[0] for mc in matching_columns][0]

    if len(matching_rows) > 0:
        match += [mr[0] for mr in matching_rows][0] * 100

    return match


puzzle_split = read_input(puzzle_1)
matches = []
for i in range(len(puzzle_split)):
    puzzle_matrix = [list(puzz) for puzz in puzzle_split[i].splitlines()]
    matches.append(get_final_match(puzzle_matrix))


print(sum(matches))