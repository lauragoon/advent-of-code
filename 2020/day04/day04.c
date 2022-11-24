#include <ctype.h>
#include <regex.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define LEN_FILE 1024
#define MAX_LINE 128
#define NUM_PASSPORTS 257

struct answers
{
    int part_one;
    int part_two;
};

struct answers process_passports(const char *filepath)
{
    // open file
    FILE *f = fopen(filepath, "r");
    if (f == NULL)
    {
        fprintf(stderr, "Input file cannot be opened\n");
        exit(1);
    }
    
    // read through file
    char line[MAX_LINE];
    int passport_fields[8] = {0, 0, 0, 0, 0, 0, 0, 0};
    int strict_passport_fields[8] = {0, 0, 0, 0, 0, 0, 0, 0};
    int num_valid = 0;
    int num_strict_valid = 0;
    
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
                
                int byr_val = atoi(tok);
                if (byr_val >= 1920 && byr_val <= 2002)
                    strict_passport_fields[0] = 1;
            }
            else if (strcmp(tok, "iyr") == 0)
            {
                tok = strtok(NULL, ": \n");
                passport_fields[1] = 1;
                
                int iyr_val = atoi(tok);
                if (iyr_val >= 2010 && iyr_val <= 2020)
                    strict_passport_fields[1] = 1;
            }
            else if (strcmp(tok, "eyr") == 0)
            {
                tok = strtok(NULL, ": \n");
                passport_fields[2] = 1;

                int eyr_val = atoi(tok);
                if (eyr_val >= 2020 && eyr_val <= 2030)
                    strict_passport_fields[2] = 1;
            }
            else if (strcmp(tok, "hgt") == 0)
            {
                tok = strtok(NULL, ": \n");
                passport_fields[3] = 1;
                
                regex_t hgt_regex;
                int hgt_regex_ret;
                char hgt_msgbuf[100];
                hgt_regex_ret = regcomp(&hgt_regex, "^[0-9]+(in|cm)$", REG_EXTENDED); // compile regex
                if (hgt_regex_ret)
                {
                    fprintf(stderr, "Could not compile hgt regex\n");
                    exit(1);
                }
                hgt_regex_ret = regexec(&hgt_regex, tok, 0, NULL, 0); // execute regex
                if (!hgt_regex_ret)
                {
                    const char *hgt_unit = &tok[strlen(tok)-2];
                    long hgt_val = strtol(tok, &tok, 10);
                    if ((strcmp(hgt_unit, "cm") == 0 && (hgt_val >= 150 && hgt_val <= 193)) ||
                        (strcmp(hgt_unit, "in") == 0 && (hgt_val >= 59 && hgt_val <= 76)))
                    {
                        printf("%ld", hgt_val);
                        printf("\n");
                        printf(hgt_unit);
                        printf("\n\n");
                        strict_passport_fields[3] = 1;   
                    }
                }
                else if (hgt_regex_ret == REG_NOMATCH)
                {
                    ;
                }
                else
                {
                    regerror(hgt_regex_ret, &hgt_regex, hgt_msgbuf, sizeof(hgt_msgbuf));
                    fprintf(stderr, "Regex match for hgt failed: %s\n", hgt_msgbuf);
                    exit(1);
                }
                regfree(&hgt_regex); // free regex
            }
            else if (strcmp(tok, "hcl") == 0)
            {
                tok = strtok(NULL, ": \n");
                passport_fields[4] = 1;

                regex_t hcl_regex;
                int hcl_regex_ret;
                char hcl_msgbuf[100];
                hcl_regex_ret = regcomp(&hcl_regex, "^[#][0-9|a-f][0-9|a-f][0-9|a-f][0-9|a-f][0-9|a-f][0-9|a-f]$", REG_EXTENDED); // compile regex
                if (hcl_regex_ret)
                {
                    fprintf(stderr, "Could not compile hcl regex\n");
                    exit(1);
                }
                hcl_regex_ret = regexec(&hcl_regex, tok, 0, NULL, 0); // execute regex
                if (!hcl_regex_ret)
                {
                    strict_passport_fields[4] = 1;
                }
                else if (hcl_regex_ret == REG_NOMATCH)
                {
                    ;
                }
                else
                {
                    regerror(hcl_regex_ret, &hcl_regex, hcl_msgbuf, sizeof(hcl_msgbuf));
                    fprintf(stderr, "Regex match for hcl failed: %s\n", hcl_msgbuf);
                    exit(1);
                }
                regfree(&hcl_regex); // free regex
            }
            else if (strcmp(tok, "ecl") == 0)
            {
                tok = strtok(NULL, ": \n");
                passport_fields[5] = 1;

                if (strcmp(tok, "amb") == 0 || strcmp(tok, "blu") == 0 || strcmp(tok, "brn") == 0 || strcmp(tok, "gry") == 0 || strcmp(tok, "grn") == 0 || strcmp(tok, "hzl") == 0 || strcmp(tok, "oth") == 0)
                {
                    strict_passport_fields[5] = 1;
                }
            }
            else if (strcmp(tok, "pid") == 0)
            {
                tok = strtok(NULL, ": \n");
                passport_fields[6] = 1;

                regex_t pid_regex;
                int pid_regex_ret;
                char pid_msgbuf[100];
                pid_regex_ret = regcomp(&pid_regex, "[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]", 0); // compile regex
                if (pid_regex_ret)
                {
                    fprintf(stderr, "Could not compiel pid regex\n");
                    exit(1);
                }
                pid_regex_ret = regexec(&pid_regex, tok, 0, NULL, 0); // execute regex
                if (!pid_regex_ret)
                {
                    strict_passport_fields[6] = 1;
                }
                else if (pid_regex_ret == REG_NOMATCH)
                {
                    ;
                }
                else
                {
                    regerror(pid_regex_ret, &pid_regex, pid_msgbuf, sizeof(pid_msgbuf));
                    fprintf(stderr, "Regex match for pid failed: %s\n", pid_msgbuf);
                    exit(1);
                }
                regfree(&pid_regex); // free regex
            }
            else if (strcmp(tok, "cid") == 0)
            {
                tok = strtok(NULL, ": \n");
                passport_fields[7] = 1;
                strict_passport_fields[7] = 1;
            }
            else
            {
                fprintf(stderr, "Encountered unexpected token\n");
                exit(1);
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
            
            if (strict_passport_fields[0] == 1 && strict_passport_fields[1] == 1 && strict_passport_fields[2] == 1 && strict_passport_fields[3] == 1 && strict_passport_fields[4] == 1 && strict_passport_fields[5] == 1 && strict_passport_fields[6] == 1)
            {
                num_strict_valid++;
            }
            
            // reset for new passport
            for (int i = 0; i < 8; i++)
            {
                passport_fields[i] = 0;
                strict_passport_fields[i] = 0;
            }
        }
    }
    
    // close file
    fclose(f);

    struct answers ret = { .part_one = num_valid, .part_two = num_strict_valid };
    return ret;
}

int main()
{
    struct answers all_answers = process_passports("passports.txt");

    printf("Part one output: %d\n", all_answers.part_one); // 206
    printf("Part two output: %d\n", all_answers.part_two);    

    return 0;
}
