#!/usr/bin/env python3

"""
    AoC2020, 15th day, 2nd star.
    
    https://adventofcode.com/2015/day/15
"""

numbers = []

d = {}

with open('input.txt') as f:
    for line in f:
        for i, n in enumerate([int(x) for x in line.split(',')]):
            d[n] = i
            numbers.append(n)
        last = numbers[-1]
        for cnt in range(len(numbers),30000000):
            if last in d:
                value = cnt - 1 - d[last]
            else:
                value = 0
            d[last] = cnt - 1
            last = value
            
        print(last)
