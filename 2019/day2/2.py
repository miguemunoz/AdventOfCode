
res = 0x0
noun = 0x0
verb = 0x0

def execute(code):
    pc = 0
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
    return code[0]

with open('input.txt') as f:
    for line in f:
        refcode = [int(instructions) for instructions in line.split(',')]
        for noun in range(100):
            for verb in range(100):
                # LOAD ""
                code = refcode[:]
                code[0x1] = noun
                code[0x2] = verb
                # Execution
                res = execute(code)
                # Condition
                if res == 19690720:
                    print(noun,verb)
                    break
