def process_file():
    lines = []
    with open('../aoc-inputs/2023/01.txt') as f:
        lines = f.read().splitlines()
    return lines

# new function for Part 2
def process_alpha_digits(lines):
    alpha_digit_map = {
        'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    new_lines = []
    for line in lines:
        new_line = line
        for alpha_digit in alpha_digit_map.keys():
            new_line = new_line.replace(alpha_digit, alpha_digit[0] + str(alpha_digit_map[alpha_digit]) + alpha_digit[-1])   # don't replace border letters, can contribute to next number (e.g. eightwo), but don't need more than that bc look spelling
        new_lines.append(new_line)
    return new_lines

def strip_alpha(lines):
    new_lines = []
    for line in lines:
        num_str = ''
        for ch in range(len(line)):
            if line[ch].isdigit():
                num_str += line[ch]
        new_lines.append(num_str)
    return new_lines

def strip_extra_digits(lines):
    new_lines = []
    for line in lines:
        if len(line) == 2:
            new_lines.append(line)
        elif len(line) == 1:
            new_lines.append(line[0] + line[0])
        else:
            new_lines.append(line[0] + line[-1])
    return new_lines

def sum_calibration_nums(lines):
    ret_sum = 0
    for line in lines:
        ret_sum += int(line)
    return ret_sum

def main():
    alphanum_lines = process_file()
    new_alphanum_lines = process_alpha_digits(alphanum_lines) # new for part 2
    num_lines = strip_alpha(new_alphanum_lines)
    final_lines = strip_extra_digits(num_lines)
    ans = sum_calibration_nums(final_lines)
    
    print(ans)


# ------ RUN SOLUTION ------
main()   # 55386, 54824
