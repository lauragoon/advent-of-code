'''
--- PART ONE ---
'''

def read_file(filename):
    lines = []

    with open(filename) as my_file:
        for line in my_file:
            lines.append([int(num) for num in list(line.rstrip())])

    return lines

def init_record(cavern, val):
    ret = []

    for i in range(len(cavern)):
        ret_line = []
        for j in range(len(cavern[0])):
            ret_line.append(val)
        ret.append(ret_line)

    return ret

def dijkstra(cavern):
    score = init_record(cavern, float('inf'))
    visited = init_record(cavern, False)
    to_visit = set()

    score[0][0] = 0
    to_visit.add((0,0))

    while len(to_visit) > 0:
        visit_now = {curr_idx:score[curr_idx[1]][curr_idx[0]] for curr_idx in to_visit}
        now_idx = min(visit_now, key=visit_now.get)
        now_x = now_idx[0]
        now_y = now_idx[1]

        to_visit.remove(now_idx)
        visited[now_y][now_x] = True

        # lower neighbor first
        neighbors = {}

        # up
        if now_y > 0:
            neighbors['up'] = score[now_y-1][now_x]

        # right
        if now_x < len(cavern[0])-1:
            neighbors['right'] = score[now_y][now_x+1]

        # down
        if now_y < len(cavern)-1:
            neighbors['down'] = score[now_y+1][now_x]

        # left
        if now_x > 0:
            neighbors['left'] = score[now_y][now_x-1]

        while len(neighbors) > 0:
            curr_neigh = min(neighbors, key=neighbors.get)
            del neighbors[curr_neigh]

            # up
            if curr_neigh == 'up':
                if score[now_y][now_x] + cavern[now_y-1][now_x] < score[now_y-1][now_x]:
                    score[now_y-1][now_x] = score[now_y][now_x] + cavern[now_y-1][now_x]
                if not visited[now_y-1][now_x]:
                    to_visit.add((now_x, now_y-1))  

            # right
            if curr_neigh == 'right':
                if score[now_y][now_x] + cavern[now_y][now_x+1] < score[now_y][now_x+1]:
                    score[now_y][now_x+1] = score[now_y][now_x] + cavern[now_y][now_x+1]
                if not visited[now_y][now_x+1]:
                    to_visit.add((now_x+1, now_y))

            # down
            if curr_neigh == 'down':
                if score[now_y][now_x] + cavern[now_y+1][now_x] < score[now_y+1][now_x]:
                    score[now_y+1][now_x] = score[now_y][now_x] + cavern[now_y+1][now_x]
                if not visited[now_y+1][now_x]:
                    to_visit.add((now_x, now_y+1))  

            # left
            if curr_neigh == 'left':
                if score[now_y][now_x] + cavern[now_y][now_x-1] < score[now_y][now_x-1]:
                    score[now_y][now_x-1] = score[now_y][now_x] + cavern[now_y][now_x-1]
                if not visited[now_y][now_x-1]:
                    to_visit.add((now_x-1, now_y))  

    return score

def find_path(cavern):
    score = dijkstra(cavern)
    return score[len(cavern)-1][len(cavern[0])-1]

cavern = read_file('cavern.txt')
print(find_path(cavern))
