import re


def total_game_ids(games):

    game_ids = []
    for game in games:
        red_matches = re.findall(r"(\d+)\sred", game[0].split(': ')[1])
        max_red = max([int(nb) for nb in red_matches])

        green_matches = re.findall(r"(\d+)\sgreen", game[0].split(': ')[1])
        max_green = max([int(nb) for nb in green_matches])

        blue_matches = re.findall(r"(\d+)\sblue", game[0].split(': ')[1])
        max_blue = max([int(nb) for nb in blue_matches])

        if max_red > 12 or max_green > 13 or max_blue > 14:
            game_id = 0
        else:
            game_id = int(re.sub("[^0-9]", "", game[0].split(': ')[0]))

        game_ids.append(game_id)

    return sum(game_ids)


def total_game_powers(games):

    powers = []
    for game in games:
        red_matches = re.findall(r"(\d+)\sred", game[0].split(': ')[1])
        max_red = max([int(nb) for nb in red_matches])

        green_matches = re.findall(r"(\d+)\sgreen", game[0].split(': ')[1])
        max_green = max([int(nb) for nb in green_matches])

        blue_matches = re.findall(r"(\d+)\sblue", game[0].split(': ')[1])
        max_blue = max([int(nb) for nb in blue_matches])

        power = max_red * max_green * max_blue
        powers.append(power)

    return sum(powers)


with open('runs/sources/puzzleinput_2.txt', 'r', encoding='utf-8') as puzzleinput:
    inputs = puzzleinput.read().splitlines()
    games = [[input] for input in inputs]

print("-----TOTAL SUM: ", total_game_ids(games))
print("-----TOTAL POWER: ", total_game_powers(games))
