#!/usr/bin/env python3

"""
    AoC2020, 8th day, 1st star.
    
    https://adventofcode.com/2020/day/8
"""

def execute(code):
    
    pc = acc = 0x0
    
    hit = set()
    
    while True:
        
        if pc in hit: # same instruction executed twice
            return pc, acc
        
        hit.add(pc)
        
        opcode, param = code[pc][0], code[pc][1]
        
        if (opcode == 'nop'):
            pc += 1
        elif (opcode == 'jmp'):
            pc += int(param)
        elif opcode == 'acc':
            acc += int(param)
            pc += 1

with open('input.txt') as f:

    ram = []

    for line in f:
        ram.append(line.strip().split())

    pc, acc = execute(ram)
    
    print(acc)
    