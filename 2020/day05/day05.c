#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define NUM_ROWS 128
#define NUM_COLS 8
#define NUM_ROW_SPECS 7
#define NUM_COL_SPECS 3

struct answers
{
    int part_one;
    int part_two;
};

int get_row_col_num(char *this_specifiers, int is_row)
{
    int this_min = 0;
    int this_max = is_row ? NUM_ROWS-1 : NUM_COLS-1;
    
    int i_max = is_row ? NUM_ROW_SPECS : NUM_COL_SPECS;
    for (int i = 0; i < i_max; i++)
    {
        float this_mid = (this_min + this_max) / 2.0;
        
        char min_specifier = is_row ? 'F' : 'L';
        if (this_specifiers[i] == min_specifier)
        {
            this_max = (int)floor(this_mid);
        }
        else // 'B' / 'R'
        {
            this_min = (int)ceil(this_mid);
        }
    }
    if (this_min != this_max)
    {
        fprintf(stderr, "Row/col num finding did not converge on a number\n");
        exit(1);
    }
    
    return this_min;
}

int get_seat_id(int row_num, int col_num)
{
    return (row_num * 8) + col_num;
}

struct answers process_boarding_passes(const char *filepath)
{
    // open file
    FILE *f = fopen(filepath, "r");
    if (f == NULL)
    {
        fprintf(stderr, "Input file cannot be opened\n");
        exit(1);
    }
    
    // part 1 answer
    int max_seat_id = -1;
    
    // read through file
    char row_specifiers[NUM_ROW_SPECS+1], col_specifiers[NUM_COL_SPECS+1]; // need an extra space to store null terminator
    while (fscanf(f, "%7s%3s\n", row_specifiers, col_specifiers) > 0)
    {
        int row_num = get_row_col_num(row_specifiers, 1);
        int col_num = get_row_col_num(col_specifiers, 0);
        int seat_id = get_seat_id(row_num, col_num);
        
        // part 1 logic
        max_seat_id = seat_id > max_seat_id ? seat_id : max_seat_id;
    }
    
    
    // close file
    fclose(f);
    
    struct answers ret = { .part_one = max_seat_id, .part_two = -1 };
    return ret;
}

int main()
{
    struct answers all_answers = process_boarding_passes("passes.txt");

    printf("Part one output: %d\n", all_answers.part_one);
    printf("Part two output: %d\n", all_answers.part_two);    

    return 0;
}
