from itertools import permutations

class Intcode:

    pc = 0x0

    output = 0x0

    def decode(self, instruction):
        opcode = int(str(instruction)[-2:])
        mode = [-1, -1, -1]
        if (str(instruction)[-3:-2] != ''):
            mode[0] = int(str(instruction)[-3:-2])
        if (str(instruction)[-4:-3] != ''):
            mode[1] = int(str(instruction)[-4:-3])
        if (str(instruction)[-5:-4] != ''):
            mode[2] = int(str(instruction)[-5:-4])
        return opcode, mode

    def operand(self, code, pc, mode):
        if mode == 0x0:
            return code[code[pc]]
        elif mode == 0x1:
            return code[pc]
        else:
            return code[code[pc]]

    def execute(self, code, inputs):
        while code[self.pc] != 99:
            # instruction decoding
            opcode, mode = self.decode(code[self.pc])
            # instruction execution
            if (opcode == 0x1):    # ADD
                op1 = self.operand(code, self.pc+1, mode[0])
                op2 = self.operand(code, self.pc+2, mode[1])
                dst = code[self.pc+3]
                code[dst] = op1 + op2
                self.pc += 4
            elif (opcode == 0x2):  # MUL
                op1 = self.operand(code, self.pc+1, mode[0])
                op2 = self.operand(code, self.pc+2, mode[1])
                dst = code[self.pc+3]
                code[dst] = op1 * op2
                self.pc += 4
            elif (opcode == 0x3):  # INPUT
                dst = code[self.pc+1]
                code[dst] = inputs.pop(0)
                self.pc += 2
            elif (opcode == 0x4):  # OUTPUT
                src = self.operand(code, self.pc+1, mode[0])
                self.pc += 2
                self.output = src
                return src
            elif (opcode == 0x5):  # JUMP-IF-TRUE
                op1 = self.operand(code, self.pc+1, mode[0])
                op2 = self.operand(code, self.pc+2, mode[1])
                if (op1 != 0x0):
                    self.pc = op2
                else:
                    self.pc += 3
            elif (opcode == 0x6):  # JUMP-IF-FALSE
                op1 = self.operand(code, self.pc+1, mode[0])
                op2 = self.operand(code, self.pc+2, mode[1])
                if (op1 == 0x0):
                    self.pc = op2
                else:
                    self.pc += 3
            elif (opcode == 0x7):  # LESS-THAN
                op1 = self.operand(code, self.pc+1, mode[0])
                op2 = self.operand(code, self.pc+2, mode[1])
                if (op1 < op2):
                    code[code[self.pc+3]] = 1
                else:
                    code[code[self.pc+3]] = 0
                self.pc += 4
            elif (opcode == 0x8):  # EQUAL
                op1 = self.operand(code, self.pc+1, mode[0])
                op2 = self.operand(code, self.pc+2, mode[1])
                if (op1 == op2):
                    code[code[self.pc+3]] = 1
                else:
                    code[code[self.pc+3]] = 0
                self.pc += 4
        # HALT
        return

amp_phases = [5, 6, 7, 8, 9]

with open('input.txt') as f:
    for line in f:
        refcode = [int(instructions) for instructions in line.split(',')]
        test_cases = list(permutations(amp_phases))
        values = []
        for test in test_cases:
            code = [c.copy() for c in [refcode] * len(amp_phases)]
            amplifiers = [Intcode() for i in amp_phases]
            boot = True
            output = 0x0
            while True:
                for i,amp in enumerate(test):
                    inputs = [amp, output] if boot else [output]
                    output = amplifiers[i].execute(code[i], inputs)
                boot = False
                if output:
                    values.append(output)
                else:
                    break
        print(max(values))

