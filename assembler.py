from sys import argv
from constants import opcode
from op_func import *
from errors import *

input_file = argv[1]
instructions = []
current_variables = {}
current_address = '0000000'

with open(input_file) as file:
    instructions = file.readlines()

# clean whitespaces and split each instruction
# [['var', 'X'], ['mov', 'R1', '$10']]
instructions = [i.strip().split() for i in instructions]


def instructionToBinary(instruction: list[str]) -> str:
    # add reg1 reg2 reg3
    binary_instruction = ''
    instruction_type = ''
    if instruction[0] == 'var':
        current_variables[instruction[1]] = current_address
        current_address = bin(int(current_address, 2)+1)[2:].zfill(7)
        return ''
    if instruction[0] != 'mov':
        binary_instruction += opcode[instruction[0]][0]
        instruction_type = opcode[instruction[0]][1]
    else:
        if instruction[2][0] == '$':
            binary_instruction += opcode[instruction[0]][0][0]
            instruction_type = 'B'
        else:
            binary_instruction += opcode[instruction[0]][0][1]
            instruction_type = 'C'

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
    for i in instructions:
        if i != '':
            print(instructionToBinary(i))


print(instructions)
