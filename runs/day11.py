import numpy as np

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
            for r in range(1):
                lines.append(current_line)
    return lines


def expand_puzzle(puzzle):
    puzzle_columns = expand_lines([''.join(i) for i in zip(*puzzle.splitlines())])
    print('expand columns ok')
    puzzle_lines = expand_lines([''.join(i) for i in zip(*puzzle_columns)])
    print('expand lines ok')
    return puzzle_lines


def get_coordinates(puzzle):
    expanded_puzzle = expand_puzzle(puzzle)
    expanded_puzzle = np.array(list(map(list, expanded_puzzle)))
    print('puzzle ok')
    coordinates = {}

    indices = np.where(expanded_puzzle == '#')
    row_indices, col_indices = indices

    for i in range(len(row_indices)):
        key = f"{i+1}"
        value = [row_indices[i], col_indices[i]]
        coordinates[key] = value

    print('coordinates done')
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


print(shortest_paths(puzzle))
