from sys import argv
from constants import opcode
from op_func import *
from errors import *
from convertors import *
import constants

# input_file = argv[1]
input_file = "input.asm"
instruction = []

with open(input_file) as file:
    instruction = file.readlines()

# print(instructions)
# clean whitespaces and split each instruction
# [['var', 'X'], ['mov', 'R1', '$10']]
total_lines = len(instruction)
instruction = [i.strip().split() for i in instruction if i.strip() != '']
var_count = len([i for i in instruction if 'var' in i])
print(var_count)
print(total_lines, total_lines-var_count + 1)
current_address = integerToSevenBitBinary(total_lines - var_count + 1)


def find_instruction_type(instruction: list[str]) -> str:
    instruction_type = ''
    if ':' in instruction[0]:
        instruction_type = 'label+'
        instruction = instruction[1:]
    if instruction[0] == 'var':
        instruction_type += 'var'
    elif instruction[0] != 'mov':
        instruction_type += opcode[instruction[0]][1]
    else:
        if instruction[2][0] == '$':
            instruction_type += 'B'
        else:
            instruction_type += 'C'
    return instruction_type


def instructionToBinary(instruction: list[str], instructions: list[list[str]] = instruction) -> str:
    global current_address
    # add reg1 reg2 reg3
    binary_instruction = ''
    instruction_type = find_instruction_type(instruction)

    if 'label' in instruction_type:
        # print(constants.line_count-var_count, instruction[0][:-1])
        constants.current_labels[instruction[0][:-1]] = constants.line_count-var_count
        instruction = instruction[1:]
        instruction_type = instruction_type[-1]
    if instruction[0] == 'var':
        constants.current_variables[instruction[1]] = current_address
        current_address = integerToSevenBitBinary(
            sevenBitBinaryToInteger(current_address)+1)
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
        binary_instruction += typeE(instruction, instructions)

    elif instruction_type == "F":
        binary_instruction += typeF(instruction)

    return binary_instruction


def main():
    for i in instruction:
        if i != []:
            for error in instruction_error_functions_list:
                if error(i) != "":
                    print(error(i), end='')
                    exit()
            if instructionToBinary(i) != '':
                print(instructionToBinary(i))
        constants.line_count += 1

    for error in file_error_functions_list:
        if error() != "":
            print(error(), end='')
            exit()


if __name__ == "__main__":
    main()
