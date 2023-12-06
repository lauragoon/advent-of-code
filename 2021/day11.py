'''
--- PART ONE ---
'''

def read_file(filename):
    lines = []

    with open(filename) as my_file:
        for line in my_file:
            lines.append([int(num) for num in list(line.rstrip())])

    return lines

def flash(map_old, j, k, flash_old):
    map_length = len(map_old)
    map_width = len(map_old[0])
    map_new = map_old
    flash_new = flash_old
    num_flash = 0

    num_flash += 1
    flash_new[j][k] = 1
    map_new[j][k] = 0

    # check top left
    if j > 0 and k > 0 and flash_new[j-1][k-1] != 1:
        map_new[j-1][k-1] += 1
        if map_new[j-1][k-1] > 9:
            output = flash(map_new, j-1, k-1, flash_new)
            num_flash += output[0]
            map_new = output[1]
            flash_new = output[2]

    # check top
    if j > 0 and flash_new[j-1][k] != 1:
        map_new[j-1][k] += 1
        if map_new[j-1][k] > 9:
            output = flash(map_new, j-1, k, flash_new)
            num_flash += output[0]
            map_new = output[1]
            flash_new = output[2]

    # check top right
    if j > 0 and k < map_width-1 and flash_new[j-1][k+1] != 1:
        map_new[j-1][k+1] += 1
        if map_new[j-1][k+1] > 9:
            output = flash(map_new, j-1, k+1, flash_new)
            num_flash += output[0]
            map_new = output[1]
            flash_new = output[2]

    # check right
    if k < map_width-1 and flash_new[j][k+1] != 1:
        map_new[j][k+1] += 1
        if map_new[j][k+1] > 9:
            output = flash(map_new, j, k+1, flash_new)
            num_flash += output[0]
            map_new = output[1]
            flash_new = output[2]

    # check bottom right
    if j < map_length-1 and k < map_width-1 and flash_new[j+1][k+1] != 1:
        map_new[j+1][k+1] += 1
        if map_new[j+1][k+1] > 9:
            output = flash(map_new, j+1, k+1, flash_new)
            num_flash += output[0]
            map_new = output[1]
            flash_new = output[2]

    # check bottom
    if j < map_length-1 and flash_new[j+1][k] != 1:
        map_new[j+1][k] += 1
        if map_new[j+1][k] > 9:
            output = flash(map_new, j+1, k, flash_new)
            num_flash += output[0]
            map_new = output[1]
            flash_new = output[2]

    # check bottom left
    if j < map_length-1 and k > 0 and flash_new[j+1][k-1] != 1:
        map_new[j+1][k-1] += 1
        if map_new[j+1][k-1] > 9:
            output = flash(map_new, j+1, k-1, flash_new)
            num_flash += output[0]
            map_new = output[1]
            flash_new = output[2]

    # check left
    if k > 0 and flash_new[j][k-1] != 1:
        map_new[j][k-1] += 1
        if map_new[j][k-1] > 9:
            output = flash(map_new, j, k-1, flash_new)
            num_flash += output[0]
            map_new = output[1]
            flash_new = output[2]

    return num_flash, map_new, flash_new

def count_flashes(octopi, steps):
    octopi_copy = octopi
    num_flash = 0

    flash_map = []
    for i in range(10):
        new_row = []
        for j in range(10):
            new_row.append(0)
        flash_map.append(new_row)

    for i in range(steps):

        # refresh flash map
        flash_map = []
        for ij in range(10):
            new_row = []
            for jk in range(10):
                new_row.append(0)
            flash_map.append(new_row)

        for j in range(10):
            for k in range(10):

                # no need to update again if it updated during flash
                if flash_map[j][k] != 1:    
                    octopi_copy[j][k] += 1     

                    # flash
                    if octopi_copy[j][k] > 9:
                        output = flash(octopi_copy, j, k, flash_map)
                        num_flash += output[0]
                        octopi_copy = output[1]
                        flash_map = output[2]

    return num_flash

# octopi = read_file('octopus.txt')
# print(count_flashes(octopi, 100)) # 1749

'''
--- PART TWO ---
'''

def count_flashes2(octopi, steps):
    octopi_copy = octopi
    num_flash = 0

    flash_map = []
    for i in range(10):
        new_row = []
        for j in range(10):
            new_row.append(0)
        flash_map.append(new_row)

    for i in range(steps):

        # refresh flash map
        flash_map = []
        for ij in range(10):
            new_row = []
            for jk in range(10):
                new_row.append(0)
            flash_map.append(new_row)

        for j in range(10):
            for k in range(10):

                # no need to update again if it updated during flash
                if flash_map[j][k] != 1:    
                    octopi_copy[j][k] += 1     

                    # flash
                    if octopi_copy[j][k] > 9:
                        output = flash(octopi_copy, j, k, flash_map)
                        num_flash += output[0]
                        octopi_copy = output[1]
                        flash_map = output[2]

        stillFlash = True
        for a in range(10):
            for b in range(10):
                if flash_map[a][b] != 1:
                    stillFlash = False
        if stillFlash:
            return i+1

    return -1

octopi = read_file('../aoc-inputs/2021/11.txt')
print(count_flashes2(octopi, 10000)) # 285
