'''
--- PART ONE ---
'''

def read_file(filename):
    with open(filename) as my_file:
        line = my_file.read().splitlines()
    return [int(num) for num in line[0].split(',')]

# assumes that crabs is sorted already
def get_feul_count(crabs, pos):
    left_arr = list(filter(lambda num: num < pos, crabs))
    right_arr = list(filter(lambda num: num > pos, crabs))

    left_feul = (len(left_arr) * pos) - sum(left_arr)
    right_feul = sum(right_arr) - (len(right_arr) * pos)

    return left_feul + right_feul

def crab_position(crabs):
    if len(crabs) == 1:
        return crabs[0]

    crabs = sorted(crabs)
    prev = float('inf')

    for i in range(max(crabs)):
        curr_feul = get_feul_count(crabs, i)
        if curr_feul > prev:
            return prev
        else:
            prev = curr_feul

    return prev


# crab_subs = read_file('crabs.txt')
# print(crab_position(crab_subs)) # 328187

'''
--- PART TWO ---
'''

# assumes that crabs is sorted already
def get_feul_count(crabs, pos):
    crabs_dict = {}
    for crab in crabs:
        if crab in crabs_dict.keys():
            crabs_dict[crab] += 1
        else:
            crabs_dict[crab] = 1

    left_arr = list(filter(lambda num: num < pos, crabs))
    right_arr = list(filter(lambda num: num > pos, crabs))

    left_keys = list(set(left_arr))
    right_keys = list(set(right_arr))

    left_partialsum = 0
    right_partialsum = 0

    for key in left_keys:
        left_partialsum += int(((abs(key-pos)**2 + abs(key-pos)) / 2) * crabs_dict[key])
    for key in right_keys:
        right_partialsum += int(((abs(key-pos)**2 + abs(key-pos)) / 2) * crabs_dict[key])

    return left_partialsum + right_partialsum

def crab_position(crabs):
    if len(crabs) == 1:
        return crabs[0]

    crabs = sorted(crabs)
    prev = float('inf')

    for i in range(max(crabs)):
        curr_feul = get_feul_count(crabs, i)
        if curr_feul > prev:
            return prev
        else:
            prev = curr_feul

    return prev

crab_subs = read_file('crabs.txt')
print(crab_position(crab_subs)) # 91257582
