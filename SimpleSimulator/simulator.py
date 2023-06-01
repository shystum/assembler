from instances import ee, mem, rf


halted = False


while not halted:
    Instruction = mem.getInstruction(mem.pc_counter)
    halted,mem.pc_counter = ee.execute(Instruction,mem, rf)
    #pc.dump()
    #pc.dump()
    # rf.dump()
    #pc.update(new_pc)