'''
--- PART ONE ---
'''

def read_file(filename):
    dots = []
    folds = []
    max_x = 0
    max_y = 0

    with open(filename) as my_file:
        for line in my_file:
            line = line.rstrip()

            # if dot
            if ',' in line:
                line_split = line.split(',')
                line_x = int(line_split[0])
                line_y = int(line_split[1])

                # max x, y
                if line_x > max_x:
                    max_x = line_x
                if line_y > max_y:
                    max_y = line_y

                dots.append((line_x, line_y))

            # if fold instructions
            if 'fold' in line:
                fold_dir = line.split()[2]
                fold_split = fold_dir.split('=')
                folds.append((fold_split[0], int(fold_split[1])))

    return dots, folds, (max_x, max_y)

def init_grid(max_x, max_y):
    grid = []

    for y in range(max_y+1):
        row = []
        for x in range(max_x+1):
            row.append('.')
        grid.append(row)

    return grid

def fill_grid(grid, dots):
    for dot in dots:
        grid[dot[1]][dot[0]] = '#'
    return grid

def count_dots(grid):
    num_dots = 0
    grid_length = len(grid)
    grid_width = len(grid[0])

    for i in range(grid_length):
        for j in range(grid_width):
            if grid[i][j] == '#':
                num_dots += 1

    return num_dots

def fold_dots(dots, folds, max):
    max_x = max[0]
    max_y = max[1]

    grid = init_grid(max_x, max_y)
    grid = fill_grid(grid, dots)

    # for fold in folds[0:1]: # limits for part 1
    for fold in folds:
        dir = fold[0]
        pos = fold[1]

        # fold LEFT
        if dir == 'x':
            diff = max_x+1 - pos
            for i in range(diff):
                for j in range(max_y+1):
                    if grid[j][pos+i] == '#':
                        grid[j][pos-i] = '#'
            for row_num in range(max_y+1):
                grid[row_num] = grid[row_num][0:pos]

        # fold UP
        elif dir == 'y':
            diff = max_y+1 - pos
            for i in range(diff):
                for j in range(max_x+1):
                    if grid[pos+i][j] == '#':
                        grid[pos-i][j] = '#'
            grid = grid[0:pos]

        max_x = len(grid[0])-1
        max_y = len(grid)-1

    return grid

def num_dots(dots, folds, max):
    return count_dots(fold_dots(dots, folds, max))

dots, folds, max = read_file('instructions.txt')
# print(num_dots(dots, folds, max)) # 755
print(fold_dots(dots, folds, max)) # BLKJRBAG
