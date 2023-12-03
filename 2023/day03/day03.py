def process_file():
    lines = []
    with open('engine.txt') as f:
        lines = f.read().splitlines()
    arr = []
    for line in lines:
            arr.append(list(line))
    return arr

def is_symbol(ch):
    return not ch.isdigit() and ch != '.'

def get_entire_number(engine_arr, i, j):
    num_str = engine_arr[i][j]
    end_of_num_yet = False
    temp_j = j-1
    while not end_of_num_yet and temp_j >= 0:
        if engine_arr[i][temp_j].isdigit():
            num_str = engine_arr[i][temp_j] + num_str
            temp_j -= 1
        else:
            end_of_num_yet = True
    end_of_num_yet = False
    temp_j = j+1
    while not end_of_num_yet and temp_j < len(engine_arr[0]):
        if engine_arr[i][temp_j].isdigit():
            num_str += engine_arr[i][temp_j]
            temp_j += 1
        else:
            end_of_num_yet = True
    return int(num_str), temp_j

def get_part_numbers(engine_arr):
    part_nums = []

    for i in range(len(engine_arr)): # up down
        j = 0
        while j < len(engine_arr[0]): # left right

            if engine_arr[i][j].isdigit():
                if (i < len(engine_arr)-1 and is_symbol(engine_arr[i+1][j]))\
                    or (j < len(engine_arr[0])-1 and is_symbol(engine_arr[i][j+1]))\
                    or (i < len(engine_arr)-1 and j < len(engine_arr[0])-1 and is_symbol(engine_arr[i+1][j+1]))\
                    or (i > 0 and is_symbol(engine_arr[i-1][j]))\
                    or (j > 0 and is_symbol(engine_arr[i][j-1]))\
                    or (i > 0 and j > 0 and is_symbol(engine_arr[i-1][j-1]))\
                    or (i < len(engine_arr)-1 and j > 0 and is_symbol(engine_arr[i+1][j-1]))\
                    or (j < len(engine_arr[0])-1 and i > 0 and is_symbol(engine_arr[i-1][j+1])):

                    entire_num_details = get_entire_number(engine_arr,i,j)
                    part_nums.append(entire_num_details[0])
                    j = entire_num_details[1]

                else:
                    j += 1
            else:
                j += 1
                

    return part_nums

def get_sum_part_numbers(part_nums):
    ret_sum = 0
    for num in part_nums:
        ret_sum += num
    return ret_sum

def get_possible_gear_ratio_or_none(engine_arr, row_num, col_num):
    adj_nums = []

    for i in range(row_num-1,row_num+2):
        if i >= 0 and i < len(engine_arr):
            j = col_num-1
            while j < col_num+2:
                if j > 0 and j < len(engine_arr[0]):
                    
                    if engine_arr[i][j].isdigit():
                        entire_num_details = get_entire_number(engine_arr,i,j)
                        adj_nums.append(entire_num_details[0])
                        j = entire_num_details[1]

                    else:
                        j += 1
                else:
                    j += 1

    print(adj_nums)

    if len(adj_nums) == 2:
        return adj_nums[0] * adj_nums[1]
    else:
        return None

def get_gear_ratios(engine_arr):
    gear_ratios = []

    for i in range(len(engine_arr)):
        for j in range(len(engine_arr[0])):
            if engine_arr[i][j] == '*':
                got_ratio = get_possible_gear_ratio_or_none(engine_arr,i,j)
                if got_ratio != None:
                    gear_ratios.append(got_ratio)

    return gear_ratios

def main():
    arr = process_file()

    part_nums = get_part_numbers(arr)
    ans1 = get_sum_part_numbers(part_nums)

    gear_ratios = get_gear_ratios(arr)
    ans2 = get_sum_part_numbers(gear_ratios)

    print(ans2)


# ------ RUN SOLUTION ------
main()   # 532331, 82301120
