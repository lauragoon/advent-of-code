'''
--- PART ONE ---
'''

def read_file(filename):
    lines = []

    with open(filename) as my_file:
        for line in my_file:
            lines.append(list(line.rstrip()))

    return lines

def find_corruption(subsystem):
    open_char = set(['(', '[', '{', '<'])
    close_open_dict = {')':'(', ']':'[', '}':'{', '>':'<'}
    errors = {')': 0, ']': 0, '}': 0, '>':0}

    for line in subsystem:
        openings = []

        for char in line:
            # track open chars
            if char in open_char:
                openings.append(char)
            
            # closing needs to match
            else:
                # invalid closing
                if close_open_dict[char] != openings[-1]:
                    errors[char] += 1
                    break
                else:
                    openings = openings[0:-1]

    return (errors[')'] * 3) + (errors[']'] * 57) + (errors['}'] * 1197) + (errors['>'] * 25137)

subsystem = read_file('navigation.txt')
print(find_corruption(subsystem)) # 316851
