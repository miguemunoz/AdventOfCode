#!/usr/bin/env python3

"""
    AoC2015, 5th day, 2nd star.
    
    https://adventofcode.com/2015/day/5
"""

with open('input.txt') as f:

    nice = 0
    
    for line in f:
        
        simmetry = twice = 0x0
        
        for i in range(len(line)-1):
            s = line[i]+line[i+1]
            if line.find(s) != -1:
                if line[i+2:].find(s) != -1:
                    twice += 1
                    break
        
        for i in range(len(line)-2):
            if line[i] == line[i+2]:
                simmetry += 1
                break
        
        if simmetry >= 1 and twice >= 1:
            nice += 1
    
    print(nice)
