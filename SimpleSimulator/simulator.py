from instances import ee, mem, rf


halted = False


while not halted:
    Instruction = mem.getInstruction(mem.pc_counter)
    mem.pc_dump()
    halted, mem.pc_counter, flag_change = ee.execute(Instruction, mem, rf)
    if not flag_change:
        rf.registers['111'] = '0000000000000000'
    rf.dump()
mem.dump()
