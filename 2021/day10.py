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
    errors = {')': 0, ']': 0, '}': 0, '>': 0}

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

# subsystem = read_file('navigation.txt')
# print(find_corruption(subsystem)) # 316851

'''
--- PART TWO ---
'''

def is_corrupted(line):
    return find_corruption([line]) > 0

def get_closing_score(open_chars):
    score_map = {'(': 1, '[': 2, '{': 3, '<': 4}
    score = 0

    # iterate in reverse order
    for i in range(len(open_chars)):
        char = open_chars[-1-i]
        score = (score * 5) + score_map[char]

    return score

def find_closings(subsystem):
    incompletes = []
    open_char = set(['(', '[', '{', '<'])
    scores = []

    # get incomplete lines only
    for line in subsystem:
        if not is_corrupted(line):
            incompletes.append(line)

    # go through incomplete lines
    for line in incompletes:
        openings = []

        for char in line:
            # track open chars
            if char in open_char:
                openings.append(char)
            # closing needs to match
            else:
                openings = openings[0:-1]

        # get closing score
        scores.append(get_closing_score(openings))

    # find middle score
    num_scores = len(scores)
    mid_num = int(num_scores / 2)
    scores = sorted(scores)
    
    return scores[mid_num]

subsystem = read_file('../aoc-inputs/2021/10.txt')
print(find_closings(subsystem)) # 2182912364
