'''
--- PART ONE & TWO ---
'''

# import time

def read_file(filename):
    vents = []

    with open(filename) as my_file:
        for line in my_file:
            line_split = line.split()
            point1 = [int(pt) for pt in line_split[0].split(',')]
            point2 = [int(pt) for pt in line_split[2].split(',')]
            vents.append([point1, point2])

    return vents

def count_intersections(vents):
    # start_time = time.time()
    num_vents = len(vents)
    all_intersections = set()

    # compare pairs of vent lines
    for i in range(num_vents-1):
        for j in range(i+1, num_vents):

            line1 = vents[i]
            line2 = vents[j]

            line1x1, line1y1 = line1[0][0], line1[0][1]
            line1x2, line1y2 = line1[1][0], line1[1][1]
            line2x1, line2y1 = line2[0][0], line2[0][1]
            line2x2, line2y2 = line2[1][0], line2[1][1]

            line1_orien = "vertical" if line1x1 == line1x2 else ("horizontal" if line1y1 == line1y2 else "diagonal")
            line2_orien = "vertical" if line2x1 == line2x2 else ("horizontal" if line2y1 == line2y2 else "diagonal")

            # # ignore diagonal lines as specified in part 1
            # if line1_orien is "diagonal" or line2_orien is "diagonal":
            #     continue

            m1 = (0,(line1y2 - line1y1)/abs(line1y2 - line1y1)) if line1_orien is "vertical" else \
                (((line1x2 - line1x1)/abs(line1x2 - line1x1),0) if line1_orien is "horizontal" else \
                    ((line1x2 - line1x1)/abs(line1x2 - line1x1), (line1y2 - line1y1)/abs(line1y2 - line1y1)))
            m1 = (int(m1[0]), int(m1[1]))
                    
            m2 = (0,(line2y2 - line2y1)/abs(line2y2 - line2y1)) if line2_orien is "vertical" else \
                (((line2x2 - line2x1)/abs(line2x2 - line2x1),0) if line2_orien is "horizontal" else \
                    ((line2x2 - line2x1)/abs(line2x2 - line2x1), (line2y2 - line2y1)/abs(line2y2 - line2y1)))
            m2 = (int(m2[0]), int(m2[1]))

            len1 = abs(line1x2 - line1x1) + 1 if line1_orien is "horizontal" else abs(line1y2 - line1y1) + 1
            len2 = abs(line2x2 - line2x1) + 1 if line2_orien is "horizontal" else abs(line2y2 - line2y1) + 1

            line1pts = set()
            line2pts = set()

            # line 1 pts
            for iter1 in range(len1):
                line1pts.add((line1x1 + (m1[0] * iter1), line1y1 + (m1[1] * iter1)))

            # line 2 pts
            for iter2 in range(len2):
                line2pts.add((line2x1 + (m2[0] * iter2), line2y1 + (m2[1] * iter2)))

            all_intersections = all_intersections.union(line1pts.intersection(line2pts))

    # print("finished in: ", time.time() - start_time)
    return len(list(all_intersections))

# def count_intersections_alt(vents):
#     start_time = time.time()
#     num_vents = len(vents)
#     all_points = set()
#     all_intersect = set()

#     # compare pairs of vent lines
#     for i in range(num_vents-1):

#         line1 = vents[i]

#         line1x1, line1y1 = line1[0][0], line1[0][1]
#         line1x2, line1y2 = line1[1][0], line1[1][1]

#         line1_orien = "vertical" if line1x1 == line1x2 else ("horizontal" if line1y1 == line1y2 else "diagonal")

#         # ignore diagonal lines as specified in part 1
#         if line1_orien is "diagonal":
#             continue

#         m1 = (0,(line1y2 - line1y1)/abs(line1y2 - line1y1)) if line1_orien is "vertical" else \
#             (((line1x2 - line1x1)/abs(line1x2 - line1x1),0) if line1_orien is "horizontal" else \
#                 ((line1x2 - line1x1)/abs(line1x2 - line1x1), (line1y2 - line1y1)/abs(line1y2 - line1y1)))
#         m1 = (int(m1[0]), int(m1[1]))

#         len1 = abs(line1x2 - line1x1) + 1 if line1_orien is "horizontal" else abs(line1y2 - line1y1) + 1

#         line1pts = set()

#         # line 1 pts
#         for iter1 in range(len1):
#             curr_point = (line1x1 + (m1[0] * iter1), line1y1 + (m1[1] * iter1))
            
#             line1pts.add(curr_point)

#             # # check intersection
#             # if curr_point in all_points:
#             #     all_intersect.add(curr_point)
#             # else:
#             #     all_points.add(curr_point)
#         all_intersect = all_intersect.union(line1pts.intersection(all_points))
#         all_points = all_points.union(line1pts)
#     print("finished in: ", time.time() - start_time)
#     return len(list(all_intersect))

vent_lines = read_file('vents.txt')
print(count_intersections(vent_lines))
# print(count_intersections_alt(vent_lines))
