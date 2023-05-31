from RF import RF
from simulator import mem 
from convertors import *

def add(Instruction):
    reg1 = Instruction[7:10]
    reg2 = Instruction[10:13]
    reg3 = Instruction[13:16]
    if (RF.registers[reg2]+RF.registers[reg3])>65535:
        RF.registers[reg1]=0
        RF.registers['111'] = RF.registers['111'][:12]+'1'+RF.registers['111'][13:]
        return
    RF.registers[reg1] = RF.registers[reg2] + RF.registers[reg3]

def subtract(instruction):
    reg1 = instruction[7:10]
    reg2 = instruction[10:13]
    reg3 = instruction[13:16]
    if (RF.registers[reg3]>RF.registers[reg2]):
        RF.registers[reg1]=0
        RF.registers['111'] = RF.registers['111'][:12]+'1'+RF.registers['111'][13:]
        return
    RF.registers[reg1] = RF.registers[reg2] - RF.registers[reg3]

def move_immediate(instruction):
    reg1= instruction[6:9]
    imm = instruction[9:16]
    imm = int(imm,2)
    RF.registers[reg1] = imm

def move_register(instruction):
    reg1 = instruction[10:13]
    reg2 = instruction[13:16]
    RF.registers[reg1] = RF.registers[reg2]

def load(instruction):
    reg = instruction[6:9]
    address = instruction[9:16]
    address=int(address,2)
    RF.registers[reg]=mem.memory(address)

def store(instruction):
    reg = instruction[6:9]
    address = instruction[9:16]
    address=int(address,2)
    mem.memory[address]= integerToSixteenBitBinary(RF.registers[reg])

def multiply(instruction):
    reg1 = instruction[7:10]
    reg2 = instruction[10:13]
    reg3 = instruction[13:16]
    if (RF.registers[reg2]*RF.registers[reg3])>65535:
        RF.registers[reg1]=0
        RF.registers['111'] = RF.registers['111'][:12]+'1'+RF.registers['111'][13:]
        return
    RF.registers[reg1] = RF.registers[reg2] * RF.registers[reg3]

def divide(instruction):
    reg1=instruction[10:13]
    reg2=instruction[13:16]
    if (RF.registers[reg2]==0):
        RF.registers['000']=0
        RF.registers['001']=0
        RF.registers['111'] = RF.registers['111'][:12]+'1'+RF.registers['111'][13:]
        return
    RF.registers['000'] = RF.registers[reg1] // RF.registers[reg2]
    RF.registers['001'] = RF.registers[reg1] % RF.registers[reg2]

def right_shift(instruction):
    reg1=instruction[6:9]
    imm = instruction[9:16]
    imm = int(imm,2)
    RF.registers[reg1] = (RF.registers[reg1]>>imm)%65536

def left_shift(instruction):
    reg1=instruction[6:9]
    imm = instruction[9:16]
    imm = int(imm,2)
    RF.registers[reg1] = (RF.registers[reg1]<<imm)%65536

def xor(instruction):
    reg1 = instruction[7:10]
    reg2 = instruction[10:13]
    reg3 = instruction[13:16]
    RF.registers[reg1] = RF.registers[reg2] ^ RF.registers[reg3]

def Or(instruction):
    reg1=instruction[7:10]
    reg2=instruction[10:13]
    reg3=instruction[13:16]
    RF.registers[reg1] = RF.registers[reg2] | RF.registers[reg3]

def And(instruction):
    reg1=instruction[7:10]
    reg2=instruction[10:13]
    reg3=instruction[13:16]
    RF.registers[reg1] = RF.registers[reg2] & RF.registers[reg3]

def Invert(instruction):
    reg1=instruction[10:13]
    reg2=instruction[13:16]
    RF.registers[reg1] = ~RF.registers[reg2]

def compare(instruction):
    reg1=instruction[10:13]
    reg2=instruction[13:16]
    if RF.registers[reg1] == RF.registers[reg2]:
        RF.registers['111'] = RF.registers['111'][:15]+'1'
    elif RF.registers[reg1] > RF.registers[reg2]:
        RF.registers['111'] = RF.registers['111'][:14]+'1'+RF.registers['111'][15:]
    else:
        RF.registers['111'] = RF.registers['111'][:13]+'1'+RF.registers['111'][14:]
    
def jump_unconditional(instruction):
    address= instruction[9:16]
    address = int(address,2)
    mem.pc_counter = address

def jump_if_less_than(instruction):
    address= instruction[9:16]
    address = int(address,2)
    if RF.registers['111'][14] == '1':
        mem.pc_counter = address

def jump_if_greater_than(instruction):
    address= instruction[9:16]
    address = int(address,2)
    if RF.registers['111'][15] == '1':
        mem.pc_counter = address

def jump_if_equal(instruction):
    address= instruction[9:16]
    address = int(address,2)
    if RF.registers['111'][16] == '1':
        mem.pc_counter = address

def halt(instruction):
    mem.halted = True
