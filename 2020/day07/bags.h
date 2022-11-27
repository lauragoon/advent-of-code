#ifndef __BAGS_H__
#define __BAGS_H__

#define MAX_BAG_NAME 30

typedef struct inner_bag
{
    char name[MAX_BAG_NAME];
    struct inner_bag *next;
} inner_bag_t;

typdef struct outer_bag
{
    char name[MAX_BAG_NAME];
    int num_inner_bags;
    inner_bag_t *inside;
    struct outer_bag *next;
} outer_bag_t;


void push_outer_bag(outer_bag_t **head, char bag_name[MAX_BAG_NAME]);
void push_inner_bag(inner_bag_t **head, char bag_name[MAX_BAG_NAME]);

outer_bag_t *find_bag(outer_bag_t **head, char bag_name[MAX_BAG_NAME]);

void print_bags(outer_bag_t **head);


#endif
