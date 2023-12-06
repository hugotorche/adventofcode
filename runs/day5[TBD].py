import re

inputs = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""
inputs = inputs.split("\n\n")

with open('runs/sources/puzzleinput_5.txt', 'r', encoding='utf-8') as puzzleinput:
    inputs_1 = puzzleinput.read().split("\n\n")


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
    z = 0
    for seed in seeds:
        z += 1
        print((z/len(seeds))*100, '%')
        s_list = []
        for s in [int(seed[0]), int(seed[0]) + int(seed[1])]:
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
                    s_int = int(s)
                    if s_int >= source_range_start and s_int <= source_range_end:
                        s = s + source_vs_destination
                        break
                    else:
                        s = s_int

            s_list.append(s)

            locations.append(s_list)

    return min(locations)


# print(init_seeds(inputs, mode='ranges'))
print(min_location(mode='ranges'))
