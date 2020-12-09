#!/usr/bin/env python3

"""
    AoC2020, 9th day, 1st star.
    
    https://adventofcode.com/2020/day/9
"""

import itertools

with open('input.txt') as f:

    numbers =  [int(x) for x in f.readlines()]
    
    preamble = numbers[:25]
    
    permutations = list(itertools.permutations(preamble, 2))
    
    candidates = numbers[25:]
    
    for i in candidates:
        
        found = False
        
        for p in permutations:
            if p[0] != p[1] and i == p[0] + p[1]:
                found = True
                break
        
        if not found:
            number = i
            break
        
        preamble = preamble[1:]
        preamble.append(i)
        
        permutations = list(itertools.permutations(preamble, 2))
    
    print(number)
