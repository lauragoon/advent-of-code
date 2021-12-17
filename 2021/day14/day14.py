'''
--- PART ONE & TWO ---
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

def max_minus_min(template, rules, steps):
    count_dict = {} 
    polymer = apply_rules(template, rules, steps)

    for i in range(len(polymer)):
        if polymer[i] in count_dict.keys():
            count_dict[polymer[i]] += 1
        else:
            count_dict[polymer[i]] = 1

    return max(count_dict.values()) - min(count_dict.values())

# template, rules = read_file('polymer.txt')
# print(max_minus_min(template, rules, 10)) # 2703

'''
--- PART TWO ---
'''

def convert_to_dict(polymer):
    d = {}

    for i in range(len(polymer)-1):
        curr_pair = polymer[i:i+2]
        if curr_pair not in d.keys():
            d[curr_pair] = 1
        else:
            d[curr_pair] += 1

    return d

def apply_rules2(template, rules, steps):
    ret_dict = convert_to_dict(template)

    # repeat for x amount of steps
    for step in range(steps):
        new_dict = {}
        ret_keys = list(ret_dict.keys())

        for curr_pair in ret_keys:
            insertion = rules[curr_pair] # insertion via rule
            new_pair = curr_pair[0] + insertion
            new_pair2 = insertion + curr_pair[1]
            
            if new_pair not in new_dict.keys():
                new_dict[new_pair] = ret_dict[curr_pair] #+ 1
            else:
                new_dict[new_pair] += ret_dict[curr_pair]
                # new_dict[new_pair] += 1
            
            if new_pair2 not in new_dict.keys():
                new_dict[new_pair2] = ret_dict[curr_pair] #+ 1
            else:
                new_dict[new_pair2] += ret_dict[curr_pair]
                # new_dict[new_pair2] += 1

        ret_dict = new_dict # replace tracked polymer

    return ret_dict

def convert_to_chars(polymer_dict, first, last):
    char_dict = {}

    for pair in polymer_dict.keys():
        first_char = pair[0]
        second_char = pair[1]

        if first_char not in char_dict.keys():
            char_dict[first_char] = polymer_dict[pair]
        else:
            char_dict[first_char] += polymer_dict[pair]
        
        if second_char not in char_dict.keys():
            char_dict[second_char] = polymer_dict[pair]
        else:
            char_dict[second_char] += polymer_dict[pair]

    for c in char_dict.keys():
        char_dict[c] = int(char_dict[c]/2)
        # extra count for beginning and end letters
        if c == last or c == first:
            char_dict[c] += 1
    
    return char_dict

def max_minus_min2(template, rules, steps):
    polymer = apply_rules2(template, rules, steps)
    first_char = template[0]
    last_char = template[-1]

    polymer_char = convert_to_chars(polymer, first_char, last_char)

    return max(polymer_char.values()) - min(polymer_char.values())

template, rules = read_file('polymer.txt')
print(max_minus_min2(template, rules, 40))
