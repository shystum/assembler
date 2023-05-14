var xyz
add R0 R1 R2
sub    R0 R1 R2
mov    R0 $100
mov    R1 R2
mov FLAGS R5
ld R5 xyz
st R5 xyz
mul R6 R1 R1
div    R1 R3
ls R1 $1
xor    R0 R1 R2
or R0 R1 R1
and R0 R1 R2
cmp    R1 R6
jmp mylabel
jlt    mylabel
jgt mylabel
je mylabel
hlt