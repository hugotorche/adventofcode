from runs.day7 import init_inputs, score_hands

inputs_1 = '''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483'''

inputs_2 = '''KAAAA 92
TAAAA 686'''


def test_init_inputs():
    assert init_inputs(inputs_1) == [['32T3K', '765'],
                                     ['T55J5', '684'],
                                     ['KK677', '28'],
                                     ['KTJJT', '220'],
                                     ['QQQJA', '483']]
    assert init_inputs(inputs_2) == [['KAAAA', '92'],
                                     ['TAAAA', '686']]


def test_score_hands():
    assert score_hands(inputs_1) == 6440
    assert score_hands(inputs_2) == 870
