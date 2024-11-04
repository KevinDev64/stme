#!/usr/bin/env python3

import argparse

# TODO: import some to source and some to config
null_symbol = '#'
prefix_lenght = 15
suffix_lenght = 15
end_state = 'q0'
init_state = 'q1'
commands = []
tape = []
start_pos = 0
is_other_start_pos = False

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
    if len(line) != 0:
        match line[0]:
            case 'null_symbol':
                null_symbol = line[1]
            case 'prefix_lenght':
                prefix_lenght = int(line[1])
            case 'suffix_lenght':
                suffix_lenght = int(line[1])
            case 'start_pos':
                start_pos = int(line[1])
                is_other_start_pos = True
            case 'tape':
                tape_str = null_symbol * prefix_lenght + line[1] + null_symbol * suffix_lenght
                tape = []
                print(tape_str)
                for char in tape_str:
                    tape.append(char)
            case 'com':
                com_init_state = line[1]
                com_init_value = line[2]
                com_final_state = line[3]
                com_final_value = line[4]
                com = [com_init_state, com_init_value, com_final_state, com_final_value]
                if len(line) == 6: cursor = line[5]; com.append(cursor)
                else: com.append('C')
                commands.append(com)

current_pos = len(tape) - suffix_lenght - 1
if is_other_start_pos: current_pos = start_pos + prefix_lenght - 1

current_state = init_state
states = set([end_state, init_state])  
for command in commands:
    states.add(command[0])
    states.add(command[2])

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