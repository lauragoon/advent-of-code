#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "bags.h"

#define MAX_LINE 128

struct answers
{
    int part_one;
    int part_two;
};


struct answers process_rules(const char *filepath)
{
    // initialize vars
    outer_bag_t *outer_head = NULL;
    
    // open file
    FILE *f = fopen(filepath, "r");
    if (f == NULL)
    {
        fprintf(stderr, "Input file cannot be opened\n");
        exit(1);
    }
    
    // read through file
    char line[MAX_LINE];
    
    while (fgets(line, MAX_LINE, f))
    {
        // outer bag
        char adj[MAX_BAG_NAME];
        char color[MAX_BAG_NAME];
        char curr_outer_bag_name[MAX_BAG_NAME];
        
        sscanf(line, "%s %s", adj, color);
        strcpy(curr_outer_bag_name, adj);
        strcat(curr_outer_bag_name, " ");
        strcat(curr_outer_bag_name, color);
        
        outer_bag_t *curr_outer_bag = new_outer_bag(curr_outer_bag_name);
        
        // inner bag
        char *bag_ptr = strstr(line, "contain");
        ptr += 8;
        
        //..
    }
    
    // close file
    fclose(f);

    struct answers ret = { .part_one = -1, .part_two = -1 };
    return ret;
}

int main()
{
    struct answers all_answers = process_rules("../../aoc-inputs/2020/07.txt");

    printf("Part one output: %d\n", all_answers.part_one); // 
    printf("Part two output: %d\n", all_answers.part_two); //    

    return 0;
}
