from math import lcm

def process_file():
    lines = []
    with open('../aoc-inputs/2023/08.txt') as f:
        lines = f.read().splitlines()

    directions = lines[0]
    network_map = {}
    starting_nodes = []

    for i in range(2,len(lines)):
        split_line = lines[i].split(' = ')
        src = split_line[0]
        dest_left = split_line[1].split(', ')[0][1:]
        dest_right = split_line[1].split(', ')[1][:-1]
        network_map[src] = (dest_left, dest_right)
        if src[-1] == 'A':
            starting_nodes.append(src)
    
    return directions, network_map, starting_nodes

def get_idx_from_direction(direction):
    if direction == 'L':
        return 0
    else:
        return 1

def get_num_steps_part1(directions, network_map, starting_node='AAA', ending_node='ZZZ'):
    num_steps = 0
    found_dest = False
    curr_dir_idx = 0
    curr_loc = starting_node

    while not found_dest:
        num_steps += 1
        curr_dir = directions[curr_dir_idx]
        curr_loc = network_map[curr_loc][get_idx_from_direction(curr_dir)]
        if (ending_node != None and curr_loc == 'ZZZ') or (ending_node == None and curr_loc[-1] == 'Z'):
            found_dest = True
        else:
            if curr_dir_idx == len(directions)-1:
                curr_dir_idx = 0
            else:
                curr_dir_idx += 1

    return num_steps, curr_loc

# part 2
def verify_lcm_applicable(directions, network_map, starts):
    for starting_node in starts:
        num_steps, first_ending_node = get_num_steps_part1(directions, network_map, starting_node, None)
        num_steps2, second_ending_node = get_num_steps_part1(directions, network_map, first_ending_node, None)
        if num_steps != num_steps2 or first_ending_node != second_ending_node:
            return False
    return True

# part 2
def get_num_steps_part2(directions, network_map, starts):
    num_steps = []

    if verify_lcm_applicable(directions, network_map, starts):
        for starting_node in starts:
            num_steps.append(get_num_steps_part1(directions, network_map, starting_node, None)[0])

    return lcm(*num_steps)
    

def main():
    directions, net_map, starts = process_file()

    ans1 = get_num_steps_part1(directions, net_map)[0]
    ans2 = get_num_steps_part2(directions,net_map,starts)
    print(ans1, ans2)


# ------ RUN SOLUTION ------
main()   # 12083, 13385272668829
