#!/usr/bin/env python3

import argparse

# TODO: import some to source and some to config
null_symbol = '#'
prefix_lenght = 5
suffix_lenght = 5
end_state = 'q0'
init_state = 'q1'
commands = []

with open('docs/description.txt') as description_file:
    description = description_file.read()

args_parser = argparse.ArgumentParser(description=description)
args_parser.add_argument('input_file', help='The file to run')
# args_parser.add_argument('--verbose') # TODO

args = args_parser.parse_args()
source_file = open(args.input_file)
source = source_file.readlines()
source_file.close()

for line in source:
    line = line.split()
    match line[0]:
        case 'start_pos':
            start_pos = int(line[1])
        case 'tape':
            tape_str = null_symbol * prefix_lenght + line[1] + null_symbol * suffix_lenght
            tape = []
            for char in tape_str:
                tape.append(char)
        case 'com':
            init_state = line[1]
            init_value = line[2]
            final_state = line[3]
            final_value = line[4]
            com = [init_state, init_value, final_state, final_value]
            if len(line) == 6: cursor = line[5]; com.append(cursor)
            else: com.append('C')
            commands.append(com)

current_pos = len(tape) - suffix_lenght - 1
current_pos = start_pos + prefix_lenght
current_state = init_state
states = set([end_state, init_state])  
for command in commands:
    states.add(command[0])
    states.add(command[2])

#TODO: states verification
# print('STATES', states)

# steps = 0 #TODO
while current_state != end_state:
    # steps += 1
    for command in commands:
        if command[0] == current_state and command[1] == tape[current_pos]:
                current_command = command
    current_state = current_command[2]
    tape[current_pos] = current_command[3]
    if current_command[4] == 'L':
        current_pos -= 1
    if current_command[4] == 'R':
        current_pos += 1
    if current_command[4] == 'C':
        pass

    # print('Current Program Step ->', steps, end='\r') 
print('The program was completed successfully!')
print((''.join(tape)).replace(null_symbol, ''))