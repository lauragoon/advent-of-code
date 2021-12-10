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

    fish_list = []
    for fish in fishes:
        if fish == 0:
            fish_list.append(6)
            fish_list.append(8)
        else:
            fish_list.append(fish - 1)

    return population_helper(fish_list, days, curr_day + 1)

def fish_population(fishes, days):
    num_fish = 0
    population_dict = {}

    for fish in fishes:
        
        # check records
        if fish in population_dict.keys():
            num_fish += population_dict[fish]
        else:
            new_fish = population_helper([fish], days, 0)
            population_dict[fish] = new_fish
            num_fish += new_fish

    return num_fish

lanternfish = read_file('fish.txt')
print(fish_population(lanternfish, 80))
