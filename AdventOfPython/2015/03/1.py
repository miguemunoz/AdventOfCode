#!/usr/bin/env python3

"""
    AoC2015, 3rd day, 1st star.
    
    https://adventofcode.com/2015/day/3
"""

coordinates = {(0,0)}

current = [0,0]

with open('input.txt') as f:
    for line in f:
        for idx, c in enumerate(line, 1):
            if c == '>':
                current[0] += 1
            elif c == '<':
                current[0] -= 1
            elif c == '^':
                current[1] += 1
            elif c == 'v':
                current[1] -= 1
            coordinates.add(tuple(current))
        print(len(coordinates))
