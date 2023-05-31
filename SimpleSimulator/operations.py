from RF import RF

def add( reg1, reg2, reg3):
    if (RF.registers[reg2]+RF.registers[reg3])>65535:
        RF.registers[reg1]=0
        RF.registers['111'] = RF.registers['111'][:12]+'1'+RF.registers['111'][13:]
        return
    RF.registers[reg1] = RF.registers[reg2] + RF.registers[reg3]

def subtract( reg1, reg2, reg3):
    if (RF.registers[reg3]>RF.registers[reg2]):
        RF.registers[reg1]=0
        RF.registers['111'] = RF.registers['111'][:12]+'1'+RF.registers['111'][13:]
        return
    RF.registers[reg1] = RF.registers[reg2] - RF.registers[reg3]

def move_immediate( reg1, imm):
    imm = int(imm,2)
    RF.registers[reg1] = imm

def move_register(reg1,reg2):
    RF.registers[reg1] = RF.registers[reg2]

# load data from memory address function to be implemented
# store data from memory address function to be implemented

def multiply( reg1, reg2, reg3):
    if (RF.registers[reg2]*RF.registers[reg3])>65535:
        RF.registers[reg1]=0
        RF.registers['111'] = RF.registers['111'][:12]+'1'+RF.registers['111'][13:]
        return
    RF.registers[reg1] = RF.registers[reg2] * RF.registers[reg3]

def divide( reg1, reg2):
    if (RF.registers[reg2]==0):
        RF.registers['000']=0
        RF.registers['001']=0
        RF.registers['111'] = RF.registers['111'][:12]+'1'+RF.registers['111'][13:]
        return
    RF.registers['000'] = RF.registers[reg1] // RF.registers[reg2]
    RF.registers['001'] = RF.registers[reg1] % RF.registers[reg2]

def right_shift(reg1,imm):
    imm = int(imm,2)
    RF.registers[reg1] = (RF.registers[reg1]>>imm)%65536

def left_shift(reg1,imm):
    imm = int(imm,2)
    RF.registers[reg1] = (RF.registers[reg1]<<imm)%65536

def xor(reg1,reg2,reg3):
    RF.registers[reg1] = RF.registers[reg2] ^ RF.registers[reg3]

def Or(reg1,reg2,reg3):
    RF.registers[reg1] = RF.registers[reg2] | RF.registers[reg3]

def And(reg1,reg2,reg3):
    RF.registers[reg1] = RF.registers[reg2] & RF.registers[reg3]

def Invert(reg1,reg2):
    RF.registers[reg1] = ~RF.registers[reg2]

def compare(reg1,reg2):
    if RF.registers[reg1] == RF.registers[reg2]:
        RF.registers['111'] = RF.registers['111'][:15]+'1'
    elif RF.registers[reg1] > RF.registers[reg2]:
        RF.registers['111'] = RF.registers['111'][:14]+'1'+RF.registers['111'][15:]
    else:
        RF.registers['111'] = RF.registers['111'][:13]+'1'+RF.registers['111'][14:]
    



