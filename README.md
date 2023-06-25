# Assembler
Group Assignment for the course CSE112 - Computer Organization.

Implemented a custom assembler and simulator for a given ISA.

##
### Instructions:
Run ./run inside the automatedTested directory to run the automated assembler and simulator test cases.


##
### Bonus Part:
| Opcode | Instruction           | Semantics                   | Syntax              | Type |
|--------|-----------------------|-----------------------------|---------------------|------|
| 10011  | Immediate addition    | Performs reg1 = reg2 + $Imm | addi reg1 reg2 $Imm | B    |
| 10100  | Immediate Subtraction | Performs reg1 = reg2 - $Imm | subi reg1 reg2 $Imm | B    |
| 10101  | Immediate Multiply    | Performs reg1 = reg2 * $Imm | muli reg1 reg2 $Imm | B    |
| 10110  | Modulus               | Performs reg1 = reg2 % reg3 | mod reg1 reg2 reg3  | A    |
| 10111  | Immediate Xor         | Performs reg1 = reg2 ^ $Imm | xori reg1 reg2 $Imm | B    |


##
#### Group Member:
Aarav Mathur 2022005

Arnav Jindal 2022101

Dhruv Jain 2022166

Dikshant Agarwal 2022175
