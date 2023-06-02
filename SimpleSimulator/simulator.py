from instances import ee, mem, rf


halted = False


while not halted:
    Instruction = mem.getInstruction(mem.pc_counter)
    mem.pc_dump()
    halted, mem.pc_counter = ee.execute(Instruction, mem, rf)
    rf.dump()
