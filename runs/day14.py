import numpy as np

with open('runs/sources/puzzleinput_14.txt', 'r', encoding='utf-8') as puzzleinput:
    puzzle_1 = puzzleinput.read()

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
            coordinates[rows[i]+1].append(value)
        except KeyError:
            coordinates[rows[i]+1] = [value]

    return coordinates


def find_zero_n_blocks(puzzle):

    puzzle_matrix = init_puzzle(puzzle)
    zero_rows, zero_columns = np.where(puzzle_matrix == 'O')
    zero_coordinates = get_coordinates(zero_rows, zero_columns)

    block_rows, block_columns = np.where(puzzle_matrix == '#')
    block_coordinates = get_coordinates(block_rows, block_columns)

    return zero_coordinates, block_coordinates


def get_load(puzzle):

    zero_coordinates, block_coordinates = find_zero_n_blocks(puzzle)
    load_per_line = []
    print(zero_coordinates)
    print(block_coordinates)

    for key in list(zero_coordinates.keys()):
        if key in list(block_coordinates.keys()):

            # See if no blocking points in the current line
            if max(block_coordinates[key]) < min(zero_coordinates[key]):
                zero_coordinates[key] = [list(block_coordinates.keys())[-1] - i
                                         for i in reversed(range(len(zero_coordinates[key])))]
            else:
                # Loop through reversed values
                for i in reversed(range(len(zero_coordinates[key]))):
                    # Set last values to max load if no blocking point
                    if (i == 0
                       and max(block_coordinates[key]) < zero_coordinates[key][i]):
                        zero_coordinates[key][i] = list(block_coordinates.keys())[-1]

                    else:
                        # Stop to blocking point if any
                        for j in range(len(block_coordinates[key])):
                            if block_coordinates[key][j] > zero_coordinates[key][i]:
                                zero_coordinates[key][i] = block_coordinates[key][j] - 1
                                break

                        # Avoiding zero values overlapping
                        if (i != len(zero_coordinates[key]) - 1 and
                           zero_coordinates[key][i] >= zero_coordinates[key][i+1]):
                            zero_coordinates[key][i] = zero_coordinates[key][i+1] - 1

        else:
            # If no blocking point in line then enumerate
            zero_coordinates[key] = [list(block_coordinates.keys())[-1] - i
                                     for i in reversed(range(len(zero_coordinates[key])))]

        load_per_line.append(sum(zero_coordinates[key]))

    total_load = sum(load_per_line)

    return total_load, zero_coordinates


print(get_load(puzzle))
