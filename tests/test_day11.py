from runs.day11 import expand_puzzle, assign_numbers

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

puzzle_2 = '''
................432....
........435............'''


def test_expansion():
    assert expand_puzzle(puzzle_1) == '''....#........
.........#...
#............
.............
.............
........#....
.#...........
............#
.............
.............
.........#...
#....#.......'''
    assert assign_numbers(puzzle_1) == '''....1........
.........2...
3............
.............
.............
........4....
.5...........
............6
.............
.............
.........7...
8....9.......'''
