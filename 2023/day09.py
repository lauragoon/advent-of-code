def process_file():
    lines = []
    with open('../aoc-inputs/2023/09.txt') as f:
        for line in f:
            lines.append([int(i) for i in line.split(' ')])

    return lines

def get_extrapolated_value(hist):
    curr_hist_calcs = hist
    hist_diffs = [hist]
    got_all_zeroes = False

    while not got_all_zeroes:
        curr_diffs = []
        for i in range(1,len(curr_hist_calcs)):
            curr_diffs.append(curr_hist_calcs[i] - curr_hist_calcs[i-1])
        hist_diffs.append(curr_diffs)
        curr_hist_calcs = curr_diffs

        if len(set(curr_diffs)) == 1 and curr_diffs[0] == 0:
            got_all_zeroes = True

    for i in reversed(range(len(hist_diffs))):
        if i == len(hist_diffs)-1:
            hist_diffs[i].append(0)
            hist_diffs[i].insert(0, 0)
        else:
            hist_diffs[i].append(hist_diffs[i][-1] + hist_diffs[i+1][-1])
            hist_diffs[i].insert(0, hist_diffs[i][0] - hist_diffs[i+1][0])

    return hist_diffs[0][0], hist_diffs[0][-1]

def get_sum_arr(arr):
    ret_sum = 0
    for num in arr:
        ret_sum += num
    return ret_sum

def get_sum_all_extrapolated_values(lines):
    extrapolated_vals_past = []
    extrapolated_vals_future = []
    for hist in lines:
        extrapolated_val = get_extrapolated_value(hist)
        extrapolated_vals_past.append(extrapolated_val[0])
        extrapolated_vals_future.append(extrapolated_val[1])
    return get_sum_arr(extrapolated_vals_past), get_sum_arr(extrapolated_vals_future)

def main():
    lines = process_file()

    ans1, ans2 = get_sum_all_extrapolated_values(lines)
    print(ans1)
    print(ans2)


# ------ RUN SOLUTION ------
main()   # 2075724761, 1072 # TODO: input mutable/changes per run

