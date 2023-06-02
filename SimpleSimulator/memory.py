from sys import stdin
import convertors


class MEMORY:
    pc_counter = 0
    halted = False

    def __init__(self):
        temp = stdin.readlines()
        temp = [i.strip() for i in temp]
        for i in range(128 - len(temp)):
            temp.append("0000000000000000")
        self.memory = temp
        self.line_number = len(temp)

    def getInstruction(self, pc_counter):
        return self.memory[pc_counter]

    def getBinarypc_counter(self):
        return convertors.integerToSevenBitBinary(self.pc_counter)

    def pc_dump(self):
        print(convertors.integerToEightBitBinary(self.pc_counter), end=" ")
