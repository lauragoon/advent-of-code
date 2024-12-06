import re

from helpers import process_file


def main():
    memory_lines = process_file("03.txt")

    sum_product = 0
    for memory in memory_lines:
        memory = memory
        regex_pattern = r"mul\((\d+),(\d+)\)"
        match = re.findall(regex_pattern, memory)

        match = [[int(x) for x in tup] for tup in match]

        for mul_coeffs in match:
            sum_product += mul_coeffs[0] * mul_coeffs[1]

    print(f"Part 1 answer: {sum_product}") # 167090022


if __name__ == "__main__":
    main()