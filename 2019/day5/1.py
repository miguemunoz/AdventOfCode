
def decode(instruction):
        opcode = int(str(instruction)[-2:])
        mode = [-1, -1, -1]
        if (str(instruction)[-3:-2] != ''):
            mode[0] = int(str(instruction)[-3:-2])
        if (str(instruction)[-4:-3] != ''):
            mode[1] = int(str(instruction)[-4:-3])
        if (str(instruction)[-5:-4] != ''):
            mode[2] = int(str(instruction)[-5:-4])
        return opcode, mode

def operand(code, pc, mode):
    if mode == 0x0:
        return code[code[pc]]
    elif mode == 0x1:
        return code[pc]
    else:
        return code[code[pc]]

def execute(code):
    pc = 0
    while code[pc] != 99:
        # instruction decoding
        opcode, mode = decode(code[pc])
        # instruction execution
        if (opcode == 0x1):    # ADD
            op1 = operand(code, pc+1, mode[0])
            op2 = operand(code, pc+2, mode[1])
            dst = code[pc+3]
            code[dst] = op1 + op2
            pc += 4
        elif (opcode == 0x2):  # MUL
            op1 = operand(code, pc+1, mode[0])
            op2 = operand(code, pc+2, mode[1])
            dst = code[pc+3]
            code[dst] = op1 * op2
            pc += 4
        elif (opcode == 0x3):  # INPUT
            dst = code[pc+1]
            code[dst] = int(input())
            pc += 2
        elif (opcode == 0x4):  # OUTPUT
            src = operand(code, pc+1, mode[0])
            print(src)
            pc += 2
    # HALT
    return code

with open('input.txt') as f:
    for line in f:
        refcode = [int(instructions) for instructions in line.split(',')]
        code = execute(refcode)

