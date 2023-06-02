def integerToSevenBitBinary(n: int) -> str:
    return bin(n)[2:].zfill(7)


def sevenBitBinaryToInteger(n: str) -> int:
    return int(n, 2)


def integerToSixteenBitBinary(n: int) -> str:
    return bin(n)[2:].zfill(16)


def integerToEightBitBinary(n: int) -> str:
    return bin(n)[2:].zfill(8)
