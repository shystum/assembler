from assembler import find_instruction_type, total_lines
from constants import opcode, registers, line_count
import assembler
import constants

hlt_count = 0


def InvalidInstructionError(instruction: str) -> str:
    if instruction[0] not in opcode and instruction[0] != "var":
        return f"InvalidInstructionError: Invalid instruction in line number {constants.line_count}. Is there any typo in the instruction?"
    else:
        return ""


def InvalidRegisterError(instructions: str = assembler.instructions) -> str:
    instruction_type = find_instruction_type(instructions)
    if instruction_type == "A" or instruction_type == "C":
        if not all([i in registers for i in instructions[1:]]):
            return f"InvalidRegisterError: Invalid register in line number {constants.line_count}. Is there any typo in the regsiter name?"
    elif instruction_type == "B" or instruction_type == "D":
        if instructions[1] not in registers:
            return f"InvalidRegisterError: Invalid register in line number {constants.line_count}. Is there any typo in the regsiter name?"
    return ""


def HaltError(instruction: list[list]) -> str:
    hltCount = 0
    for c in instruction:
        if c:
            if c[0] == "hlt":
                hltCount += 1
    if hltCount > 1:
        return "HaltError: More than one hlt instruction found"

    elif hltCount == 0:
        return "HaltError: No hlt instruction found"
    for i in range(len(instruction)-1,0,-1):
        if instruction[i]:
            if instruction[i][0] != 'hlt':
                return f"HaltError: hlt instruction not at last line. hlt instruction found in line {i}"
            else:
                return ""
    return ""

def UndefinedVariableError(instruction: str) -> str:
    instruction_type = find_instruction_type(instruction)
    if instruction_type == "D":
        if instruction[2] in constants.current_variables:
            return ''
        else:
            return f"UndefinedVariableError: Undefined variable in line number {constants.line_count}. Is there any typo in the variable name?"
    elif instruction_type == "E":
        if instruction[1] in constants.current_variables:
            return ''
        else:
            return f"UndefinedVariableError: Undefined variable in line number {constants.line_count}. Is there any typo in the variable name?"
    return ''


error_functions_list = [InvalidInstructionError, InvalidRegisterError, UndefinedVariableError] 