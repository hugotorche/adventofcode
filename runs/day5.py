import re


def init_seeds(inputs, mode='default'):

    seeds = re.findall(r'(\d+)', inputs[0])

    if mode == 'ranges':
        range_seeds = []
        for i in range(0, len(seeds), 2):
            current_seed = int(seeds[i])
            next_seed = int(seeds[i+1])
            range_seeds.append([str(current_seed), str(next_seed)])
        seeds = range_seeds
    return seeds


def map_dict(inputs):

    map_dict = {}
    for input in inputs[1:]:
        key_text = input.splitlines()[0].replace(' map:', '')
        value_texts = input.splitlines()[1:]
        for text in value_texts:
            value_list = re.findall(r'(\d+)', text)
            try:
                map_dict[key_text].append(value_list)
            except KeyError:
                map_dict[key_text] = [value_list]

    return map_dict


def min_location(mode='default'):

    # First loop seed by seed
    seeds = init_seeds(inputs, mode=mode)
    locations = []
    for seed in seeds:

        # Loop on each transformation: seed to soil, soil to fertilizer, etc.
        for key, value in map_dict(inputs).items():
            map_number_lists = value

            # For each 3 numbers serie from the mapping: get numbers info
            for number_list in map_number_lists:
                destination_range_start = int(number_list[0])
                source_range_start = int(number_list[1])
                range_length = int(number_list[2])
                source_range_end = source_range_start + range_length
                source_vs_destination = destination_range_start - source_range_start

                # Updating seed accordingly
                seed_int = int(seed)
                if seed_int >= source_range_start and seed_int <= source_range_end:
                    seed = seed + source_vs_destination
                    break
                else:
                    seed = seed_int

        locations.append(seed)

    return min(locations)


with open('runs/sources/puzzleinput_5.txt', 'r', encoding='utf-8') as puzzleinput:
    inputs = puzzleinput.read().split("\n\n")

print(min_location())
