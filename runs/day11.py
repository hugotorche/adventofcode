import numpy as np

with open('runs/sources/puzzleinput_11.txt', 'r', encoding='utf-8') as puzzleinput:
    puzzle = puzzleinput.read()


def expand_lines(puzzle_lines):
    coordinates_lines = []
    for i in range(len(puzzle_lines)):
        current_line = puzzle_lines[i]
        if '#' not in current_line:
            coordinates_lines.append(i)

    return coordinates_lines


def expand_path(shortest_path, expand_lines, coef):
    final_expansion = []
    for line in expand_lines:
        if shortest_path >= line:
            final_expansion.append(line)

    return len(final_expansion) * coef


def get_coordinates(puzzle, coef):
    puzzle_lines = puzzle.splitlines()
    coordinates_columns = expand_lines([''.join(i) for i in zip(*puzzle_lines)])
    coordinates_lines = expand_lines(puzzle_lines)
    puzzle_matrix = np.array(list(map(list, puzzle_lines)))
    coordinates = {}

    indices = np.where(puzzle_matrix == '#')
    row_indices, col_indices = indices

    for i in range(len(row_indices)):
        key = f"{i+1}"
        row_indice = row_indices[i] + expand_path(row_indices[i], coordinates_lines, coef)
        col_indice = col_indices[i] + expand_path(col_indices[i], coordinates_columns, coef)
        value = [row_indice, col_indice]
        coordinates[key] = value

    return coordinates


def shortest_paths(puzzle, coef):
    shortest_paths = []
    coordinates = get_coordinates(puzzle, coef)
    keys_list = list(coordinates.keys())

    for i in range(len(keys_list)):
        current_nb = int(keys_list[i])
        for j in range(current_nb, len(keys_list)):
            shortest_path_x = abs(coordinates[keys_list[j]][0] - coordinates[keys_list[i]][0])
            shortest_path_y = abs(coordinates[keys_list[j]][1] - coordinates[keys_list[i]][1])
            shortest_path = shortest_path_x + shortest_path_y
            shortest_paths.append(shortest_path)

    return sum(shortest_paths)


# print('Part 1:', shortest_paths(puzzle, 1))
# print('Part 2:', shortest_paths(puzzle, 999999))
