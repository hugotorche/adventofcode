import re


def total_calibration(inputs):

    calibration = []
    for input in inputs:

        print('-----------INPUT:', input)
        words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        words_matches = []
        digits_matches = []

        # re finditer finds all non-overlapping matches from lists
        for word in words:
            digit = str(words.index(word) + 1)

            for match in re.finditer(word, input):
                words_matches.extend([[digit, match.start()]])

            for match in re.finditer(digit, input):
                digits_matches.extend([[digit, match.start()]])

        # we compile matches and sort them to get first and last ones
        all_matches = words_matches + digits_matches
        all_matches_sorted = sorted(all_matches, key=lambda x: x[1])
        print('matches:', all_matches_sorted)

        first_last_digits = all_matches_sorted[0][0] + all_matches_sorted[-1][0]
        print('calibration:', first_last_digits)
        calibration.append(int(first_last_digits))

    total_calibration = sum(calibration)

    return total_calibration


with open('runs/sources/puzzleinput.txt', 'r', encoding='utf-8') as puzzleinput:
    inputs = puzzleinput.read().splitlines()

print('-----------TOTAL CALIBRATION:', total_calibration(inputs))
