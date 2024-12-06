import re

from helpers import process_file


def scan_memory(
    lines: str,
    regex_pattern: str,
    part_two: bool = False
) -> int:
    """
    Return sum of multiplications from "corrupted memory".

    :param lines: Multiple lines of memory
    :param regex_pattern: Regex pattern to match on
    :capture_str: True if on part two, False otherwise
    :return: Sum of multiplications
    """
    sum_product = 0
    line = "".join(lines)

    # Patterns for do(), don't(), and mul
    mul_pattern = r"mul\((\d+),(\d+)\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"


    if part_two:
        assert regex_pattern == (
            mul_pattern + "|" + do_pattern + "|" + dont_pattern
        )

    mul_enabled = True
    
    for x in re.finditer(regex_pattern, line):

        if re.fullmatch(do_pattern, x.group()):
            mul_enabled = True
        
        elif re.fullmatch(dont_pattern, x.group()):
            mul_enabled = False

        elif mul_enabled:
            sum_product += int(x.group(1)) * int(x.group(2))

    return sum_product

def main():
    memory_lines = process_file("03.txt", use_single_line=True)

    part_one_regex_pattern =  r"mul\((\d+),(\d+)\)"
    part_one_sum = scan_memory(
        lines=memory_lines, regex_pattern=part_one_regex_pattern, part_two=False
    )

    part_two_regex_pattern = r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)"
    part_two_sum = scan_memory(
        lines=memory_lines, regex_pattern=part_two_regex_pattern, part_two=True
    )

    print(f"Part 1 answer: {part_one_sum}") # 167090022
    print(f"Part 2 answer: {part_two_sum}") # 89823704


if __name__ == "__main__":
    main()