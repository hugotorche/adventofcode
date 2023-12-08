puzzle = '''RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)'''


def init_map(puzzle):
    puzzle = puzzle.splitlines()
    instructions = [char for char in puzzle[0]]
    coordinates = [coor.split(' = ') for coor in puzzle[2:]]

    for coordinate in coordinates:
        coordinate[1] = coordinate[1].replace('(', '').replace(')', '')
        coordinate[1] = coordinate[1].split(', ')

    return instructions, coordinates

print(init_map(puzzle))
