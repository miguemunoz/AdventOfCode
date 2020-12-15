#!/usr/bin/env python3

"""
    AoC2015, 5th day, 1st star.
    
    https://adventofcode.com/2015/day/5
"""

nice = 0

with open('input.txt') as f:

    for line in f:
        
        vocals = twice = 0
        forbidden = True
        
        for c in line:
            if c in 'aeiou':
                vocals += 1
        
        for i in range(len(line)-1):
            if line[i] == line[i+1]:
                twice += 1
        
        for g in ['ab','cd','pq','xy']:
            if g in line:
                forbidden = False
        
        if vocals >= 3 and twice >= 1 and forbidden:
            nice += 1
    
    print(nice)
