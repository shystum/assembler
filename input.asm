var input1
var input2
var one
var zero
var two 
var three
var case
var output1
var output2
mov R1 $0
st R1 zero
mov R1 $1
st R1 one
st R1 input1
st R1 input2
mov R2 $2
st R1 two
mov R1 $3
st R1 three
mov R1 $4
st R1 case
ld R0 case
ld R1 zero
cmp R0 R1
je case0
ld R1 one
cmp R0 R1
je case1
ld R1 two
cmp R0 R1
je case2
ld R1 three
cmp R0 R1
je case3
jmp end
case0: ld R0 input1
ld R1 input2
ld R2 output1
ld R3 output2
xor R2 R1 R0
or R3 R1 R0
st R3 output2
st R2 output1
st R3 input2
st R2 input1
case1: ld R0 input1
ld R1 input2
ld R2 output1
ld R3 output2
xor R2 R1 R0
or R3 R1 R0
st R3 output2
st R2 output1
st R3 input2
st R2 input1
case2: ld R0 input1
ld R1 input2
ld R2 output1
ld R3 output2
or R2 R1 R0
xor R3 R1 R0
st R3 output2
st R2 output1
st R3 input2
st R2 input1
case3: ld R0 input1
ld R1 input2
ld R2 output1
ld R3 output2
or R2 R1 R0
xor R3 R1 R0
st R3 output2
st R2 output1
st R3 input2
st R2 input1
end: hlt
