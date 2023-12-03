import re


def gear_ratios(inputs):

    # Get all unique symbols from the puzzle: $*#-%@/&+=
    symbols = []
    for input in inputs:
        input = re.sub(r'[0-9]+', '', input)
        input = re.sub(r'[.]+', '', input)
        input = "".join(set(input))
        symbols.append(input)

    symbols = "".join(set([symbol for symbol in symbols]))
    symbols = "".join(set(symbols))

    # Transform puzzle into 2 dict including objects & positions: for numbers and symbols
    nb_dict = {}
    sb_dict = {}
    for input in inputs:
        input_index = inputs.index(input)
        nb_list = []
        for nb in re.finditer(r"(\d+)", input):
            nb_list.append({nb.group(): {'start': nb.start()-1, 'end': nb.end()}})
        nb_dict[input_index] = nb_list
        sb_list = []
        for sb in re.finditer(r"([-|"+'|'.join(symbols)+r"]+)", input):
            sb_list.append({sb.group(): sb.start()})
        sb_dict[input_index] = sb_list

    numbers_to_keep = []

    # For each line we get the numbers and all the symbols from line -1 to line +1
    for key, value in nb_dict.items():
        line_nbs = value
        if sb_dict.get(key-1) is None:
            all_sbs = sb_dict.get(key) + sb_dict.get(key+1)
        elif sb_dict.get(key+1) is None:
            all_sbs = sb_dict.get(key-1) + sb_dict.get(key)
        else:
            all_sbs = sb_dict.get(key-1) + sb_dict.get(key) + sb_dict.get(key+1)

        # For each number in the current line we get its starting and ending position
        for nb in line_nbs:
            for key, value in nb.items():
                nb_int = int(key)
                nb_position_start = value.get('start')
                nb_position_end = value.get('end')

                # For all symbols we check if the symbol position matches with the number position
                match_count = 0
                for sb in all_sbs:
                    for key, value in sb.items():
                        sb_index = value
                        if (sb_index >= nb_position_start
                                and sb_index <= nb_position_end):
                            match_count += 1

                # We only keep the matched numbers for final sum up
                if match_count > 0:
                    numbers_to_keep.append(nb_int)

    return sum(numbers_to_keep)


with open('runs/sources/puzzleinput_3.txt', 'r', encoding='utf-8') as puzzleinput:
    inputs = puzzleinput.read().splitlines()

print(gear_ratios(inputs))
