def process_file():
    lines = []
    with open('../aoc-inputs/2023/04.txt') as f:
        lines = f.read().splitlines()

    processed_lines = []
    for line in lines:
        processed_line = []
        for line_part in line.split(': ')[1].split('|'):
            processed_line.append(set([int(i) for i in line_part.split()]))
        processed_lines.append(processed_line)

    return processed_lines

def get_scratchcard_points(cards):
    card_points = []

    for card in cards:
        pts = 0
        my_nums = card[0]
        winning_nums = card[1]
        for n in winning_nums:
            if n in my_nums:
                if pts == 0:
                    pts += 1
                else:
                    pts *= 2
        card_points.append(pts)

    return card_points

def get_sum_scratchcard_points(points):
    ret_sum = 0
    for point in points:
        ret_sum += point
    return ret_sum

def initialize_card_nums_map(num_cards):
    ret_map = {}
    for i in range(num_cards):
        ret_map[i] = 1
    return ret_map

def get_total_num_cards(cards):
    card_nums = initialize_card_nums_map(len(cards))

    for i in range(len(cards)):
        card = cards[i]
        num_matching = 0
        my_nums = card[0]
        winning_nums = card[1]
        for n in winning_nums:
            if n in my_nums:
                num_matching += 1
        card_num_multiplier = card_nums[i]
        for j in range(num_matching):
            card_nums[i+j+1] += 1 * card_num_multiplier

    return card_nums

def get_total_num_cards_sum(card_nums):
    ret_sum = 0
    for val in card_nums.values():
        ret_sum += val
    return ret_sum

def main():
    cards = process_file()

    card_points = get_scratchcard_points(cards)
    ans1 = get_sum_scratchcard_points(card_points)

    num_cards = get_total_num_cards(cards)
    ans2 = get_total_num_cards_sum(num_cards)
    print(ans2)


# ------ RUN SOLUTION ------
main()   # 20829, 12648035
