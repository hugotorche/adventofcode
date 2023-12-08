with open('runs/sources/puzzleinput_8.txt', 'r', encoding='utf-8') as puzzleinput:
    puzzle = puzzleinput.read()


def init_map(puzzle):
    puzzle = puzzle.replace('(', '').replace(')', '').splitlines()
    instructions = [char for char in puzzle[0]]

    coordinates_keys = [coor.split(' = ')[0] for coor in puzzle[2:]]
    coordinates_values = [coor.split(' = ')[1].split(', ') for coor in puzzle[2:]]
    coordinates = dict(zip(coordinates_keys, coordinates_values))

    print(coordinates)

    return instructions, coordinates


def aaa_to_zzz(puzzle):
    instructions, coordinates = init_map(puzzle)
    steps = 0
    target_key = 'AAA'
    while target_key != 'ZZZ':
        for i in range(len(instructions)):
            coordinate_index = 1 if instructions[i] == 'R' else 0
            target_key = coordinates[target_key][coordinate_index]
            steps += 1

    return steps


print(aaa_to_zzz(puzzle))
