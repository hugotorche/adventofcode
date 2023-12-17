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

with open('runs/sources/puzzleinput_13.txt', 'r', encoding='utf-8') as puzzleinput:
    puzzle_1 = puzzleinput.read()

puzzle_2 = '''#.##..##.
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
#....#..#

.#.##.#.#
.##..##..
.#.##.#..
#......##
#......##
.#.##.#..
.##..##.#

#..#....#
###..##..
.##.#####
.##.#####
###..##..
#..#....#
#..##...#

#.##..##.
..#.##.#.
##..#...#
##...#..#
..#.##.#.
..##..##.
#.#.##.#.'''


def read_input(puzzle):
    puzzle_split = puzzle.split('\n\n')

    return puzzle_split


def find_matching_rows(matrix):
    matching_rows = []

    # Iterate through all pairs of rows
    for row1 in range(len(matrix)):
        for row2 in range(row1 + 1, len(matrix)):
            if matrix[row1] == matrix[row2]:
                matching_rows.append((row1+1, row2+1))

    return sorted(matching_rows, reverse=True)


def find_matching_columns(matrix):
    matching_columns = []

    # Iterate through all pairs of columns
    for col1 in range(len(matrix[0])):
        for col2 in range(col1 + 1, len(matrix[0])):
            if all(row[col1] == row[col2] for row in matrix):
                matching_columns.append((col1+1, col2+1))

    return sorted(matching_columns, reverse=True)


def filter_matches(list_x):
    filtered_pairs = []

    for i in range(len(list_x) - 1):
        a, b = list_x[i]
        c, d = list_x[i + 1]

        if (a == b - 1) and (c == d - 1) and (a == c + 1) and (b == d - 1):
            filtered_pairs.append((a, b))
            filtered_pairs.append((c, d))

    filtered_pairs = sorted(list(set(filtered_pairs)), reverse=True)
    return filtered_pairs


def get_final_match(matrix):
    print('FIRST ROWS', find_matching_rows(matrix))
    print('FIRST COLUMNS', find_matching_columns(matrix))
    try:
        if (filter_matches(find_matching_rows(matrix))[-1][1] == len(matrix)
                or filter_matches(find_matching_rows(matrix))[0][0] == 1
                or filter_matches(find_matching_rows(matrix))[-1][0] == 1):
            matching_rows = [filter_matches(find_matching_rows(matrix))[0]]
    except IndexError:
        try:
            if (filter_matches(find_matching_rows(matrix))[-1][1] == len(matrix)
                or filter_matches(find_matching_rows(matrix))[0][0] == 1
                or filter_matches(find_matching_rows(matrix))[-1][0] == 1):
                matching_rows = []
                for i in range(len(find_matching_rows(matrix))):
                    a, b = find_matching_rows(matrix)[i]
                    if (b == a + 1):
                        matching_rows.append((a, b))
        except IndexError:
            matching_rows = [(0, 0)]
    print('MATCHING ROWS----:', matching_rows)

    try:
        matching_columns = [filter_matches(find_matching_columns(matrix))[0]]
    except IndexError:
        try:
            matching_columns = []
            for i in range(len(find_matching_columns(matrix))):
                a, b = find_matching_columns(matrix)[i]
                if (b == a + 1):
                    matching_columns.append((a, b))
        except IndexError:
            matching_columns = [(0, 0)]

    print('MATCHING COLUMNS----:', matching_columns)

    match_rows = 0
    match_columns = 0

    match_rows = sum([mr[0] for mr in matching_rows]) * 100
    match_columns = sum([mc[0] for mc in matching_columns])

    return (match_rows + match_columns)


puzzle_split = read_input(puzzle_2)
matches = []
for i in range(len(puzzle_split)):
    puzzle_matrix = [list(puzz) for puzz in puzzle_split[i].splitlines()]
    for p in puzzle_matrix:
        print(p)
    print('FINAL---', get_final_match(puzzle_matrix))
    matches.append(get_final_match(puzzle_matrix))


print(sum(matches))
