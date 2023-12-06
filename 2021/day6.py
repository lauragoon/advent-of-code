'''
--- PART ONE ---
'''

def read_file(filename):
    with open(filename) as my_file:
        line = my_file.read().splitlines()
    return [int(num) for num in line[0].split(',')]

def population_helper(fishes, days, curr_day):
    # check days
    if curr_day == days:
        return len(fishes)

    fishes_dict = {}
    fishes_set = list(set(fishes))
    population_dict = {}

    # count occurrences of all timers
    for fish in fishes:
        if fish in fishes_dict.keys():
            fishes_dict[fish] += 1
        else:
            fishes_dict[fish] = 1

    # get timer -> population count for designated days
    for fish in fishes_set:
        if fish == 0:
            population_dict[fish] = population_helper([6, 8], days, curr_day + 1)
        else:
            population_dict[fish] = population_helper([fish-1], days, curr_day + 1)

    num_fish = 0

    for fish in fishes_set:
        num_fish += fishes_dict[fish] * population_dict[fish]

    return num_fish

def fish_population(fishes, days):
    return population_helper(fishes, days, 0)

# lanternfish = read_file('fish.txt')
# print(fish_population(lanternfish, 80)) # 395627 

'''
--- PART TWO ---
'''

def fish_population_faster(fishes, days):
    fishes_dict = {}

    # count occurrences of all timers
    for fish in fishes:
        if fish in fishes_dict.keys():
            fishes_dict[fish] += 1
        else:
            fishes_dict[fish] = 1

    for i in range(days):
        new_dict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
        
        for key in fishes_dict.keys():
            if key == 0:
                new_dict[6] += fishes_dict[key]
                new_dict[8] += fishes_dict[key]

            else:
                new_dict[key-1] += fishes_dict[key]

        fishes_dict = new_dict

    fishes_count = 0
    for key in fishes_dict.keys():
        fishes_count += fishes_dict[key]
    
    return fishes_count


lanternfish = read_file('../aoc-inputs/2021/06.txt')
print(fish_population_faster(lanternfish, 256)) # 1767323539209
