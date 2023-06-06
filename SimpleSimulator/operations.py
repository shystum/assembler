from convertors import *
MAX_INT = 2**16 - 1


def add(instruction, mem, rf):
    reg1 = instruction[7:10]
    reg2 = instruction[10:13]
    reg3 = instruction[13:16]
    if (rf.registers[reg2] + rf.registers[reg3]) > MAX_INT:
        rf.registers[reg1] = 0
        rf.registers["111"] = rf.registers["111"][:12] + \
            "1" + rf.registers["111"][13:]
        return mem, rf, True

    rf.registers[reg1] = rf.registers[reg2] + rf.registers[reg3]

    return mem, rf, False


def subtract(instruction, mem, rf):
    reg1 = instruction[7:10]
    reg2 = instruction[10:13]
    reg3 = instruction[13:16]
    if rf.registers[reg3] > rf.registers[reg2]:
        rf.registers[reg1] = 0
        rf.registers["111"] = rf.registers["111"][:12] + \
            "1" + rf.registers["111"][13:]
        return mem, rf, True

    rf.registers[reg1] = rf.registers[reg2] - rf.registers[reg3]
    return mem, rf, False


def move_immediate(instruction, mem, rf):
    reg1 = instruction[6:9]
    imm = instruction[9:16]
    imm = int(imm, 2)
    rf.registers[reg1] = imm
    return mem, rf, False


def move_register(instruction, mem, rf):
    reg1 = instruction[10:13]
    reg2 = instruction[13:16]
    if reg2 == "111":
        rf.registers[reg1] = int(rf.registers[reg2], 2)
        return mem, rf, False
    rf.registers[reg1] = rf.registers[reg2]
    return mem, rf, False


def load(instruction, mem, rf):
    reg = instruction[6:9]
    address = instruction[9:16]
    num = mem.memory[int(address, 2)]
    num = int(num, 2)
    # print(address)
    rf.registers[reg] = num
    return mem, rf, False


def store(instruction, mem, rf):
    reg = instruction[6:9]
    address = instruction[9:16]
    address = int(address, 2)
    mem.memory[address] = integerToSixteenBitBinary(rf.registers[reg])
    return mem, rf, False


def multiply(instruction, mem, rf):
    reg1 = instruction[7:10]
    reg2 = instruction[10:13]
    reg3 = instruction[13:16]
    if (rf.registers[reg2] * rf.registers[reg3]) > MAX_INT:
        rf.registers[reg1] = 0
        rf.registers["111"] = rf.registers["111"][:12] + \
            "1" + rf.registers["111"][13:]
        return mem, rf, True
    rf.registers[reg1] = rf.registers[reg2] * rf.registers[reg3]
    return mem, rf, False


def divide(instruction, mem, rf):
    reg1 = instruction[10:13]
    reg2 = instruction[13:16]
    if rf.registers[reg2] == 0:
        rf.registers["000"] = 0
        rf.registers["001"] = 0
        rf.registers["111"] = rf.registers["111"][:12] + \
            "1" + rf.registers["111"][13:]
        return mem, rf, True
    rf.registers["000"] = rf.registers[reg1] // rf.registers[reg2]
    rf.registers["001"] = rf.registers[reg1] % rf.registers[reg2]
    return mem, rf, False


def right_shift(instruction, mem, rf):
    reg1 = instruction[6:9]
    imm = instruction[9:16]
    imm = int(imm, 2)
    rf.registers[reg1] = (rf.registers[reg1] >> imm) % 65536
    return mem, rf, False


def left_shift(instruction, mem, rf):
    reg1 = instruction[6:9]
    imm = instruction[9:16]
    imm = int(imm, 2)
    rf.registers[reg1] = (rf.registers[reg1] << imm) % 65536
    return mem, rf, False


def xor(instruction, mem, rf):
    reg1 = instruction[7:10]
    reg2 = instruction[10:13]
    reg3 = instruction[13:16]
    rf.registers[reg1] = rf.registers[reg2] ^ rf.registers[reg3]
    return mem, rf, False


def Or(instruction, mem, rf):
    reg1 = instruction[7:10]
    reg2 = instruction[10:13]
    reg3 = instruction[13:16]
    rf.registers[reg1] = rf.registers[reg2] | rf.registers[reg3]
    return mem, rf, False


def And(instruction, mem, rf):
    reg1 = instruction[7:10]
    reg2 = instruction[10:13]
    reg3 = instruction[13:16]
    rf.registers[reg1] = rf.registers[reg2] & rf.registers[reg3]
    return mem, rf, False


def Invert(instruction, mem, rf):
    reg1 = instruction[10:13]
    reg2 = instruction[13:16]
    num = integerToSixteenBitBinary(rf.registers[reg2])
    num = ''.join(['1' if x == '0' else '0' for x in num])
    num = int(num, 2)
    rf.registers[reg1] = num
    # print(~rf.registers[reg2])
    return mem, rf, False


def compare(instruction, mem, rf):
    reg1 = instruction[10:13]
    reg2 = instruction[13:16]
    if rf.registers[reg1] == rf.registers[reg2]:
        rf.registers["111"] = rf.registers["111"][:15] + "1"
    elif rf.registers[reg1] > rf.registers[reg2]:
        rf.registers["111"] = rf.registers["111"][:14] + \
            "1" + rf.registers["111"][15:]
    else:
        rf.registers["111"] = rf.registers["111"][:13] + \
            "1" + rf.registers["111"][14:]
    return mem, rf, True


