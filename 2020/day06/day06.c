#include <ctype.h>
#include <regex.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINE 128

struct answers
{
    int part_one;
    int part_two;
};

int char_to_int(char ch)
{
    char str[2] = "\0";
    str[0] = ch;
    return strtol(str, NULL, 36) - 10;
}


struct answers process_ans(const char *filepath)
{
    // open file
    FILE *f = fopen(filepath, "r");
    if (f == NULL)
    {
        fprintf(stderr, "Input file cannot be opened\n");
        exit(1);
    }
    
    // part 1
    int group_ans_sum = 0;
    // part 2
    int group_all_ans_sum = 0;
    int curr_group_members_num = 0;
    
    // read through file
    int ch;
    char prev_ch;
    int yes_answers[26] = {0};
    
    while ((ch = fgetc(f)) != EOF)
    {
        
        if (ch != '\n')
        {
            yes_answers[char_to_int(ch)]++;
        }
        else
        {
            if (ch == '\n')
            {
                if (prev_ch == '\n')
                {
                    // process previous group, since they are done
                    int curr_group_sum = 0;
                    int curr_group_all_sum = 0;
                    for (int i = 0; i < 26; i++)
                    {
                        if (yes_answers[i] > 0)
                        {
                            curr_group_sum++;
                        }
                        if (yes_answers[i] == curr_group_members_num)
                        {
                            curr_group_all_sum++;
                        }
                    }
                    group_ans_sum += curr_group_sum;
                    group_all_ans_sum += curr_group_all_sum;
                    
                    // reset group answer tracker
                    for (int i = 0; i < 26; i++)
                    {
                        yes_answers[i] = 0;   
                    }
                    curr_group_members_num = 0;
                }
                else {
                    curr_group_members_num++;
                }
            }
        }
        
        prev_ch = ch;
    }
    
    // hacky way to process last group
    // process previous group, since they are done
    int curr_group_sum = 0;
    int curr_group_all_sum = 0;
    for (int i = 0; i < 26; i++)
    {
        if (yes_answers[i] > 0)
        {
            curr_group_sum++;
        }
        if (yes_answers[i] == curr_group_members_num+1) // hacky fix on group num count
        {
            curr_group_all_sum++;
        }
    }
    group_ans_sum += curr_group_sum;
    group_all_ans_sum += curr_group_all_sum;
    
    // close file
    fclose(f);

    struct answers ret = { .part_one = group_ans_sum, .part_two = group_all_ans_sum };
    return ret;
}

int main()
{
    struct answers all_answers = process_ans("answers.txt");

    printf("Part one output: %d\n", all_answers.part_one); // 6161
    printf("Part two output: %d\n", all_answers.part_two); // 2971, need to remove last newline from input txt idk

    return 0;
}
