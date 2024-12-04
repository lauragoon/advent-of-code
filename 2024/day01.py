from typing import List, Optional

from helpers import process_file


def part_one(left_list: List[str], right_list: List[str]):
    """
    Find the "total distance" between the left and right lists by adding up the
    "distances".
    
    :param left_list: Path to the file to be processed.
    :param right_list: Number of columns to split the line into (if > 1).
    :return: None
    """
    len_list = len(left_list)

    total_dist = 0
    for i in range(len_list):
        total_dist += abs(int(left_list[i]) - int(right_list[i]))
    
    print(f"Part 1 answer: {total_dist}") # 1580061


def part_two(left_list: List[str], right_list: List[str]):
    pass


def main():
    lists = process_file("01.txt", num_col=2, split=True)
    left_list = lists[0]
    right_list = lists[1]

    left_list.sort()
    right_list.sort()
    
    assert len(left_list) == len(right_list) # Both list lengths should be equal
    
    part_one(left_list, right_list)


if __name__ == "__main__":
    main()