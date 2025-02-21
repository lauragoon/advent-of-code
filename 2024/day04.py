from helpers import process_file


def main():
    word_search = process_file("04.txt", use_single_line=True)
    word_search = [list(x) for x in word_search]

    rows = len(word_search)
    cols = len(word_search[0])

    # Overlapping is ok so sliding 4x4 window, but need to make sure no overcount
    for i in range(rows-3):
        for j in range(cols-3):
            pass


    # horizontal matches keep adding on when go right sliding
    # vertical matches keep adding on when go down sliding

    # x x x x
    # x x x x
    # x x x x
    # x x x x


if __name__ == "__main__":
    main()