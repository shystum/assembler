from constants import registers
from convertors import *
import constants
total_bits = 16
opcode_bits = 5
register_bits = 3
immediate_value_bits = 7
memory_addr_bits = 7


def typeA(instruction: list[str]) -> str:
    binary_instruction = ''
    unused_bits = '0'*(total_bits - opcode_bits - register_bits * 3)
    binary_instruction += unused_bits
    binary_instruction += registers[instruction[1]]
    binary_instruction += registers[instruction[2]]
    binary_instruction += registers[instruction[3]]
    return binary_instruction


def typeB(instruction: list[str]) -> str:
    binary_instruction = ''
    unused_bits = '0'*(total_bits - opcode_bits -
                       register_bits - immediate_value_bits)
    binary_instruction += unused_bits
    binary_instruction += registers[instruction[1]]
    # $10 -> 10 -> 0b1010 -> 1010 -> 0000000000001010
    binary_instruction += bin(int(instruction[2][1:])%128
                              )[2:].zfill(immediate_value_bits)
    return binary_instruction


def typeC(instruction: list[str]) -> str:
    binary_instruction = ''
    unused_bits = '0'*(total_bits - opcode_bits - register_bits * 2)
    binary_instruction += unused_bits
    binary_instruction += registers[instruction[1]]
    binary_instruction += registers[instruction[2]]

    return binary_instruction


def typeD(instruction: list[str]) -> str:
    binary_instruction = ''
    unused_bits = '0'*(total_bits - opcode_bits -
                       register_bits - memory_addr_bits)
    binary_instruction += unused_bits
    binary_instruction += registers[instruction[1]]
    binary_instruction += constants.current_variables[instruction[2]]
    return binary_instruction


def typeE(instruction: list[str], instructions: list[list[str]]) -> str:
    for i in range(len(instructions)):
        if ':' in instructions[i][0]:
            if instructions[i][0][:-1] not in constants.current_labels:
                # print(instructions[i][0][:-1], i-constants.var_count)
                # print(instructions[i])
                constants.current_labels[instructions[i][0][:-1]] = integerToSevenBitBinary(i-constants.var_count)
    binary_instruction = ''
    unused_bits = '0'*(total_bits - opcode_bits - memory_addr_bits)
    binary_instruction += unused_bits
    binary_instruction += (constants.current_labels[instruction[1]])
    return binary_instruction


def typeF(instruction: list[str]) -> str:
    binary_instruction = ''
    unused_bits = '0'*(total_bits - opcode_bits)
    binary_instruction += unused_bits
    return binary_instruction
