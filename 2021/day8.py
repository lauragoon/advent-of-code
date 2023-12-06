'''
--- PART ONE ---
'''

def read_file(filename):
    lines = []

    with open(filename) as my_file:
        for line in my_file:
            line_split = line.split('|')
            lines.append((line_split[0].split(), line_split[1].split()))

    return lines

def find_digits(digits):
    num = 0
    want_len = [2, 4, 3, 7]

    for line in digits:
        for digit in line[1]:
            if len(digit) in want_len:
                num += 1

    return num

# digits = read_file('digits.txt')
# print(find_digits(digits)) # 330

'''
--- PART TWO ---
'''

def decipher_all_digits(digits):
    output_sum = 0

    # decipher digits for each line
    for line in digits:
        signal_digit_dict = {}
        digit_signal_dict = {}
        grouped_signals = {5: [], 6: []} # group ambiguous digits
        
        # get unique signals
        signals = line[0]

        # get obvious digits out of way
        for signal in signals:
            if len(signal) == 2:
                signal_digit_dict[signal] = 1
                digit_signal_dict[1] = signal
            elif len(signal) == 4:
                signal_digit_dict[signal] = 4
                digit_signal_dict[4] = signal
            elif len(signal) == 3:
                signal_digit_dict[signal] = 7
                digit_signal_dict[7] = signal
            elif len(signal) == 7:
                signal_digit_dict[signal] = 8
                digit_signal_dict[8] = signal
            else:
                grouped_signals[len(signal)].append(signal)

        # find 9
        four_set = set(list(digit_signal_dict[4]))
        seven_set = set(list(digit_signal_dict[7]))
        for signal in grouped_signals[6]:
            signal_set = set(list(signal))
            if len(list(signal_set.difference(four_set.union(seven_set)))) == 1:
                signal_digit_dict[signal] = 9
                digit_signal_dict[9] = signal
                grouped_signals[6].remove(signal)
                break

        # find 2
        nine_set = set(list(digit_signal_dict[9]))
        for signal in grouped_signals[5]:
            signal_set = set(list(signal))
            if signal_set.union(nine_set) != nine_set:
                signal_digit_dict[signal] = 2
                digit_signal_dict[2] = signal
                grouped_signals[5].remove(signal)
                break

        # find 5
        two_set = set(list(digit_signal_dict[2]))
        eight_set = set(list(digit_signal_dict[8]))
        for signal in grouped_signals[5]:
            signal_set = set(list(signal))
            if signal_set.union(two_set) == eight_set:
                signal_digit_dict[signal] = 5
                digit_signal_dict[5] = signal
                grouped_signals[5].remove(signal)
                break

        # get 3
        signal_digit_dict[grouped_signals[5][0]] = 3
        digit_signal_dict[3] = grouped_signals[5][0]

        # find 6
        one_set = set(list(digit_signal_dict[1]))
        for signal in grouped_signals[6]:
            signal_set = set(list(signal))
            if signal_set.union(one_set) == eight_set:
                signal_digit_dict[signal] = 6
                digit_signal_dict[6] = signal
                grouped_signals[6].remove(signal)
                break

        # get 0
        signal_digit_dict[grouped_signals[6][0]] = 0
        digit_signal_dict[0] = grouped_signals[6][0]

        # decipher output
        output = line[1]
        output_num = ''
        for sig in output:

            # iterate bc sets are unhashable
            for key in signal_digit_dict.keys():
                if set(list(key)) == set(list(sig)):
                    output_num += str(signal_digit_dict[key])
                    break

        output_sum += int(output_num)

    return output_sum


digits = read_file('../aoc-inputs/2021/08.txt')
print(decipher_all_digits(digits)) # 1010472
