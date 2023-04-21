from sys import argv
from constants import opcode
from op_func import *
from errors import *
import constants

# input_file = argv[1]
input_file = "input.asm"
instruction = []
current_address = '0000000'

with open(input_file) as file:
    instruction = file.readlines()

# print(instructions)
# clean whitespaces and split each instruction
# [['var', 'X'], ['mov', 'R1', '$10']]
total_lines = len(instruction)
instruction = [i.strip().split() for i in instruction]

def find_instruction_type(instruction: list[str]) -> str:
    if instruction[0] == 'var':
        instruction_type = 'var'
    elif ':' in instruction[0]:
        instruction_type = 'label'
    elif instruction[0] != 'mov':
        instruction_type = opcode[instruction[0]][1]
    else:
        if instruction[2][0] == '$':
            instruction_type = 'B'
        else:
            instruction_type = 'C'
    return instruction_type

def instructionToBinary(instruction: list[str]) -> str:
    global current_address
    # add reg1 reg2 reg3
    binary_instruction = ''
    instruction_type = find_instruction_type(instruction)

    if ':' in instruction[0]: 
        constants.current_labels[instruction[0][:-1]] = constants.line_count
        return ''
    if instruction[0] == 'var':
        constants.current_variables[instruction[1]] = current_address
        current_address = bin(int(current_address, 2)+1)[2:].zfill(7)
        return ''
    if instruction[0] != 'mov':
        binary_instruction += opcode[instruction[0]][0]
    else:
        if instruction[2][0] == '$':
            binary_instruction += opcode[instruction[0]][0][0]
        else:
            binary_instruction += opcode[instruction[0]][0][1]

    if instruction_type == "A":
        binary_instruction += typeA(instruction)

    elif instruction_type == "B":
        binary_instruction += typeB(instruction)

    elif instruction_type == "C":
        binary_instruction += typeC(instruction)

    elif instruction_type == "D":
        binary_instruction += typeD(instruction)

    elif instruction_type == "E":
        binary_instruction += typeE(instruction)

    elif instruction_type == "F":
        binary_instruction += typeF(instruction)

    return binary_instruction


def main():
    for error in file_error_functions_list:
            if error() != "":
                print(error(), end='')
                exit()
    for i in instruction:
        if i != []:
            for error in instruction_error_functions_list:
                if error(i) != "":
                    print(error(i), end='')
                    exit()
            if instructionToBinary(i) != '':
                print(instructionToBinary(i))
        constants.line_count += 1


if __name__ == "__main__":
    main()
