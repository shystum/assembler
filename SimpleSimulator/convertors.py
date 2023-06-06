def integerToSevenBitBinary(n: int) -> str:
    return bin(n)[2:].zfill(7)


def sevenBitBinaryToInteger(n: str) -> int:
    return int(n, 2)


def integerToSixteenBitBinary(n: int) -> str:
    return bin(n)[2:].zfill(16)


def integerToEightBitBinary(n: int) -> str:
    return bin(n)[2:].zfill(8)


def floatToBinary(n: float) -> str:
    integerPart = int(n)
    decimalPart = n - integerPart
    integerPart = bin(integerPart)[2:]
    decimal_binary = ''
    while decimalPart > 0:
        decimalPart *= 2
        if int(decimalPart) == 1:
            decimal_binary += '1'
            decimalPart -= 1
        else:
            decimal_binary += '0'
    return integerPart + '.' + decimal_binary


def binaryToFloat(n: str) -> float:
    parts = n.split('.')
    integer_part = parts[0]
    fractional_part = parts[1] if len(parts) > 1 else '0'
    decimal = int(integer_part, 2)
    fraction = 0
    for i, bit in enumerate(fractional_part):
        fraction += int(bit) * (2 ** -(i + 1))
    result = decimal + fraction
    return result


def floatToEightBitBinaryFloat(n: float) -> str:
    n = floatToBinary(n)
    parts = n.split('.')
    mantissa = parts[0][1:] + parts[1]
    if len(mantissa) > 5:
        return -1
    mantissa = mantissa.ljust(5, '0')
    zeroOneFlag = bool(int(parts[0][0]))
    print(zeroOneFlag)
    # exp = -3 if not zeroOneFlag else len(parts[0]) - 1
    print(parts)
    E = bin(len(parts[0]) - 1 + 3)[2:] if zeroOneFlag else 0
    E = str(E)
    print(E)
    E = E.zfill(3)
    return E + mantissa


def eightBitBinaryFloatTofloat(n: str) -> float:
    exp = n[:3]
    mantissa = n[3:]
    exp_value = int(exp, 2) - 3
    mantissa = '0' + mantissa if exp == '0' else '1' + mantissa
    mantissa_value = binaryToFloat(mantissa)
    result = mantissa_value * (2 ** exp_value)
    return result
