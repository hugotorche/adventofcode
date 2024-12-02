with open('runs/sources/puzzleinput_9.txt', 'r', encoding='utf-8') as puzzleinput:
    puzzle = puzzleinput.read()


def extrapolate_histories(puzzle):
    # Initializing histories and next values list
    histories = puzzle.splitlines()
    histories = (h.split() for h in histories)
    next_values_histories = []

    # Looping through histories and getting the differences
    for history in histories:
        last_diffs = []
        last_diffs.append(int(history[-1]))
        diff_sequence = [int(history[i+1])-int(history[i]) for i in range(len(history)-1)]
        while sum(diff_sequence) != 0:
            last_diffs.append(diff_sequence[-1])
            diff_sequence = [int(diff_sequence[i+1])-int(diff_sequence[i])
                             for i in range(len(diff_sequence)-1)]

        # Compiling all next values
        next_value_history = sum(last_diffs)
        next_values_histories.append(next_value_history)

    return sum(next_values_histories)


# print(extrapolate_histories(puzzle))
# 1972648895


def extrapolate_histories_backwards(puzzle):
    # Initializing histories and next values list
    histories = puzzle.splitlines()
    histories = (h.split() for h in histories)
    next_values_histories = []

    # Looping through histories and getting the differences
    for history in histories:
        print(history)
        last_diffs = []
        last_diffs.append(int(history[0]))
        diff_sequence = [int(history[i+1])-int(history[i]) for i in range(len(history)-1)]
        while sum(diff_sequence) != 0:
            last_diffs.append(diff_sequence[0])
            diff_sequence = [int(diff_sequence[i+1])-int(diff_sequence[i])
                             for i in range(len(diff_sequence)-1)]
        last_diffs.append(0)

        # Extrapolating backwards
        last_diffs_reversed = list(reversed(last_diffs))
        last_diffs_backwards = []
        for i in range(len(last_diffs_reversed)-1):
            if i == 0:
                inter_diff = last_diffs_reversed[i+1]-last_diffs_reversed[i]
            else:
                inter_diff = last_diffs_reversed[i+1]-inter_diff
            last_diffs_backwards.append(inter_diff)

        # Compiling all next values
        next_value_history = last_diffs_backwards[-1]
        next_values_histories.append(next_value_history)

    return sum(next_values_histories)


# print(extrapolate_histories_backwards(puzzle))
# 119
