from assembler import find_instruction_type
from constants import opcode, registers, line_count
import constants


def InvalidInstructionError(instruction: str) -> str:
    if instruction[0] not in opcode: 
        return f"InvalidInstructionError: Invalid instruction in line number {constants.line_count}. Is there any typo in the instruction?"
    else:
        return ""


def InvalidRegisterError(instruction: str) -> str:
    instruction_type = find_instruction_type(instruction)
    if instruction_type == "A" or instruction_type == "C":
        if not all([i in registers for i in instruction[1:]]):
            return f"InvalidRegisterError: Invalid register in line number {constants.line_count}. Is there any typo in the regsiter name?"
    elif instruction_type == "B" or instruction_type == "D":
        if instruction[1] not in registers:
            return f"InvalidRegisterError: Invalid register in line number {constants.line_count}. Is there any typo in the regsiter name?"
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