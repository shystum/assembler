from sys import argv
from constants import opcode, registers
from op_func import *

input_file = argv[1]
instructions = []

with open(input_file) as file:
    instructions = file.readlines()

# clean whitespaces and split each instruction
# [['var', 'X'], ['mov', 'R1', '$10']]
instructions = [i.strip().split() for i in instructions]


def instructionToBinary(instruction: list[str]) -> str:
    # add reg1 reg2 reg3
    binary_instruction = ''
    binary_instruction += opcode[instruction[0]][0]
    instruction_type = ''
    if instruction[0] != 'mov':
        instruction_type = opcode[instruction[0]][1]
    else:
        if instruction[2][0] == '$':
            instruction_type = 'B'
        else:
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


print(instructions)
