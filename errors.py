from assembler import find_instruction_type, total_lines
from constants import opcode, registers, line_count
import assembler
import constants

hlt_count = 0


def InvalidInstructionError(instruction: str) -> str:
    instruction_type = find_instruction_type(instruction)
    if instruction[0] not in opcode and instruction_type != "var" and instruction_type != 'label':
        return f"InvalidInstructionError: Invalid instruction in line number {constants.line_count}. Is there any typo in the instruction?"
    else:
        return ""


def InvalidRegisterError(instruction: str = assembler.instruction) -> str:
    instruction_type = find_instruction_type(instruction)
    if instruction_type == "A" or instruction_type == "C":
        if not all([i in registers for i in instruction[1:]]):
            return f"InvalidRegisterError: Invalid register in line number {constants.line_count}. Is there any typo in the regsiter name?"
    elif instruction_type == "B" or instruction_type == "D":
        if instruction[1] not in registers:
            return f"InvalidRegisterError: Invalid register in line number {constants.line_count}. Is there any typo in the regsiter name?"
    return ""


def HaltError(instructions: list[list] = assembler.instruction) -> str:
    hltCount = 0
    for c in instructions:
        if c:
            if c[0] == "hlt":
                hltCount += 1
    if hltCount > 1:
        return "HaltError: More than one hlt instruction found"

    elif hltCount == 0:
        return "HaltError: No hlt instruction found"
    for i in range(len(instructions)-1, 0, -1):
        if instructions[i]:
            if instructions[i][0] != 'hlt':
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


def IllegalImmediateValueError(instruction: str) -> str:
    instruction_type = find_instruction_type(instruction)
    if instruction_type == "B":
        val = int(instruction[2][1:])
        if val < 0 or val > 127:
            return f"IllegalImmediateValueError: Illegal immediate value in line number {constants.line_count}"
    return ""


def VariablesNotInBeginning(instructions: list[list] = assembler.instruction):
    flagger = 0
    for i in instructions:
        if i:
            if flagger == 0 and i[0] != 'var':
                flagger = 1
            elif flagger == 1 and i[0] == 'var':
                return "VariablesNotInBeginning: Variables not in the beginning of the file"
    return ""


instruction_error_functions_list = [
    InvalidInstructionError, InvalidRegisterError, UndefinedVariableError]
file_error_functions_list = [HaltError, VariablesNotInBeginning]
