from sys import stdin

class MEMORY:
    pc_counter = 0
    halted = False
    def __init__(self):
        temp = stdin.readlines()
        temp = [i.strip() for i in temp]
        self.memory = temp
        self.line_number = len(temp)

    def getInstruction(self, pc_counter):
        return self.memory[pc_counter]


