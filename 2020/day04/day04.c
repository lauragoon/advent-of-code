#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define LEN_FILE 1024
#define MAX_LINE 128
#define NUM_PASSPORTS 257

int process_passports(const char *filepath)
{
    // open file
    FILE *f = fopen(filepath, "r");
    if (f == NULL)
    {
        perror("Input file cannot be opened\n");
        abort();
    }
    
    // read through file
    char line[MAX_LINE];
    int passport_fields[8] = {0, 0, 0, 0, 0, 0, 0, 0};
    int num_valid = 0;
    
    while (fgets(line, MAX_LINE, f))
    {
        // process current passport
        char *tok = strtok(line, ": \n");
        while (tok != NULL)
        {
            if (strcmp(tok, "byr") == 0)
            {
                tok = strtok(NULL, ": \n");
                passport_fields[0] = 1;
            }
            else if (strcmp(tok, "iyr") == 0)
            {
                tok = strtok(NULL, ": \n");
                passport_fields[1] = 1;
            }
            else if (strcmp(tok, "eyr") == 0)
            {
                tok = strtok(NULL, ": \n");
                passport_fields[2] = 1;
            }
            else if (strcmp(tok, "hgt") == 0)
            {
                tok = strtok(NULL, ": \n");
                passport_fields[3] = 1;
            }
            else if (strcmp(tok, "hcl") == 0)
            {
                tok = strtok(NULL, ": \n");
                passport_fields[4] = 1;
            }
            else if (strcmp(tok, "ecl") == 0)
            {
                tok = strtok(NULL, ": \n");
                passport_fields[5] = 1;
            }
            else if (strcmp(tok, "pid") == 0)
            {
                tok = strtok(NULL, ": \n");
                passport_fields[6] = 1;
            }
            else if (strcmp(tok, "cid") == 0)
            {
                tok = strtok(NULL, ": \n");
                passport_fields[7] = 1;
            }
            else
            {
                perror("Encountered unexpected token\n");
                abort();
            }
            
            tok = strtok(NULL, ": \n");
        }

        // new passport now
        if (strlen(line) == 1)
        {
            // process prev done passport
            if (passport_fields[0] == 1 && passport_fields[1] == 1 && passport_fields[2] == 1 && passport_fields[3] == 1 && passport_fields[4] == 1 && passport_fields[5] == 1 && passport_fields[6] == 1)
            {
                num_valid++;
            }

            // reset for new passport
            for (int i = 0; i < 8; i++)
                passport_fields[i] = 0;
        }
    }
    
    // close file
    fclose(f);
    
    return num_valid;
}

int main()
{
    int part_one_ans = process_passports("passports.txt");

    printf("Part one output: %d\n", part_one_ans); // 206    

    return 0;
}
