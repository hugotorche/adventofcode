from runs.day8 import init_map

puzzle = '''RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)'''


def test_init_map():
    assert init_map(puzzle) == (['R', 'L'],
                                [['AAA', ['BBB', 'CCC']],
                                 ['BBB', ['DDD', 'EEE']],
                                 ['CCC', ['ZZZ', 'GGG']],
                                 ['DDD', ['DDD', 'DDD']],
                                 ['EEE', ['EEE', 'EEE']],
                                 ['GGG', ['GGG', 'GGG']],
                                 ['ZZZ', ['ZZZ', 'ZZZ']]])
