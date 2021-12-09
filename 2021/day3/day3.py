'''
--- Part One ---
'''

def read_file(filename):
    with open(filename) as my_file:
        bin_nums = my_file.read().splitlines()
    return bin_nums

def convert_binary_to_dec(bin_num):
    ret = 0
    for i in range(12):
        ret += int(bin_num[12-i-1]) * (2**(0+i))
    return ret

def get_power_consumption(report):
    # gamma bits: most common bit in index of all
    # epislon: least common bit in index of all

    num_nums = len(report)
    one_bit_ctr = {}
    for i in range(12):
        one_bit_ctr[i] = 0

    for num in report:
        for i in range(12):
            if num[i] == '1':
                one_bit_ctr[i] += 1

    gamma_bit = ''
    epsilon_bit = ''

    for i in range(12):
        ctr = one_bit_ctr[i]
        # most 1 bits in that idx
        if ctr > (num_nums / 2):
            gamma_bit += '1'
            epsilon_bit += '0'
        else:
            gamma_bit += '0'
            epsilon_bit += '1'

    gamma = convert_binary_to_dec(gamma_bit)
    epsilon = convert_binary_to_dec(epsilon_bit)

    return gamma * epsilon

# diag_report = read_file('report.txt')
# print(get_power_consumption(diag_report)) # 3633500

'''
--- Part Two ---
'''

def most_or_least_common_bit(arr, idx, get_most):
    # error handling small arr or iterating past avail arr elements
    if len(arr) == 0:
        return 'ERROR: empty input on common bit function'
    elif len(arr) == 1:
        return arr[0]
    elif idx >= len(arr[0]):
        return 'ERROR: indexed out of bounds in common bit function'
    else:
        # separate nums into 2 sets to compare lenghs
        ones_set = []
        zeros_set = []

        # separate based on bit of designated idx
        for i in range(len(arr)):
            if arr[i][idx] == '1':
                ones_set.append(arr[i])
            else:
                zeros_set.append(arr[i])

        # ones bit designated mroe than zero bit designated
        if len(ones_set) > len(zeros_set):
            # wanted most common
            if get_most:
                return most_or_least_common_bit(ones_set, idx+1, get_most)
            # wanted least common
            else:
                return most_or_least_common_bit(zeros_set, idx+1, get_most)
        # zeros bit has more
        elif len(ones_set) < len(zeros_set):
            # wanted most common
            if get_most:
                return most_or_least_common_bit(zeros_set, idx+1, get_most)
            # wanted least common
            else:
                return most_or_least_common_bit(ones_set, idx+1, get_most)
        # tie breaker = 1 for oxy, 0 for co2
        else:
            if get_most:
                return most_or_least_common_bit(ones_set, idx+1, get_most)
            else:
                return most_or_least_common_bit(zeros_set, idx+1, get_most)

def get_ratings(report):
    oxy_gen_rating_bit = most_or_least_common_bit(report, 0, True)
    co2_scrb_rating_bit = most_or_least_common_bit(report, 0, False)

    oxy_gen_rating = convert_binary_to_dec(oxy_gen_rating_bit)
    co2_scrb_rating = convert_binary_to_dec(co2_scrb_rating_bit)

    return oxy_gen_rating * co2_scrb_rating

diag_report = read_file('report.txt')
print(get_ratings(diag_report)) # 4550283
