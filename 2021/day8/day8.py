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

digits = read_file('digits.txt')
print(find_digits(digits))
