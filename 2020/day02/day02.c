#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct answers {
    int part_one;
    int part_two;
};

int part_one_validity(int min_amt, int max_amt, char letter, char *password)
{
    int curr_amt = 0;
    
    char *pwd_pos;
    for (pwd_pos = password; *pwd_pos != '\0'; pwd_pos++)
    {
        if (*pwd_pos == letter)
        {
            curr_amt++;
            
            if (curr_amt > max_amt)
            {
                return 0;
            }
        }
    }

    return curr_amt >= min_amt ? 1 : 0;
}

int part_two_validity(int first_pos, int second_pos, char letter, char *password)
{
    int curr_amt = 0;
    return (password[first_pos-1] == letter) != (password[second_pos-1] == letter) ? 1 : 0;
}

struct answers process_password_policies(const char *filepath)
{
    // open file
    FILE *f = fopen(filepath, "r");
    if (f == NULL)
    {
        perror("Input file cannot be opened \n");
        abort();
    }

    // read through file
    int num_valid, num_valid2 = 0;
    int min_amt, max_amt = 0;
    char letter, password[50];

    while (fscanf(f, "%d-%d %c: %s\n", &min_amt, &max_amt, &letter, password) > 0)
    {
        num_valid += part_one_validity(min_amt, max_amt, letter, password);
        num_valid2 += part_two_validity(min_amt, max_amt, letter, password);
    }

    struct answers ret = { .part_one = num_valid, .part_two = num_valid2 };
    return ret;
}

int main()
{
    struct answers all_answers = process_password_policies("passwords.txt");

    printf("Part one output: %d\n", all_answers.part_one); // 506
    printf("Part two output: %d", all_answers.part_two); // 443

    return 0;
}
