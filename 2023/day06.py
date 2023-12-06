# part 1
def process_file():
    lines = []
    with open('../aoc-inputs/2023/06.txt') as f:
        lines = f.read().splitlines()

    processed_lines = []
    for line in lines:
        split_line = line.split()
        if line.startswith('Time'):
            processed_lines = [[int(i),-1] for i in split_line[1:]]
        else:
            for i in range(1,len(split_line)):
                processed_lines[i-1][1] = int(split_line[i])

    return processed_lines

# part 2
def process_files_part2():
    lines = []
    with open('../aoc-inputs/2023/06.txt') as f:
        lines = f.read().splitlines()

    processed_lines = []
    for line in lines:
        processed_lines.append(int(''.join(line.split()[1:])))

    return [processed_lines]

def get_num_ways_to_win(races):
    num_ways = [0] * len(races)

    for i in range(len(races)):
        race_time = races[i][0]
        race_record_distance = races[i][1]

        for j in range(1,race_time+1):
            if (race_time - j) * j > race_record_distance:
                num_ways[i] += 1

    return num_ways

def get_nums_multiplied(arr):
    ret_product = 1
    for num in arr:
        ret_product *= num
    return ret_product

def main():
    lines1 = process_file()
    num_ways_to_win1 = get_num_ways_to_win(lines1)
    ans1 = get_nums_multiplied(num_ways_to_win1)
    print(ans1)

    lines2 = process_files_part2()
    num_ways_to_win2 = get_num_ways_to_win(lines2)
    ans2 = get_nums_multiplied(num_ways_to_win2)
    print(ans2)


# ------ RUN SOLUTION ------
main()   # 211904, 43364472
