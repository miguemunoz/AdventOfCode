
class IntCode:

    pc = 0x0

    relative_address = 0x0

    def decode(self, instruction):
        opcode = int(str(instruction)[-2:])
        mode = [0x0] * 3
        if (str(instruction)[-3:-2] != ''):
            mode[0] = int(str(instruction)[-3:-2])
        if (str(instruction)[-4:-3] != ''):
            mode[1] = int(str(instruction)[-4:-3])
        if (str(instruction)[-5:-4] != ''):
            mode[2] = int(str(instruction)[-5:-4])
        return opcode, mode

    def idx(self, code, pc, mode):
        if mode == 0x0:
            return code[pc]
        elif mode == 0x1:
            return pc
        elif mode == 0x2:
            return code[pc] + self.relative_address

    def execute(self, code):
        while code[self.pc] != 99:
            # instruction decoding
            opcode, mode = self.decode(code[self.pc])
            # instruction execution
            if (opcode == 0x1):    # ADD
                op1 = code[self.idx(code, self.pc+1, mode[0])]
                op2 = code[self.idx(code, self.pc+2, mode[1])]
                dst = self.idx(code, self.pc+3, mode[2])
                code[dst] = op1 + op2
                self.pc += 4
            elif (opcode == 0x2):  # MUL
                op1 = code[self.idx(code, self.pc+1, mode[0])]
                op2 = code[self.idx(code, self.pc+2, mode[1])]
                dst = self.idx(code, self.pc+3, mode[2])
                code[dst] = op1 * op2
                self.pc += 4
            elif (opcode == 0x3):  # INPUT
                dst = self.idx(code, self.pc+1, mode[0])
                code[dst] = int(input())
                self.pc += 2
            elif (opcode == 0x4):  # OUTPUT
                value = code[self.idx(code, self.pc+1, mode[0])]
                print(value)
                self.pc += 2
            elif (opcode == 0x5):  # JUMP-IF-TRUE
                op1 = code[self.idx(code, self.pc+1, mode[0])]
                op2 = code[self.idx(code, self.pc+2, mode[1])]
                if (op1 != 0x0):
                    self.pc = op2
                else:
                    self.pc += 3
            elif (opcode == 0x6):  # JUMP-IF-FALSE
                op1 = code[self.idx(code, self.pc+1, mode[0])]
                op2 = code[self.idx(code, self.pc+2, mode[1])]
                if (op1 == 0x0):
                    self.pc = op2
                else:
                    self.pc += 3
            elif (opcode == 0x7):  # LESS-THAN
                op1 = code[self.idx(code, self.pc+1, mode[0])]
                op2 = code[self.idx(code, self.pc+2, mode[1])]
                dst = self.idx(code, self.pc+3, mode[2])
                if (op1 < op2):
                    code[dst] = 1
                else:
                    code[dst] = 0
                self.pc += 4
            elif (opcode == 0x8):  # EQUAL
                op1 = code[self.idx(code, self.pc+1, mode[0])]
                op2 = code[self.idx(code, self.pc+2, mode[1])]
                dst = self.idx(code, self.pc+3, mode[2])
                if (op1 == op2):
                    code[dst] = 1
                else:
                    code[dst] = 0
                self.pc += 4
            elif (opcode == 0x9):  # RELATIVE
                dst = self.idx(code, self.pc+1, mode[0])
                self.relative_address += code[dst]
                self.pc += 2
        # HALT
        return

with open('input.txt') as f:

    for line in f:
        computer = IntCode()
        refcode = [int(instructions) for instructions in line.split(',')]
        #refcode.setdefault(key, [])
        #print(refcode)
        refcode += [0]*30000
        #print(refcode)
        code = computer.execute(refcode)

        #print(refcode)
