#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct expenses
{
    int* data;
    size_t size;
};

struct expenses open_file(const char* filepath)
{
    // initialize arr to store data
    size_t size = 200;
    int* data = realloc(NULL, size*sizeof(int));
    size_t pos = 0;

    // open file
    FILE* f = fopen(filepath, "r");
    if (f == NULL)
    {
        perror("Input file cannot be opened \n");
        abort();
    }

    // iterate through lines
    int num = 0;
    int digit = 0;
    int chr;
    do
    {
        chr = fgetc(f);
        
        // encounter a num digit in file
        if (isdigit(chr))
        {
            num = num * 10 + (chr - '0');
            digit += 1;
        }
        // finished getting one num
        else if (digit > 0)
        {
            if (pos == size)
            {
                perror("Out of error check this \n");
                abort();
            }
            data[pos++] = num;
            num = 0;
            digit = 0;
        }
    }
    while (chr != EOF);
    
    // close file
    fclose(f);
    
    struct expenses inp = { .data = data, .size = pos };
    return inp;
}

// get product of the 2 nums that sum to 2020
int part_one(const struct expenses* report)
{
    const int* data = report->data;
    
    for (int i = 0; i < report->size; ++i)
    {
        for (int j = 0; j < report->size; ++j)
        {
            if (data[i] + data[j] == 2020)
                return data[i] * data[j];
        }
    }
}

// get product of the 3 nums that sum to 2020
int part_two(const struct expenses* report)
{
    const int* data = report->data;
    
    for (int i = 0; i < report->size; ++i)
    {
        for (int j = 0; j < report->size; ++j)
        {
            for (int k = 0; k < report->size; ++k)
            {
                if (data[i] + data[j] + data[k] == 2020)
                    return data[i] * data[j] * data[k];
            }
        }
    }
}

int main()
{
    struct expenses inp = open_file("../aoc-inputs/2020/01.txt");

    printf("Part one output: %d", part_one(&inp)); // 982464
    printf("Part two output: %d", part_two(&inp)); // 162292410
    
    free(inp.data);
    return 0;
}
