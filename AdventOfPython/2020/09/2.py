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
    
    for i in numbers[25:]:
        
        value = [x for x in permutations if x[0] != x[1] and i == x[0] + x[1]]
        
        if not value:
            number = i
            break
        
        preamble = preamble[1:]
        preamble.append(i)
        
        permutations = list(itertools.permutations(preamble, 2))
    
    gen = list(range(2, len(numbers)))
    
    permutations = list(itertools.permutations(gen, 2))
    
    print([min(numbers[p[0]:p[1]]) + max(numbers[p[0]:p[1]]) for p in permutations if sum(numbers[p[0]:p[1]]) == number])
