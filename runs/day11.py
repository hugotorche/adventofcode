with open('runs/sources/puzzleinput_11.txt', 'r', encoding='utf-8') as puzzleinput:
    puzzle = puzzleinput.read()

puzzle_1 = '''...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
'''


def expand_lines(puzzle_lines):
    lines = []
    for i in range(len(puzzle_lines)):
        current_line = puzzle_lines[i]
        lines.append(current_line)
        if '#' not in current_line:
            lines.append(current_line)

    return lines


def expand_puzzle(puzzle):
    puzzle_lines = expand_lines(puzzle.splitlines())
    puzzle_columns = expand_lines([''.join(i) for i in zip(*puzzle_lines)])

    puzzle_lines = [''.join(i) for i in zip(*puzzle_columns)]
    puzzle = '\n'.join(puzzle_lines)
    return puzzle


def assign_numbers(puzzle):
    expanded_puzzle = expand_puzzle(puzzle).splitlines()
    expanded_list = [[*puzz] for puzz in expanded_puzzle]
    x = 0
    for i in range(len(expanded_list)):
        for j in range(len(expanded_list[i])):
            if expanded_list[i][j] == '#':
                x += 1
                expanded_list[i][j] = str(x)

    expanded_list = [''.join(el) for el in expanded_list]
    expanded_puzzle = '\n'.join(expanded_list)

    return expanded_puzzle


def get_coordinates(puzzle):
    expanded_puzzle = assign_numbers(puzzle).splitlines()
    expanded_list = [[*puzz] for puzz in expanded_puzzle]
    coordinates = {}
    for i in range(len(expanded_list)):
        for j in range(len(expanded_list[i])):
            if expanded_list[i][j] != '.':
                coordinates[expanded_list[i][j]] = [i, j]

    return coordinates


def shortest_paths(puzzle):
    shortest_paths = []
    coordinates = get_coordinates(puzzle)
    keys_list = list(coordinates.keys())

    for i in range(len(keys_list)):
        current_nb = int(keys_list[i])
        for j in range(current_nb, len(keys_list)):
            shortest_path_x = abs(coordinates[keys_list[j]][0] - coordinates[keys_list[i]][0])
            shortest_path_y = abs(coordinates[keys_list[j]][1] - coordinates[keys_list[i]][1])

            shortest_path = shortest_path_x + shortest_path_y
            shortest_paths.append(shortest_path)

    return sum(shortest_paths)


print(shortest_paths(puzzle_1))