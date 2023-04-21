from constants import registers, opcode
total_bits =16
def typeA(instruction: list[str]) -> str:
    binary_instruction = ''
    binary_instruction += opcode[instruction[0]][0]
    binary_instruction += '0'*(total_bits - 5 - (len(instruction)-1)*3) 
    binary_instruction += registers[instruction[1]]
    binary_instruction += registers[instruction[2]]
    binary_instruction += registers[instruction[3]]
    return binary_instruction
def typeB(instruction: list[str]) -> str:
    binary_instruction = ''
    
    return binary_instruction

def typeC(instruction: list[str]) -> str:
    binary_instruction = ''
    
    return binary_instruction

def typeD(instruction: list[str]) -> str:
    binary_instruction = ''
    
    return binary_instruction

def typeE(instruction: list[str]) -> str:
    binary_instruction = ''
    
    return binary_instruction

def typeF(instruction: list[str]) -> str:
    binary_instruction = ''
    
    return binary_instruction