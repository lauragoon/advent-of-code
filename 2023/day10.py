NORTH = (1,0)
SOUTH = (-1,0)
WEST = (0,-1)
EAST = (0,1)

PIPES = {
    '|': [NORTH, SOUTH],
    '-': [WEST, EAST],
    'L': [NORTH, EAST],
    'J': [NORTH, WEST],
    '7': [SOUTH, WEST],
    'F': [SOUTH, EAST],
}


def process_file():
    lines = []
    with open('../aoc-inputs/2023/10.txt') as f:
        for line in f:
            lines.append(list(line.rstrip()))
    return lines

def get_starting_coords(lines):
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == 'S':
                return i,j
            
def get_starting_dir(lines, start_row, start_col):
    pass

def go_around_loop(lines):
    start_row, start_col = get_starting_coords(lines)
    end_loop_yet = False
    loop_length = 0
    next_dir = get_starting_dir(lines, start_row, start_col)

    while not end_loop_yet:


def main():
    lines = process_file()

    print(lines)


# ------ RUN SOLUTION ------
main()   # 2075724761, 1072 # TODO: input mutable/changes per run

