with open('runs/sources/puzzleinput_8.txt', 'r', encoding='utf-8') as puzzleinput:
    puzzle = puzzleinput.read()

puzzle_3 = '''LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)'''


def init_map(puzzle):
    puzzle = puzzle.replace('(', '').replace(')', '').splitlines()
    instructions = [char for char in puzzle[0]]

    coordinates_keys = [coor.split(' = ')[0] for coor in puzzle[2:]]
    coordinates_values = [coor.split(' = ')[1].split(', ') for coor in puzzle[2:]]
    coordinates = dict(zip(coordinates_keys, coordinates_values))

    return instructions, coordinates


def aaa_to_zzz(puzzle):

    instructions, coordinates = init_map(puzzle)
    steps = 0

    target_keys = [coor for coor in coordinates
                   if coor[2] == 'A'] # ['DFA', 'BLA', 'TGA', 'AAA', 'PQA', 'CQA']
    unique_last = ''.join(set([key[2] for key in target_keys])) # A
    searching_z = True

    while searching_z:
        for i in range(len(instructions)):
            coor_index = 1 if instructions[i] == 'R' else 0
            new_target_keys = []
            for j in range(len(target_keys)):
                key_match = coordinates[target_keys[j]][coor_index]
                new_target_keys.append(key_match)
            target_keys = new_target_keys
            steps += 1
            unique_last = ''.join(sorted([key[2] for key in target_keys]))

            if unique_last == 'ZZZZZ':
                searching_z = False
                break


# print(aaa_to_zzz(puzzle_3))
