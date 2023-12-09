from runs.day9 import extrapolate_histories, extrapolate_histories_backwards

puzzle_1 = '''10 13 16 21 30 45'''

puzzle_2 = '''0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45'''


def test_extrapolate_histories():
    assert extrapolate_histories(puzzle_1) == 68
    assert extrapolate_histories(puzzle_2) == 114


def test_extrapolate_histories_backwards():
    assert extrapolate_histories_backwards(puzzle_1) == 5
    assert extrapolate_histories_backwards(puzzle_2) == 2
