#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void process_trees(const char *filepath, long *ret_arr)
{
    // open file
    FILE *f = fopen(filepath, "r");
    if (f == NULL)
    {
        perror("Input file cannot be opened\n");
        abort();
    }

    // read through file
    char tree_map[323][31];
    char temp[31];
    
    for (int i = 0; i < 323; i++)
    {
        fscanf(f, "%s\n", temp);
        
        for (int j = 0; j < 31; j++)
        {
            tree_map[i][j] = temp[j];
            
        }
    }

    // count trees
    for (int i = 0; i < 5; i++)
        ret_arr[i] = 0;
    
    // part 1 - right 3 down 1
    int horz_slope1 = 3;
    int ver_slope1 = 1;
    int curr_i = 0;
    int curr_j = 0;

    while (curr_i < 323)
    {
        if (tree_map[curr_i][curr_j] == '#')
            ret_arr[1]++;

        // new coords
        curr_i += ver_slope1;
        curr_j += horz_slope1;
        if (curr_j >= 31)
            curr_j %= 31;
    }
     
    // count trees - part 2
    int horz_slope[4] = {1, 5, 7, 1};
    int ver_slope[4] = {1, 1, 1, 2};

    for (int iter = 0; iter < 4; iter++)
    {
        curr_i = 0;
        curr_j = 0;
        int ret_idx = iter == 0 ? iter : iter+1;
        
        while (curr_i < 323)
        {
            if (tree_map[curr_i][curr_j] == '#')
                ret_arr[ret_idx]++;

            // new coords
            curr_i += ver_slope[iter];
            curr_j += horz_slope[iter];
            if (curr_j >= 31)
                curr_j %= 31;
        }
    }

    // close file
    fclose(f);
    return;
}

int main()
{
    long ans[5];
    
    process_trees("trees.txt", ans);
    printf("Part one output: %ld\n", ans[1]); // 286

    printf("Part two output: %ld\n", ans[0]*ans[1]*ans[2]*ans[3]*ans[4]); // 3638606400

    return 0;
}
