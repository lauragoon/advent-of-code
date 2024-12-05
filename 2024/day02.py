from typing import List

from helpers import process_file


def is_report_safe(arr: List[int], min_diff: int, max_diff: int) -> bool:
    """
    Determine if report is "safe" or not.
    
    :param arr: Report
    :param min_diff: Lower range of unsafe difference (inclusive of safe)
    :param max_diff: Upper range of unsafe difference (inclusive of safe)
    :return: True if safe, False if unsafe
    """
    # Helper function to check if a difference is within the valid range
    def is_valid_diff(diff: int) -> bool:
        return min_diff < abs(diff) < max_diff

    # Check initial difference direction
    initial_diff = arr[0] - arr[1]

    # If the initial difference unsafe, return False
    if not is_valid_diff(initial_diff):
        return False

    # Check for rest of report
    for i in range(1, len(arr) - 1):
        current_diff = arr[i] - arr[i+1]

        # Check if the direction changes
        if ((initial_diff > 0) != (current_diff > 0) or
            not is_valid_diff(current_diff)):
            return False
        
    return True


def iterate_report_combos(arr, min_diff, max_diff, use_problem_dampener=False):
    """
    Iterate over report combinations to check if any modified report is safe.
    
    :param arr: Report
    :param min_diff: Lower range of unsafe difference (inclusive of safe)
    :param max_diff: Upper range of unsafe difference (inclusive of safe)
    :param use_problem_dampener: Whether to try modifying the report
    :return: True if any valid report is found, False otherwise
    """
    # If the original report is safe, return True
    if is_report_safe(arr, min_diff, max_diff):
        return True
    
    if not use_problem_dampener:
        return False
    
    # Try to find a safe sub-report by modifying report
    for i in range(len(arr) - 1):
        modified_report = arr[:i] + arr[i+1:] # Remove current item
        if is_report_safe(modified_report, min_diff, max_diff):
            return True

    # Try by removing last item
    if is_report_safe(arr[:-1], min_diff, max_diff):
        return True
    
    return False  


def main():
    reports = process_file("02.txt", num_col=1, split=True)
    reports = [[int(x) for x in sublist] for sublist in reports]
    
    part_one_safe_reports = sum(
        1 for report in reports if iterate_report_combos(report, 0, 4, False)
    )
    part_two_safe_reports = sum(
        1 for report in reports if iterate_report_combos(report, 0, 4, True)
    )

    print(f"Part 1 answer: {part_one_safe_reports}") # 257
    print(f"Part 2 answer: {part_two_safe_reports}") # 328


if __name__ == "__main__":
    main()