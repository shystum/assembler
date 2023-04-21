from sys import argv
from constants import opcode,registers

input_file = argv[1]
instructions = []

with open(input_file) as file:
    instructions = file.readlines()

# clean whitespaces and split each instruction
# [['var', 'X'], ['mov', 'R1', '$10']]
instructions = [i.strip().split() for i in instructions]


def instructionToBinary(instruction: list[str]) ->  str:
    # add reg1 reg2 reg3
    binary_instruction = ''    
    binary_instruction += opcode[instruction[0]][0]
    if instruction[0] !='mov':
        if opcode[instruction[0]][1] == "A":
            pass
        elif opcode[instruction[0]][1] == "B":
            pass
        elif opcode[instruction[0]][1] == "C":
            pass
        elif opcode[instruction[0]][1] == "D":
            pass
        elif opcode[instruction[0]][1] == "E":
            pass
        elif opcode[instruction[0]][1] == "F":
            pass
    else:
        if instruction[2][0]=='$':
            pass
    


print(instructions)

