from memory import *
from RF import *
from EE import *

mem = MEMORY()
halted = False
RF = RF()
EE = EE()

while not halted:
    Instruction = mem.getInstruction(mem.pc_counter)
    halted,mem.pc_counter = EE.execute(Instruction)
    #pc.dump()
    #RF.dump()
    #pc.update(new_pc)