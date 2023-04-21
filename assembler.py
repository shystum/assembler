from sys import argv
from constants import opcode

input_file = argv[1]
instructions = []

with open(input_file) as file:
    instructions = file.readlines()

# clean whitespaces and split each instruction
# [['var', 'X'], ['mov', 'R1', '$10']]
instructions = [i.strip().split() for i in instructions]


def instructionToBinary(instruction: list[int]) ->  str:
    # add reg1 reg2 reg3
    binary_instruction = ''    
    binary_instruction += opcode[instruction][0]

    if opcode[instruction][1] == "A":
        pass
    elif opcode[instruction][1] == "B":
        pass



print(instructions)

