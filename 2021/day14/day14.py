'''
--- PART ONE ---
'''

def read_file(filename):
    template = ''
    rules = {}

    with open(filename) as my_file:
        for line in my_file:
            line = line.rstrip()

            # pair rule
            if '->' in line:
                line_split = line.split(' -> ')
                line_pair = line_split[0]
                line_result = line_split[1]
                rules[line_pair] = line_result

            # template
            elif len(line) > 0:
                template = line

    return template, rules

def apply_rules(template, rules, steps):
    ret_str = template

    # repeat for x amount of steps
    for step in range(steps):
        new_str = '' # new polymer

        for i in range(len(ret_str)-1):
            curr_pair = ret_str[i:i+2] # pair
            insertion = rules[curr_pair] # insertion via rule
            new_str += curr_pair[0]
            new_str += insertion

        new_str += ret_str[-1] # add last part of last pair

        ret_str = new_str # replace tracked polymer

    return ret_str

def part_one(template, rules, steps):
    count_dict = {} 
    polymer = apply_rules(template, rules, steps)

    for i in range(len(polymer)):
        if polymer[i] in count_dict.keys():
            count_dict[polymer[i]] += 1
        else:
            count_dict[polymer[i]] = 1

    return max(count_dict.values()) - min(count_dict.values())

template, rules = read_file('polymer.txt')
print(part_one(template, rules, 10)) # 2703
