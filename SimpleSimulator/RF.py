import convertors


class RF:
    def __init__(self):
        self.registers = {
            "000": 0,
            "001": 0,
            "010": 0,
            "011": 0,
            "100": 0,
            "101": 0,
            "110": 0,
            "111": "0000000000000000",
        }

    def dump(self):
        r = list(self.registers.values())
        for i in range(7):
            if (type(r[i])) == int:
                print(convertors.integerToSixteenBitBinary(r[i]), end=" ")
            else:
                val = convertors.floatToEightBitBinaryFloat(r[i])
                print(val.rjust(16,'0'), end=" ")
        print(r[-1])
