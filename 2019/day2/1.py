
with open('input.txt') as f:
    for line in f:
        # LOAD ""
        code = [int(instructions) for instructions in line.split(',')]
        pc = 0
        # 1202 program alarm state
        code[1] = 12
        code[2] = 2
        # execution
        while code[pc] != 99:
            op1 = code[code[pc+1]]
            op2 = code[code[pc+2]]
            dst = code[pc+3]
            if (code[pc]== 1):    # ADD
                code[dst] = op1 + op2
            elif (code[pc] == 2): # MUL
                code[dst] = op1 * op2
            pc += 4
        # HALT
        print(dict(enumerate(code)))
