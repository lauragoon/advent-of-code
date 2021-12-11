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


heights = read_file('heightmap.txt')
print(find_risk_levels(heights))
