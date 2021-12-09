'''
--- Part One ---
'''

def read_file(filename):
    nums = []
    boards = []

    with open(filename) as my_file:
        curr_board = []

        for line in my_file:

            # nums not filled yet
            if len(nums) == 0:
                nums = [int(num) for num in line.rstrip().split(',')]

            # get on boards
            else:
                # board line
                if len(line.rstrip()) > 0:
                    curr_board.append([int(num) for num in line.rstrip().split()])
                # empty line
                else:
                    # add accumulated board and refresh current board
                    if len(curr_board) > 0:
                        boards.append(curr_board)
                    curr_board = []

    return nums, boards

# sum of numbers on 2d board
def score_board(board):
    score = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != '*':
                score += board[i][j]
    return score

def find_first_bingo(nums, boards):
    len_bingo = len(boards[0][0]) # length of bingo board
    board_tracker = {} # track progress to bingo for each board row/col
    for i in range(len(boards)):
        board_tracker[i] = {'row': {}, 'col': {}}
        for j in range(len_bingo):
            board_tracker[i]['row'][j] = 0
            board_tracker[i]['col'][j] = 0

    for num in nums:
        for board_idx in range(len(boards)):

            # find marked num
            for row in range(len_bingo):

                # if num on board
                if num in boards[board_idx][row]:
                    col = boards[board_idx][row].index(num)

                    # count progress to bingo
                    board_tracker[board_idx]['row'][row] += 1
                    board_tracker[board_idx]['col'][col] += 1
                    boards[board_idx][row][col] = '*' # later want sum of unmarked nums

                    # check bingo
                    if board_tracker[board_idx]['row'][row] == len_bingo or \
                        board_tracker[board_idx]['col'][col] == len_bingo:

                        return score_board(boards[board_idx]) * num

    return 'ERROR: no bingo found'

bingo_nums = read_file('bingo.txt')[0]
bingo_boards = read_file('bingo.txt')[1]
print(find_first_bingo(bingo_nums, bingo_boards))
