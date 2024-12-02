import numpy as np

with open('runs/sources/puzzleinput_14.txt', 'r', encoding='utf-8') as puzzleinput:
    puzzle = puzzleinput.read()

puzzle_1 = '''O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....'''


def init_puzzle(puzzle, direction):

    if direction == 0:
        # To north
        puzzle_matrix = np.array([list(i) for i in zip(*reversed(puzzle))])
    elif direction == 1:
        # to west
        puzzle_matrix = np.array([list(reversed(list(i))) for i in puzzle])
    elif direction == 2:
        # To south
        puzzle_matrix = np.array([list(i) for i in zip(*puzzle)])
    elif direction == 3:
        # to east
        puzzle_matrix = np.array([list(i) for i in puzzle])

    return puzzle_matrix


def get_coordinates(rows, columns):

    coordinates = {}
    for i in range(len(rows)):
        try:
            value = columns[i] + 1
            coordinates[rows[i]+1].append(value)
        except KeyError:
            coordinates[rows[i]+1] = [value]

    return coordinates


def find_zero_n_blocks(puzzle):

    zero_rows, zero_columns = np.where(puzzle == 'O')
    zero_coordinates = get_coordinates(zero_rows, zero_columns)

    block_rows, block_columns = np.where(puzzle == '#')
    block_coordinates = get_coordinates(block_rows, block_columns)

    return zero_coordinates, block_coordinates


def get_load(zero_coordinates, block_coordinates):

    load_per_line = []
    max_load = list(zero_coordinates.keys())[-1]

    for key in list(zero_coordinates.keys()):
        len_zero_range = len(zero_coordinates[key])
        reverse_zero_range = reversed(range(len(zero_coordinates[key])))

        if key in list(block_coordinates.keys()):

            # Loop through reversed values
            for i in reversed(range(len_zero_range)):

                # Set values to max load if no blocking point
                if (max(block_coordinates[key]) < zero_coordinates[key][i]):
                    zero_coordinates[key][i] = list(block_coordinates.keys())[-1]

                else:
                    # Stop to blocking point if any
                    for j in range(len(block_coordinates[key])):
                        if block_coordinates[key][j] > zero_coordinates[key][i]:
                            zero_coordinates[key][i] = block_coordinates[key][j] - 1
                            break

                # Avoiding values overlapping
                if (i != len_zero_range - 1 and
                   zero_coordinates[key][i] >= zero_coordinates[key][i+1]):
                    zero_coordinates[key][i] = zero_coordinates[key][i+1] - 1

        else:
            # If no blocking point in line then enumerate
            zero_coordinates[key] = [max_load - i for i in reverse_zero_range]

        load_per_line.append(sum(zero_coordinates[key]))

    total_load = sum(load_per_line)

    return total_load


def new_grid(zero_coordinates, block_coordinates, direction):

    grid_size = max(max(zero_coordinates), max(block_coordinates))
    grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]

    for key, values in zero_coordinates.items():
        for value in values:
            grid[key - 1][value - 1] = 'O'

    for key, values in block_coordinates.items():
        for value in values:
            grid[key - 1][value - 1] = '#'

    if direction in [0, 1, 2, 3]:
        # To north
        grid = list(reversed(list(map(list, zip(*grid)))))

    return grid


puzzle_1 = list(map(list, puzzle_1.splitlines()))
for i in range(4):
    print(f'{i} -----------')
    puzzle = init_puzzle(puzzle_1, i)
    print(f'START -----------')
    for p in puzzle:
        print(p)
    zero_coordinates, block_coordinates = find_zero_n_blocks(puzzle)
    print(zero_coordinates)
    print(get_load(zero_coordinates, block_coordinates))
    print(f'END -----------')
    for line in new_grid(zero_coordinates, block_coordinates, i):
        print(line)
    puzzle_1 = new_grid(zero_coordinates, block_coordinates, i)