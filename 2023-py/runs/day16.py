puzzle_1 = r'''.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....'''


def directions(puzzle):
    puzzle = [list(line) for line in puzzle.splitlines()]
    puzzle[0][0] = '>'
    print('BEFORE')
    for p in puzzle:
        print(p)

    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            current_value == puzzle[0]

    print('AFTER')
    for p in puzzle:
        print(p)
    return


print(directions(puzzle_1))
