import re
import numpy as np


def gear_ratios_p2(inputs):

    # Transform puzzle into 2 dict including objects positions: for numbers and * symbols
    nb_dict = {}
    sb_dict = {}
    for input in inputs:
        input_index = inputs.index(input)
        nb_list = []
        for nb in re.finditer(r"(\d+)", input):
            nb_list.append({nb.group(): {'start': nb.start()-1, 'end': nb.end()}})
        nb_dict[input_index] = nb_list
        sb_list = []
        for sb in re.finditer(r"([*]+)", input):
            sb_list.append({sb.group(): sb.start()})
        sb_dict[input_index] = sb_list

    # For each line we get the numbers and all the * symbols from line -1 to line +1
    # Add-on vs P1: we keep symbol line number it will help to feed stars matches
    stars_matches = {}

    for key, value in nb_dict.items():
        line_nbs = value
        if sb_dict.get(key-1) is None:
            all_sbs = {key: sb_dict.get(key)} | {key+1: sb_dict.get(key+1)}
        elif sb_dict.get(key+1) is None:
            all_sbs = {key-1: sb_dict.get(key-1)} | {key: sb_dict.get(key)}
        else:
            all_sbs = {key-1: sb_dict.get(key-1)} | {key: sb_dict.get(key)} | {key+1: sb_dict.get(key+1)}

        # For each number in the current line we get its starting and ending position
        for nb in line_nbs:
            for key, value in nb.items():
                nb_int = int(key)
                nb_position_start = value.get('start')
                nb_position_end = value.get('end')

                # For all * symbols we check if the symbol position matches the number position
                stars_match = {}
                for key, value in all_sbs.items():
                    line_sbs = key
                    sbs = value
                    if len(sbs) > 0:
                        for sb in sbs:
                            sbs_val = sb
                            for key, value in sbs_val.items():
                                sb_index = value
                                if (sb_index >= nb_position_start
                                        and sb_index <= nb_position_end):

                                    # We collect all matching numbers per star index and star line
                                    stars_match[f'{line_sbs}'] = {f'*{sb_index}': [nb_int]}
                                    try:
                                        stars_matches[f'{line_sbs}'][f'*{sb_index}'].append(nb_int)
                                    except KeyError:
                                        try:
                                            stars_matches[f'{line_sbs}'][f'*{sb_index}'] = [nb_int]
                                        except KeyError:
                                            stars_matches[f'{line_sbs}'] = {f'*{sb_index}': [nb_int]}

    # We only keep stars with 2 matching numbers and multiply their numbers
    numbers_to_keep = []
    for key, value in stars_matches.items():
        sub_dict = value
        for key, value in sub_dict.items():
            if len(value) == 2:
                numbers_to_keep.append(np.prod(value))

    return sum(numbers_to_keep)


with open('runs/sources/puzzleinput_3.txt', 'r', encoding='utf-8') as puzzleinput:
    inputs = puzzleinput.read().splitlines()

# print(gear_ratios_p2(inputs))
