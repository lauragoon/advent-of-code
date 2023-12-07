from functools import cmp_to_key


FIVE_OF_A_KIND = 0
FOUR_OF_A_KIND = 1
FULL_HOUSE = 2
THREE_OF_A_KIND = 3
TWO_PAIR = 4
ONE_PAIR = 5
HIGH_CARD = 6

def process_file():
    hands = []
    with open('../aoc-inputs/2023/07.txt') as f:
        for line in f:
            hands.append((line.split()[0], int(line.split()[1])))
    return hands

def get_hand_type(hand):
    list_hand = list(hand)
    set_hand = set(list_hand)
    card_nums = {}
    for card in set_hand:
        card_nums[card] = list_hand.count(card)

    # absolute case if have 2 nums, can convert all to same with joker
    if len(set_hand) <= 2 and 'J' in set_hand:
        return FIVE_OF_A_KIND
    
    if 5 in card_nums.values():
        return FIVE_OF_A_KIND
    
    elif 4 in card_nums.values():
        # return FOUR_OF_A_KIND # part 1
        if 'J' in set_hand:
            return FIVE_OF_A_KIND
        else:
            return FOUR_OF_A_KIND
        
    elif 3 in card_nums.values():
        # if 2 in card_nums.values(): # part 1
        #     return FULL_HOUSE
        # else:
        #     return THREE_OF_A_KIND
        if 'J' in set_hand:
            if card_nums['J'] == 2:
                return FIVE_OF_A_KIND
            else:
                return FOUR_OF_A_KIND
        else:
            if 2 in card_nums.values():
                return FULL_HOUSE
            else:
                return THREE_OF_A_KIND
            
    elif 2 in card_nums.values():
        # if list(card_nums.values()).count(2) == 2: # part 1
        #     return TWO_PAIR
        # else:
        #     return ONE_PAIR
        if 'J' in set_hand:
            if card_nums['J'] != 2:
                if list(card_nums.values()).count(2) == 2:
                    return FULL_HOUSE
                else:
                    return THREE_OF_A_KIND
            else:
                if list(card_nums.values()).count(2) == 2:
                    return FOUR_OF_A_KIND
                else:
                    return THREE_OF_A_KIND
        else:
            if list(card_nums.values()).count(2) == 2:
                return TWO_PAIR
            else:
                return ONE_PAIR
            
    else:
        if 'J' in set_hand:
            return ONE_PAIR
        else:
            return HIGH_CARD
    
def compare_hands(hand1, hand2):
    # ordered_cards = ['2','3','4','5','6','7','8','9','T','J','Q','K','A'] # part 1
    ordered_cards = ['J','2','3','4','5','6','7','8','9','T','Q','K','A']
    # although ordred cards are sroted from least to greatest for index checking
    # returning sorted hand is sorted from highest to lowest left to right, so the sorting logic is reversed
    for i in range(5):
        if ordered_cards.index(hand1[0][0][i]) < ordered_cards.index(hand2[0][0][i]):
            return 1
        elif ordered_cards.index(hand1[0][0][i]) > ordered_cards.index(hand2[0][0][i]):
            return -1
    return 0
      
def get_hands_order(hands):
    categorized_hands = [[],[],[],[],[],[],[]]
    for hand in hands:
        curr_hand_type = get_hand_type(hand[0])
        categorized_hands[curr_hand_type].append((hand,curr_hand_type))
    
    ordered_hands = []
    for hand_category in categorized_hands:
        if len(hand_category) == 1:
            ordered_hands.append(hand_category[0])
        elif len(hand_category) >= 2:
            ordered_hands.extend(sorted(hand_category, key=cmp_to_key(compare_hands)))

    return ordered_hands
    
def get_total_winnings(ordered_hands):
    ret_winnings = 0
    num_hands = len(ordered_hands)
    for i in range(num_hands):
        ret_winnings += ordered_hands[i][0][1] * (num_hands-i)
    return ret_winnings

def main():
    lines = process_file()

    hands_order = get_hands_order(lines)
    ans = get_total_winnings(hands_order)

    print(ans)


# ------ RUN SOLUTION ------
main()   # 253866470, 254494947
