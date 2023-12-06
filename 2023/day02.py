def process_file():
    lines = []
    with open('../aoc-inputs/2023/02.txt') as f:
        lines = f.read().splitlines()

    processed_lines = []
    for line in lines:
        line_games = []
        games = line.split(': ')[1].split('; ')
        for game in games:
            line_game = [0,0,0]
            cubes = game.split(', ')
            for cube in cubes:
                cube_split = cube.split(' ')
                match cube_split[1]:
                    case 'red':
                        line_game[0] = int(cube_split[0])
                    case 'green':
                        line_game[1] = int(cube_split[0])
                    case 'blue':
                        line_game[2] = int(cube_split[0])
            line_games.append(line_game)
        processed_lines.append(line_games)
    return processed_lines

def is_game_possible(num_red, num_green, num_blue, game):
    for round in game:
        if round[0] > num_red or round[1] > num_green or round[2] > num_blue:
            return False
    return True

def get_which_games_possible(num_red, num_green, num_blue, games):
    possible_games = []
    for i in range(len(games)):
        if is_game_possible(num_red, num_green, num_blue, games[i]):
            possible_games.append(i+1)
    return possible_games\

def get_sum_games(game_ids):
    ret_sum = 0
    for id in game_ids:
        ret_sum += id
    return ret_sum

# ------ new for part 2 ------ 
def min_cubes_needed(game):
    min_needed = [0, 0, 0]
    for round in game:
        for i in range(3):
            if round[i] > min_needed[i]:
                min_needed[i] = round[i]
    return min_needed

def get_power_cube_set(cubes):
    return cubes[0] * cubes[1] * cubes[2]

def get_min_cubes_needed_all_games(games):
    min_needed = []
    for game in games:
        min_needed.append(min_cubes_needed(game))
    power_cube_sets = []
    for cubes in min_needed:
        power_cube_sets.append(get_power_cube_set(cubes))
    ret_sum = 0
    for power in power_cube_sets:
        ret_sum += power
    return ret_sum
# ------------

def main():
    games = process_file()

    possible_games = get_which_games_possible(12, 13, 14, games)
    ans1 = get_sum_games(possible_games)
    ans2 = get_min_cubes_needed_all_games(games)

    print(ans1)
    print(ans2)


# ------ RUN SOLUTION ------
main()   # 2716, 72227
