from runs.day11 import shortest_paths

puzzle = '''...#......
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


def test_shortest_paths():
    assert shortest_paths(puzzle, 1) == 374
    assert shortest_paths(puzzle, 9) == 1030
    assert shortest_paths(puzzle, 99) == 8410
