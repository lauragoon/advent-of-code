#ifndef __BAGS_H__
#define __BAGS_H__


typedef struct inner_bag
{
    char name[30];
    struct inner_bag *next;
} inner_bag_t;

typdef struct outer_bag
{
    char name[30];
    int num_inner_bags;
    inner_bag_t *inside;
    struct outer_bag *next;
} outer_bag_t;

outer_bag_t **init_bag_list(void);

void push_outer_bag(outer_bag_t **head, char bag_name[30]);
void push_inner_bag(inner_bag_t **head, char bag_name[30]);

outer_bag_t *find_bag(outer_bag_t **head, char bag_name[30]);

void print_bags(outer_bag_t **head);

#endif
