from typing import List

from helpers import process_file


def part_one(left_list: List[int], right_list: List[int]):
    """
    Find the "total distance" between the left and right lists by adding up the
    "distances".
    
    :param left_list: List of int location IDs
    :param right_list: List of int location IDs
    :return: None
    """
    left_list.sort()
    right_list.sort()

    total_dist = sum(abs(l - r) for l, r in zip(left_list, right_list))
    
    print(f"Part 1 answer: {total_dist}") # 1580061


def part_two(left_list: List[int], right_list: List[int]):
    """
    Find the "similarity score" of both lists.
    
    :param left_list: List of int location IDs
    :param right_list: List of int location IDs
    :return: None
    """
    similarity_score = 0
    for left_num in left_list:
        right_occurrences = right_list.count(left_num)
        similarity_score += left_num * right_occurrences

    print(f"Part 2 answer: {similarity_score}") # 23046913


def main():
    lists = process_file("01.txt", num_col=2, split=True)
    left_list = [int(x) for x in lists[0]]  # Convert to integers
    right_list = [int(x) for x in lists[1]]  # Convert to integers
    
    assert len(left_list) == len(right_list) # Both list lengths should be equal
    
    part_one(left_list, right_list)
    part_two(left_list, right_list)


if __name__ == "__main__":
    main()