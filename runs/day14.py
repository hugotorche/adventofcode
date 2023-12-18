import numpy as np

puzzle = '''O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....'''


def init_puzzle(puzzle):

    puzzle_matrix = list(map(list, puzzle.splitlines()))
    puzzle_matrix = np.array([list(i) for i in zip(*reversed(puzzle_matrix))])

    return puzzle_matrix


def get_coordinates(rows, columns):

    coordinates = {}
    for i in range(len(rows)):
        try:
            value = columns[i] + 1
            coordinates[rows[i]].append(value)
        except KeyError:
            coordinates[rows[i]] = [value]

    return coordinates


def find_zero_n_blocks(puzzle):

    puzzle_matrix = init_puzzle(puzzle)
    zero_rows, zero_columns = np.where(puzzle_matrix == 'O')
    zero_coordinates = get_coordinates(zero_rows, zero_columns)

    block_rows, block_columns = np.where(puzzle_matrix == '#')
    block_coordinates = get_coordinates(block_rows, block_columns)

    return f'{zero_coordinates}\n{block_coordinates}'


print(find_zero_n_blocks(puzzle))
