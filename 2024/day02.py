from typing import List

from helpers import process_file


def is_report_safe(arr: List[int], min_diff: int, max_diff: int) -> bool:
    """
    Determine if report is safe or not.
    
    :param arr: Report
    :param min_diff: Start of lower range of unsafe difference
    :param max_diff: Start of upper range of unsafe difference
    :return: True if safe, False if unsafe
    """
    # Check initial difference direction
    initial_diff = arr[0] - arr[1]

    # If the initial difference unsafe, return False
    if abs(initial_diff) == min_diff or abs(initial_diff) > max_diff:
        return False

    # Check for rest of report
    for i in range(1, len(arr) - 1):
        current_diff = arr[i] - arr[i+1]

        # Check if the direction changes
        if (initial_diff > 0) != (current_diff > 0):
            return False

        # Check if the difference is invalid
        if abs(current_diff) == min_diff or abs(current_diff) > max_diff:
            return False
        
    return True


def main():
    reports = process_file("02.txt", num_col=1, split=True)
    reports = [[int(x) for x in sublist] for sublist in reports]
    
    num_safe_reports = sum(
        1 for report in reports if is_report_safe(report, 0, 3)
    )

    print(f"Part 1 answer: {num_safe_reports}") # 257


if __name__ == "__main__":
    main()