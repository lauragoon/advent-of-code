'''
--- Part One ---
'''

# read file
depths = []
with open('depths.txt') as my_file:
    for line in my_file:
        depths.append(int(line))


def count_increases(depths):
    # iterate depths
    ctr = 0
    prev = -1

    for depth in depths:
        # if not first depth and current depth > previous
        if prev != -1 and depth > prev:
            ctr += 1
        # set prev
        prev = depth

    # return output
    return ctr

# print(count_increases('depths.txt')) # 1655


'''
--- Part Two ---
'''

def count_sum_increases(depths):
    itr = 0
    ctr = 0
    prev = -1

    # interate in thirds
    while itr <= len(depths) - 3:
        # there is something to compare
        if prev != -1:
            curr = depths[itr] + depths[itr+1] + depths[itr+2]
            if curr > prev:
                ctr += 1
        # update prev and iteration pointer
        prev = depths[itr] + depths[itr+1] + depths[itr+2]
        itr += 1

    return ctr

print(count_sum_increases(depths))
