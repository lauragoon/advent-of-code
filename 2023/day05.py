def process_file():
    seeds = []
    seed_to_soil_map = []
    soil_to_fertilizer_map = []
    fertilizer_to_water_map = []
    water_to_light_map = []
    light_to_temperature_map = []
    temperature_to_humidity_map = []
    humidity_to_location_map = []

    ret_data = [seeds, seed_to_soil_map, soil_to_fertilizer_map, fertilizer_to_water_map, water_to_light_map, light_to_temperature_map, temperature_to_humidity_map, humidity_to_location_map]
    curr_map = 0

    with open('../aoc-inputs/2023/05.txt') as f:
        for line in f:
            if line.startswith('seeds'):
                ret_data[curr_map].extend([int(i) for i in line[7:].split()])  
            elif line.startswith('seed-to-soil'):
                curr_map = 1
            elif line.startswith('soil-to-fertilizer'):
                curr_map = 2
            elif line.startswith('fertilizer-to-water'):
                curr_map = 3
            elif line.startswith('water-to-light'):
                curr_map = 4
            elif line.startswith('light-to-temperature'):
                curr_map = 5
            elif line.startswith('temperature-to-humidity'):
                curr_map = 6
            elif line.startswith('humidity-to-location'):
                curr_map = 7
            elif len(line) > 1:
                processed_nums = [int(i) for i in line.split()]
                ret_data[curr_map].append((processed_nums[1], processed_nums[1]+processed_nums[2]-1, processed_nums[0]-processed_nums[1]))

    for i in range(1,8):
        ret_data[i] = sorted(ret_data[i], key=lambda x: x[0])

    return ret_data

# part 1
def get_lowest_location_num(almanac):
    seeds = almanac[0]
    lowest_location = float('inf')

    for seed in seeds:
        curr_source = seed

        for i in range(1,8): # iterate through maps
            is_found = False
            j = 0
            while not is_found and j < len(almanac[i]): # while we haven't found match in the next map yet
                if curr_source >= almanac[i][j][0] and curr_source <= almanac[i][j][1]:
                    curr_source += almanac[i][j][2] # update the new mapped value as the next source value for next map
                    is_found = True
                j += 1 # look at next new map interval within the same map

        if curr_source < lowest_location:
            lowest_location = curr_source

    return lowest_location

# part 2 (condense lists of ranges)
def condense_ranges(range_list):
    ret_range_list = []
    sorted_range_list = sorted(range_list, key=lambda x: (x[0],x[1]))

    ret_range_list.append(sorted_range_list[0])

    for i in range(1,len(sorted_range_list)):
        curr_range_start = sorted_range_list[i][0]
        curr_range_end = sorted_range_list[i][1]

        if curr_range_start <= ret_range_list[-1][1]:
            ret_range_list[-1][1] = max(ret_range_list[-1][1], curr_range_end)
        else:
            ret_range_list.append([curr_range_start, curr_range_end])


    return ret_range_list

# part 2
def get_lowest_location_num_modified(almanac):
    curr_source = []
    i = 0 # iterate through pairs of seed input
    while i < len(almanac[0])-1:
        curr_source.append([almanac[0][i],almanac[0][i]+almanac[0][i+1]-1]) # add seeds as ranges into curr_source (seed_range_start, seed_range_len)
        i += 2 # seed input comes in pairs of numbers

    for i in range(1,8): # iterate over all the maps
        new_source = []
        temp_source = [] # for intervals that are not yet translated, but to translate before finishing up
        k = 0 # index in the current source intervals to see which interval focus on

        while k < len(curr_source):
            curr_range_start = curr_source[k][0]
            curr_range_end = curr_source[k][1]

            for j in range(len(almanac[i])):
                if curr_range_start >= almanac[i][j][0] and curr_range_start <= almanac[i][j][1]:
                    # all numbers in curr range are in the same curr new mapped bucket
                    if curr_range_end <= almanac[i][j][1]:
                        new_source.append([curr_range_start+almanac[i][j][2], curr_range_end+almanac[i][j][2]])
                    # only beginning section curr range numbers are curr new mapped bucket
                    else:
                        new_source.append([curr_range_start+almanac[i][j][2], almanac[i][j][1]+almanac[i][j][2]])
                        temp_source.append([almanac[i][j][1]+1,curr_range_end]) # add this unaccounted for yet range
                elif curr_range_end >= almanac[i][j][0] and curr_range_end <= almanac[i][j][1]:
                    # only end section of curr range numbers are in curr new mapped bucket
                    if curr_range_start < almanac[i][j][0]:
                        new_source.append([almanac[i][j][0]+almanac[i][j][2],curr_range_end+almanac[i][j][2]])
                        temp_source.append([curr_range_start,almanac[i][j][0]-1]) # add this unaccounted for yet range
            
            k += 1

            # consider the partial intervals that have not yet been translated into the new map
            if k >= len(curr_source) and len(temp_source) > 0:
                k = 0
                curr_source = temp_source
                temp_source = []

        # if there new mapped numbers, condense ranges from the new mapped numbers, though idk how it accounts for when somoe numbers don't have matches and just map number == itself
        if len(new_source) > 0:
            curr_source = condense_ranges(new_source)

    return sorted(curr_source, key=lambda x: x[0])[0][0]


def main():
    almanac = process_file()
    # print(almanac)

    ans1 = get_lowest_location_num(almanac)
    print(ans1)

    ans2 = get_lowest_location_num_modified(almanac)
    print(ans2)


# ------ RUN SOLUTION ------
main()   # 388071289, 84206669