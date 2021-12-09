'''
--- Part One ---
'''

def read_file(filename):
    with open(filename) as my_file:
        commands = my_file.read().splitlines()
    return commands


def travel_course(commands):
    depth = 0
    horz = 0
    
    for command in commands:
        dir = command.split(' ')[0]
        amt = int(command.split(' ')[1])

        if dir == 'forward':
            horz += amt
        elif dir == 'down':
            depth += amt
        elif dir == 'up':
            depth -= amt
        else:
            print('ERROR: unexpeced direction input')
            return

    return horz * depth


# cmds = read_file('course.txt')
# print(travel_course(cmds)) # 1694130


'''
--- Part Two ---
'''

def travel_course_with_aim(commands):
    depth = 0
    horz = 0
    aim = 0
    
    for command in commands:
        dir = command.split(' ')[0]
        amt = int(command.split(' ')[1])

        if dir == 'forward':
            horz += amt
            depth += aim * amt
        elif dir == 'down':
            aim += amt
        elif dir == 'up':
            aim -= amt
        else:
            print('ERROR: unexpeced direction input')
            return

    return horz * depth


cmds = read_file('course.txt')
print(travel_course_with_aim(cmds)) # 1698850445
