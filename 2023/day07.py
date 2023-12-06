def process_file():
    lines = []
    with open('../aoc-inputs/2023/07.txt') as f:
        lines = f.read().splitlines()

    return lines

def main():
    lines = process_file()

    print(lines)


# ------ RUN SOLUTION ------
main()   # 
