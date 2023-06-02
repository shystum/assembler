from convertors import *


def add(Instruction, mem, rf):
    reg1 = Instruction[7:10]
    reg2 = Instruction[10:13]
    reg3 = Instruction[13:16]
    if (rf.registers[reg2] + rf.registers[reg3]) > 65535:
        rf.registers[reg1] = 0
        rf.registers["111"] = rf.registers["111"][:12] + "1" + rf.registers["111"][13:]
        return mem, rf

    rf.registers[reg1] = rf.registers[reg2] + rf.registers[reg3]
    return mem, rf


def subtract(instruction, mem, rf):
    reg1 = instruction[7:10]
    reg2 = instruction[10:13]
    reg3 = instruction[13:16]
    if rf.registers[reg3] > rf.registers[reg2]:
        rf.registers[reg1] = 0
        rf.registers["111"] = rf.registers["111"][:12] + "1" + rf.registers["111"][13:]
        return mem, rf

    rf.registers[reg1] = rf.registers[reg2] - rf.registers[reg3]
    return mem, rf


def move_immediate(instruction, mem, rf):
    reg1 = instruction[6:9]
    imm = instruction[9:16]
    imm = int(imm, 2)
    rf.registers[reg1] = imm
    return mem, rf


def move_register(instruction, mem, rf):
    reg1 = instruction[10:13]
    reg2 = instruction[13:16]
    if reg2 == "111":
        rf.registers[reg1] = int(rf.registers[reg2], 2)
        return mem, rf
    rf.registers[reg1] = rf.registers[reg2]
    return mem, rf


def load(instruction, mem, rf):
    reg = instruction[6:9]
    address = instruction[9:16]
    address = int(address, 2)
    rf.registers[reg] = address
    return mem, rf


def store(instruction, mem, rf):
    reg = instruction[6:9]
    address = instruction[9:16]
    address = int(address, 2)
    mem.memory[address] = integerToSixteenBitBinary(rf.registers[reg])
    return mem, rf


def multiply(instruction, mem, rf):
    reg1 = instruction[7:10]
    reg2 = instruction[10:13]
    reg3 = instruction[13:16]
    if (rf.registers[reg2] * rf.registers[reg3]) > 65535:
        rf.registers[reg1] = 0
        rf.registers["111"] = rf.registers["111"][:12] + "1" + rf.registers["111"][13:]
        return mem, rf
    rf.registers[reg1] = rf.registers[reg2] * rf.registers[reg3]
    return mem, rf


def divide(instruction, mem, rf):
    reg1 = instruction[10:13]
    reg2 = instruction[13:16]
    if rf.registers[reg2] == 0:
        rf.registers["000"] = 0
        rf.registers["001"] = 0
        rf.registers["111"] = rf.registers["111"][:12] + "1" + rf.registers["111"][13:]
        return mem, rf
    rf.registers["000"] = rf.registers[reg1] // rf.registers[reg2]
    rf.registers["001"] = rf.registers[reg1] % rf.registers[reg2]
    return mem, rf


def right_shift(instruction, mem, rf):
    reg1 = instruction[6:9]
    imm = instruction[9:16]
    imm = int(imm, 2)
    rf.registers[reg1] = (rf.registers[reg1] >> imm) % 65536
    return mem, rf


def left_shift(instruction, mem, rf):
    reg1 = instruction[6:9]
    imm = instruction[9:16]
    imm = int(imm, 2)
    rf.registers[reg1] = (rf.registers[reg1] << imm) % 65536
    return mem, rf


def xor(instruction, mem, rf):
    reg1 = instruction[7:10]
    reg2 = instruction[10:13]
    reg3 = instruction[13:16]
    rf.registers[reg1] = rf.registers[reg2] ^ rf.registers[reg3]
    return mem, rf


def Or(instruction, mem, rf):
    reg1 = instruction[7:10]
    reg2 = instruction[10:13]
    reg3 = instruction[13:16]
    rf.registers[reg1] = rf.registers[reg2] | rf.registers[reg3]
    return mem, rf


def And(instruction, mem, rf):
    reg1 = instruction[7:10]
    reg2 = instruction[10:13]
    reg3 = instruction[13:16]
    rf.registers[reg1] = rf.registers[reg2] & rf.registers[reg3]
    return mem, rf


def Invert(instruction, mem, rf):
    reg1 = instruction[10:13]
    reg2 = instruction[13:16]
    rf.registers[reg1] = ~rf.registers[reg2]
    return mem, rf


def compare(instruction, mem, rf):
    reg1 = instruction[10:13]
    reg2 = instruction[13:16]
    if rf.registers[reg1] == rf.registers[reg2]:
        rf.registers["111"] = rf.registers["111"][:15] + "1"
    elif rf.registers[reg1] > rf.registers[reg2]:
        rf.registers["111"] = rf.registers["111"][:14] + "1" + rf.registers["111"][15:]
    else:
        rf.registers["111"] = rf.registers["111"][:13] + "1" + rf.registers["111"][14:]
    return mem, rf


def jump_unconditional(instruction, mem, rf):
    address = instruction[9:16]
    address = int(address, 2)
    mem.pc_counter = address - 1
    return mem, rf


def jump_if_less_than(instruction, mem, rf):
    address = instruction[9:16]
    address = int(address, 2)
    if rf.registers["111"][13] == "1":
        mem.pc_counter = address - 1
    return mem, rf


def jump_if_greater_than(instruction, mem, rf):
    address = instruction[9:16]
    address = int(address, 2)
    if rf.registers["111"][14] == "1":
        mem.pc_counter = address - 1
    return mem, rf


def jump_if_equal(instruction, mem, rf):
    address = instruction[9:16]
    address = int(address, 2)
    if rf.registers["111"][15] == "1":
        mem.pc_counter = address - 1
    return mem, rf


def halt(instruction, mem, rf):
    mem.halted = True
    return mem, rf
