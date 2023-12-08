from runs.day8 import init_map, aaa_to_zzz

puzzle_1 = '''RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)'''

puzzle_2 = '''LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)'''


def test_init_map():
    assert init_map(puzzle_1) == (['R', 'L'],
                                {'AAA': ['BBB', 'CCC'],
                                 'BBB': ['DDD', 'EEE'],
                                 'CCC': ['ZZZ', 'GGG'],
                                 'DDD': ['DDD', 'DDD'],
                                 'EEE': ['EEE', 'EEE'],
                                 'GGG': ['GGG', 'GGG'],
                                 'ZZZ': ['ZZZ', 'ZZZ']})


def test_aaa_to_zzz():
    assert aaa_to_zzz(puzzle_1) == 2
    assert aaa_to_zzz(puzzle_2) == 6
