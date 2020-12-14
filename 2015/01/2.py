#!/usr/bin/env python3

"""
    AoC2015, 1st day, 2nd star.
    
    https://adventofcode.com/2015/day/1
"""

floor = 0

with open('input.txt') as f:
    for line in f:
        for idx, c in enumerate(line, 1):
            if c == '(':
                floor += 1
            elif c == ')':
                floor -= 1
            if floor == -1:
                print(idx)
                exit(0)
