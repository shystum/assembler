from memory import *

mem = MEMORY()
halted = False

while not halted:
    Instruction = mem.getInstruction(mem.pc_counter)
    
