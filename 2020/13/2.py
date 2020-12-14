#!/usr/bin/env python3

"""
    AoC2020, 13th day, 2nd star.
    
    https://adventofcode.com/2020/day/13
"""

from sympy.ntheory.modular import crt

with open('input.txt') as f:

    _, buses = f.readlines()
    
    buses = [(int(x[1]),int(x[1])-x[0]) for x in enumerate(buses.split(',')) if x[1] != 'x']
    
    n, a = zip(*buses)
    
    print(crt(n,a)[0])
