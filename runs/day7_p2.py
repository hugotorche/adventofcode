with open('runs/sources/puzzleinput_7.txt', 'r', encoding='utf-8') as puzzleinput:
    inputs = puzzleinput.read()


def init_inputs(inputs):

    inputs = inputs.splitlines()
    inputs = [input.split(' ') for input in inputs]
    return inputs


def translate_hands(inputs):

    inputs = init_inputs(inputs)
    cards_refs = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
    inputs_cards = []

    for input in inputs:

        cards = [[x, input[0].count(x)] for x in set(input[0])]

        if input[0] != 'JJJJJ':
            max_index = max(range(len(cards)),
                            key=lambda i: cards[i][1] if cards[i][0] != 'J' else 0)
            j_index = [cards.index(cards[i])
                       for i in range(0, len(cards)) if cards[i][0] == 'J']

            for index in j_index:
                cards[max_index][1] += cards[index][1]
                cards.pop(index)

        for i in range(0, len(cards)):
            card_val = cards[i][1]
            cards[i] = [card_val]

        for i in range(5):
            try:
                sorted_cards = sorted(cards, reverse=True)
            except IndexError:
                pass

        encoded_hand = [cards_refs.index(x) for x in input[0]]
        inputs_cards.append({input[0]: {'bid': input[1],
                                        'cards': sorted_cards,
                                        'encoding': encoded_hand}})

    return inputs_cards


def sort_hands(inputs):

    hands = translate_hands(inputs)
    print('translate_hands--', hands)
    for i in range(1000):
        try:
            sorted_hands = sorted(hands,
                                  key=lambda x: (x[list(x.keys())[0]]['cards'],
                                                 x[list(x.keys())[0]]['encoding']))
        except IndexError:
            pass

    return sorted_hands


def score_hands(inputs):

    hands = sort_hands(inputs)
    print('sort_hands--', hands)
    total_winnings = []
    for i in range(len(hands)):
        rank = i + 1
        bid = int(hands[i][list(hands[i].keys())[0]]['bid'])
        winnings = bid * rank
        total_winnings.append(winnings)

    return sum(total_winnings)


print(score_hands(inputs))
