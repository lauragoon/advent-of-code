'''
TODO: clean up and make better this abomination of code
'''

'''
--- PART ONE ---
'''

def read_file(filename):
    system = {}

    with open(filename) as my_file:
        for line in my_file:

            line_split = line.rstrip().split('-')
            part1 = line_split[0]
            part2 = line_split[1]

            if part1 not in system.keys():
                system[part1] = [part2]
            else:
                system[part1].append(part2)

    return system

# TODO: why is set not working but str does

def paths_helper(cave, starter, num_paths, visited, path):
    # check if valid path
    if starter not in cave.keys():
        return 0

    next_dest = cave[starter]
    new_num = num_paths

    # print("STARTER: ", starter)
    # print("path so far: ", path)
    # print("next dest: ", next_dest)
    # print("visited: ", visited)

    path_split = path.split('-')
    path_set = set()
    for dest in path_split:
        if dest.islower() and dest != 'end':
            path_set.add(dest)

    for dest in next_dest:
        # print("dest: ", dest, " for starter: ", starter)
        # print("path so far now: ", path)

        # if end of path
        if dest == 'end':
            # print("found an end")
            # print("===PATH===: ", path+'-end')
            new_num += 1

        # if not visited
        elif dest not in path_set:
            # print("visit another")
            if starter.islower() and starter != 'end':
                visited.add(starter)
            output = paths_helper(cave, dest, num_paths, visited, path+'-'+dest)
            new_num += output

        # else:
            # print("visited: ", visited)
            # print("encountered visited")

    return new_num

def find_paths(cave):
    starts = cave['start']
    num_paths = 0

    init_keys = list(cave.keys())
    for key in init_keys:
        if key != 'start':
            paths = cave[key]
            for path in paths:
                if path not in cave.keys():
                    cave[path] = [key]
                else:
                    if key not in cave[path]:
                        cave[path].append(key)

    # print(cave)

    for start in starts:
        num_paths += paths_helper(cave, start, 0, set(['start']), 'start-'+start)

    return num_paths


# cave = read_file('cave.txt')
# print(find_paths(cave)) # 4691

'''
--- PART TWO ---
'''

def paths_helper2(cave, starter, num_paths, visited, path):
    # check if valid path
    if starter not in cave.keys():
        return 0

    next_dest = cave[starter]
    new_num = num_paths

    # print("STARTER: ", starter)
    # print("path so far: ", path)
    # print("next dest: ", next_dest)
    # print("visited: ", visited)

    path_split = path.split('-')
    path_dict = {}
    for dest in path_split:
        if dest.islower() and dest != 'end':
            if dest not in path_dict.keys():
                path_dict[dest] = 1
            else:
                path_dict[dest] += 1

    # print("path: ", path)
    # print("path dict: ", path_dict)

    for dest in next_dest:
        # print("dest: ", dest, " for starter: ", starter)
        # print("path so far now: ", path)

        # if end of path
        if dest == 'end':
            # print("found an end")
            # print("===PATH===: ", path+'-end')
            new_num += 1

        # if not visited
        elif dest != 'start' and ((dest in path_dict.keys() and path_dict[dest] < 2 and 2 not in path_dict.values()) or \
            dest not in path_dict.keys()):
            # print("visit another: ", dest)
            if starter.islower() and starter != 'end':
                visited.add(starter)
            output = paths_helper2(cave, dest, num_paths, visited, path+'-'+dest)
            new_num += output

        # else:
            # print("visited: ", visited)
            # print("encountered visited")

    return new_num

def find_paths2(cave):
    starts = cave['start']
    num_paths = 0

    # go back to start possible
    init_keys = list(cave.keys())
    for key in init_keys:
        if key != 'start':
            paths = cave[key]
            for path in paths:
                if path not in cave.keys():
                    cave[path] = [key]
                else:
                    if key not in cave[path]:
                        cave[path].append(key)

    # print(cave)

    for start in starts:
        num_paths += paths_helper2(cave, start, 0, set(['start']), 'start-'+start)

    return num_paths


cave = read_file('../aoc-inputs/2021/12.txt')
print(find_paths2(cave)) # 140718
