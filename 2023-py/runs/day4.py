import re


def cards_points(cards):

    cards_points = []
    for card in cards:
        win_nbs = re.findall(r"(\d+)", card.split('|')[0])[1:]
        nbs = re.findall(r"(\d+)", card.split('|')[1])

        nb_points = 0
        for nb in nbs:
            if nb in win_nbs:
                if nb_points == 0:
                    nb_points += + 1
                else:
                    nb_points = nb_points * 2
            print(nb_points)

        cards_points.append(nb_points)

    return sum(cards_points)


def scratchcards(cards):

    cards_lists = []
    list_length = []

    # Getting cards lists to store multiple copies of same card
    for card in cards:
        card_id = card.split(':')[0].replace(' ', '')
        card_nb = card.split(': ')[1]
        win_nbs = re.findall(r"(\d+)", card_nb.split('|')[0])
        nbs = re.findall(r"(\d+)", card_nb.split('|')[1])
        cards_lists.append({card_id: [{'win_nbs': win_nbs, 'nbs': nbs}]})

    # Iterate through each copy of each card
    for i in range(len(cards_lists)):
        cards_list = (cards_lists[i][f'Card{i+1}'])
        for y in range(len(cards_list)):

            # The x value will allow us to restart process for each copy iteration
            x = i
            for nb in cards_list[y]['nbs']:
                if nb in cards_list[y]['win_nbs']:

                    # For each card item if match we copy the card at match index
                    new_copy = cards_lists[x+1][f'Card{x+2}'][0]
                    try:
                        cards_lists[x+1][f'Card{x+2}'].append(new_copy)
                        x += 1
                    except IndexError:
                        pass

        list_length.append(len(cards_list))

    return sum(list_length)


with open('runs/sources/puzzleinput_4.txt', 'r', encoding='utf-8') as puzzleinput:
    inputs = puzzleinput.read().splitlines()
    games = [[input] for input in inputs]

# print(scratchcards(inputs))
