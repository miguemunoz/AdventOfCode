#!/usr/bin/env python3

"""
    AoC2020, 9th day, 2nd star.
    
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
    
    gen = list(range(2, len(numbers)))
    
    permutations = list(itertools.permutations(gen, 2))
    
    for p in permutations:
        a = min(p[0],p[1])
        b = max(p[0],p[1])
        if sum(numbers[a:b]) == number:
            print(min(numbers[a:b]) + max(numbers[a:b]))
            break

