def integerToSevenBitBinary(n: int) -> str:
    return bin(n)[2:].zfill(7) 

def sevenBitBinaryToInteger(n: str) -> int:
    return int(n, 2)