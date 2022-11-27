#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "bags.h"


static outer_bag_t *new_outer_bag(char bag_name[MAX_BAG_NAME])
{
    outer_bag_t *o_bag = malloc(sizeof(outer_bag_t));
    assert(o_bag);
    
    strcpy(o_bag->name, bag_name);
    o_bag->num_inner_bags = 0;
    o_bag->inside = NULL;
    o_bag->next = NULL;
    
    return o_bag;
}

static inner_bag_t *new_inner_bag(char bag_name[MAX_BAG_NAME])
{
    inner_bag_t *i_bag = malloc(sizeof(inner_bag_t));
    assert(i_bag);
    
    strcpy(i_bag->name, bag_name);
    i_bag->next = NULL;
    
    return i_bag;
}

// adds to beginning of LL because it doesn't matter where added
void push_outer_bag(outer_bag_t **head, char bag_name[MAX_BAG_NAME])
{
    outer_bag_t *curr_o_bag = new_outer_bag(bag_name);
    
    curr_o_bag->next = *head;
    *head = curr_o_bag;
}

void push_inner_bag(inner_bag_t **head, char bag_name[MAX_BAG_NAME])
{
    inner_bag_t *curr_i_bag = new_inner_bag(bag_name);
    
    curr_i_bag->next = *head;
    *head = curr_i_bag;
}

outer_bag_t *find_outer_bag(outer_bag_t **head, char bag_name[MAX_BAG_NAME])
{
    outer_bag_t *curr_bag = *head;
    
    while (curr_bag != NULL)
    {
        if (strcmp(bag_name, curr_bag->name) == 0)
        {
            return curr_bag;
        }
        
        curr_bag = curr_bag->next;
    }
    
    return NULL;
}

inner_bag_t *find_inner_bag(inner_bag_t **head, char bag_name[MAX_BAG_NAME])
{
    inner_bag_t *curr_bag = *head;
    
    while (curr_bag != NULL)
    {
        if (strcmp(bag_name, curr_bag->name) == 0)
        {
            return curr_bag;
        }
        
        curr_bag = curr_bag->next;
    }
    
    return NULL;
}

void print_bags(outer_bag_t **head)
{
    outer_bag_t *curr_bag = *head;
    
    while (curr_bag != NULL)
    {
        fprintf(stdout, "[OUTER] %s with %d inner bags\n", curr_bag->name, curr_bag->num_inner_bags);
        curr_bag = curr_bag->next;
    }
}
