global line_count
global var_count
global isInput 

isInput=True
line_count = 1
var_count = 0

current_variables = {}
current_labels = {}
MEM_SIZE = 256

FLAG = {'UnusedBit':'000000000000', 'V':'0', 'L':'0','G': '0', 'E':'0'}

opcode = {
    'add': ('00000', 'A'),
    'sub': ('00001', 'A'),
    'mov': [('00010', 'B'), ('00011', 'C')],
    'ld': ('00100', 'D'),
    'st': ('00101', 'D'),
    'mul': ('00110', 'A'),
    'div': ('00111', 'C'),
    'rs': ('01000', 'B'),
    'ls': ('01001', 'B'),
    'xor': ('01010', 'A'),
    'or': ('01011', 'A'),
    'and': ('01100', 'A'),
    'inv': ('01101', 'C'),
    'cmp': ('01110', 'C'),
    'jmp': ('01111', 'E'),
    'jlt': ('11100', 'E'),
    'jgt': ('11101', 'E'),
    'je': ('11111', 'E'),
    'hlt': ('11010', 'F'),
    'addf': ('10000', 'A'),
    'subf': ('10001', 'A'),
    'movf': ('10010', 'G'),
    # bonus
    'addi': ('10011', 'B'),
    'subi': ('10100', 'B'),
    'muli': ('10101', 'B'),
    'mod': ('10110', 'A'),
    'xori': ('10111', 'B'),
}

registers = {
    'R0': '000',
    'R1': '001',
    'R2': '010',
    'R3': '011',
    'R4': '100',
    'R5': '101',
    'R6': '110',
    'FLAGS': '111'
}

memory = [0] * int((MEM_SIZE/2))