'''
--- PART ONE ---
'''

def read_file(filename):
    lines = []

    with open(filename) as my_file:
        for line in my_file:
            lines.append([int(num) for num in list(line.rstrip())])

    return lines

def find_risk_levels(heights):
    length = len(heights)
    width = len(heights[0])
    lo_risk_sum = 0

    for i in range(length):
        for j in range(width):

            # top left corner
            if i == 0 and j == 0:
                # check right and bottom
                if heights[i][j] < heights[i][j+1] and heights[i][j] < heights[i+1][j]:
                    lo_risk_sum += heights[i][j] + 1
            
            # top row
            elif i == 0 and j > 0 and j < width-1:
                # check left right bottom
                if heights[i][j] < heights[i][j-1] and heights[i][j] < heights[i][j+1] and heights[i][j] < heights[i+1][j]:
                    lo_risk_sum += heights[i][j] + 1

            # top right corner
            elif i == 0 and j == width-1:
                # check left and bottom
                if heights[i][j] < heights[i][j-1] and heights[i][j] < heights[i+1][j]:
                    lo_risk_sum += heights[i][j] + 1

            # left col
            elif j == 0 and i > 0 and i < length-1:
                # check top right bottom
                if heights[i][j] < heights[i-1][j] and heights[i][j] < heights[i][j+1] and heights[i][j] < heights[i+1][j]:
                    lo_risk_sum += heights[i][j] + 1

            # right col
            elif j == width-1 and i > 0 and i < length-1:
                # check top left bottom
                if heights[i][j] < heights[i-1][j] and heights[i][j] < heights[i][j-1] and heights[i][j] < heights[i+1][j]:
                    lo_risk_sum += heights[i][j] + 1

            # bottom left corner
            elif j == 0 and i == length-1:
                # check top and right
                if heights[i][j] < heights[i-1][j] and heights[i][j] < heights[i][j+1]:
                    lo_risk_sum += heights[i][j] + 1

            # bottom row
            elif i == length-1 and j > 0 and j < width-1:
                # check left top right
                if heights[i][j] < heights[i][j-1] and heights[i][j] < heights[i-1][j] and heights[i][j] < heights[i][j+1]:
                    lo_risk_sum += heights[i][j] + 1
            
            # bottom right corner
            elif j == width-1 and i == length-1:
                # check left and top
                if heights[i][j] < heights[i][j-1] and heights[i][j] < heights[i-1][j]:
                    lo_risk_sum += heights[i][j] + 1

            # fully surrounded cells
            else:
                # check top right bototom left
                if heights[i][j] < heights[i-1][j] and heights[i][j] < heights[i][j+1] and heights[i][j] < heights[i+1][j] and heights[i][j] < heights[i][j-1]:
                    lo_risk_sum += heights[i][j] + 1

    return lo_risk_sum

# heights = read_file('heightmap.txt')
# print(find_risk_levels(heights)) # 491

'''
--- PART TWO ---
'''

# edges/cornesr vs. surrounded
# go down and right
def dfs_helper(map, i, j, record, size):
    size_tracker = size
    record_new = record

    # 9's are not in basins
    if map[i][j] == 9:
        return size_tracker, record_new

    # visited
    if record[i][j] == 1:
        return size_tracker, record_new

    record_new[i][j] = 1
    size_tracker += 1

    if j < len(map[0])-1:
        dfs_out = dfs_helper(map, i, j+1, record_new, size_tracker)
        size_tracker = dfs_out[0]
        record_new = dfs_out[1]

    if i < len(map)-1:
        dfs_out = dfs_helper(map, i+1, j, record_new, size_tracker)
        size_tracker = dfs_out[0]
        record_new = dfs_out[1]

    if j > 0:
        dfs_out = dfs_helper(map, i, j-1, record_new, size_tracker)
        size_tracker = dfs_out[0]
        record_new = dfs_out[1]

    if i > 0:
        dfs_out = dfs_helper(map, i-1, j, record_new, size_tracker)
        size_tracker = dfs_out[0]
        record_new = dfs_out[1]

    return size_tracker, record_new

def find_basins(heights):
    length = len(heights)
    width = len(heights[0])
    basin_sizes = []
    
    marker_map = [] # marks basins found via dfs
    for i in range(length):
        new_row = []
        for j in range(width):
            new_row.append(0)
        marker_map.append(new_row)

    # dfs
    for i in range(length):
        for j in range(width):   
            # check if already basin or cannot be basin
            if marker_map[i][j] != 1 and heights[i][j] != 9:
                output = dfs_helper(heights, i, j, marker_map, 0)
                basin_sizes.append(output[0])
                marker_map = output[1]

    # find 3 largest basins
    basin_sizes = sorted(basin_sizes, reverse=True)

    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]

heights = read_file('heightmap.txt')
print(find_basins(heights)) # 1075536