def jump_unconditional(instruction, mem, rf):
    address = instruction[9:16]
    address = int(address, 2)
    mem.pc_counter = address - 1
    return mem, rf, False


def jump_if_less_than(instruction, mem, rf):
    address = instruction[9:16]
    address = int(address, 2)
    if rf.registers["111"][13] == "1":
        mem.pc_counter = address - 1
    return mem, rf, False


def jump_if_greater_than(instruction, mem, rf):
    address = instruction[9:16]
    address = int(address, 2)
    if rf.registers["111"][14] == "1":
        mem.pc_counter = address - 1
    return mem, rf, False


def jump_if_equal(instruction, mem, rf):
    address = instruction[9:16]
    address = int(address, 2)
    if rf.registers["111"][15] == "1":
        mem.pc_counter = address - 1
    return mem, rf, False


def halt(instruction, mem, rf):
    mem.halted = True
    return mem, rf, False


def F_addition(instruction, mem, rf):
    reg1 = instruction[7:10]
    reg2 = instruction[10:13]
    reg3 = instruction[13:16]
    reg2_val = (rf.registers[reg2])
    reg3_val = (rf.registers[reg3])
    ans = reg2_val + reg3_val
    if ans > 31.5 or ans < 0.26:
        rf.registers[reg1] = 0
        rf.registers["111"] = rf.registers["111"][:12] + \
            "1" + rf.registers["111"][13:]
    else:
        rf.registers[reg1] = (ans)
    return mem, rf, False


def F_subtraction(instruction, mem, rf):
    reg1 = instruction[7:10]
    reg2 = instruction[10:13]
    reg3 = instruction[13:16]
    reg2_val = (rf.registers[reg2])
    reg3_val = (rf.registers[reg3])
    ans = reg2_val - reg3_val
    if reg2_val < reg3_val:
        rf.registers[reg1] = 0
        rf.registers["111"] = rf.registers["111"][:12] + \
            "1" + rf.registers["111"][13:]
    elif ans > 31.5 or ans < 0.25:
        rf.registers[reg1] = 0
        rf.registers["111"] = rf.registers["111"][:12] + \
            "1" + rf.registers["111"][13:]
    else:
        rf.registers[reg1] = (ans)

    return mem, rf, False


def movF(instruction, mem, rf):
    reg = instruction[5:8]
    imm = instruction[8:16]
    imm = eightBitBinaryFloatTofloat(imm)
    # imm = floatToEightBitBinaryFloat(imm)
    rf.registers[reg] = imm
    return mem, rf, False


def addI(instruction, mem, rf):
    reg1 = instruction[6:9]
    imm = instruction[9:16]
    imm = int(imm, 2)
    ans = rf.registers[reg1] + imm
    if ans > MAX_INT:
        rf.registers[reg1] = 0
        rf.registers["111"] = rf.registers["111"][:12] + \
            "1" + rf.registers["111"][13:]
        return mem, rf, True
    else:
        rf.registers[reg1] = (rf.registers[reg1] + imm)
        return mem, rf, False


def subI(instruction, mem, rf):
    reg1 = instruction[6:9]
    imm = instruction[9:16]
    imm = int(imm, 2)
    ans = rf.registers[reg1] - imm
    if ans < 0:
        rf.registers[reg1] = 0
        rf.registers["111"] = rf.registers["111"][:12] + \
            "1" + rf.registers["111"][13:]
        return mem, rf, True
    else:
        rf.registers[reg1] = (rf.registers[reg1] - imm)
        return mem, rf, False


def mulI(instruction, mem, rf):
    reg1 = instruction[6:9]
    imm = instruction[9:16]
    imm = int(imm, 2)
    ans = rf.registers[reg1] * imm
    if ans > MAX_INT:
        rf.registers[reg1] = 0
        rf.registers["111"] = rf.registers["111"][:12] + \
            "1" + rf.registers["111"][13:]
        return mem, rf, True
    else:
        rf.registers[reg1] = (rf.registers[reg1] * imm)
        return mem, rf, False


def mod(instruction, mem, rf):
    reg1 = instruction[7:10]
    reg2 = instruction[10:13]
    reg3 = instruction[13:16]
    if (rf.registers[reg2] % rf.registers[reg3]) > MAX_INT:
        rf.registers[reg1] = 0
        rf.registers["111"] = rf.registers["111"][:12] + \
            "1" + rf.registers["111"][13:]
        return mem, rf, True
    else:
        rf.registers[reg1] = rf.registers[reg2] % rf.registers[reg3]
        return mem, rf, False


def xorI(instruction, mem, rf):
    reg1 = instruction[7:10]
    reg2 = instruction[10:13]
    imm = instruction[13:16]
    imm = int(imm, 2)
    if (rf.registers[reg1] > MAX_INT):
        rf.registers[reg1] = 0
        rf.registers["111"] = rf.registers["111"][:12] + \
            "1" + rf.registers["111"][13:]
        return mem, rf, True
    else:
        rf.registers[reg1] = rf.registers[reg2] ^ imm
        return mem, rf, False