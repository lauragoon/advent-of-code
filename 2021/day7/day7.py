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


crab_subs = read_file('crabs.txt')
print(crab_position(crab_subs)) # 328187
