from operations import *


class EE:
    def __init__(self):
        self.operations = {
            "00000": add,
            "00001": subtract,
            "00010": move_immediate,
            "00011": move_register,
            "00100": load,
            "00101": store,
            "00110": multiply,
            "00111": divide,
            "01000": right_shift,
            "01001": left_shift,
            "01010": xor,
            "01011": Or,
            "01100": And,
            "01101": Invert,
            "01110": compare,
            "01111": jump_unconditional,
            "11100": jump_if_less_than,
            "11101": jump_if_greater_than,
            "11111": jump_if_equal,
            "11010": halt,
            "10000": F_addition,
            "10001": F_subtraction,
            "10010": movF,
            "10011": addI,
            "10100": subI,
            "10101": mulI,
            "10110": mod,
            "10111": xorI
        }

    def execute(self, instruction, mem, rf):
        opcode = instruction[:5]
        mem, rf, flag_change = self.operations[opcode](instruction, mem, rf)
        return mem.halted, mem.pc_counter + 1, flag_change
