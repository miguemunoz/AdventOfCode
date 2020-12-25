#!/usr/bin/env python3

"""
    AoC2020, 15th day, 1st star.
    
    https://adventofcode.com/2015/day/15
"""

numbers = {}

with open('input.txt') as f:
    for line in f:
        for i, n in enumerate([int(x) for x in line.split(',')]):
            numbers[n],last = i,n
        for cnt in range(len(numbers),2020):
            if last in numbers:
                value = cnt-1-numbers[last]
            else:
                value = 0
            numbers[last] = cnt-1
            last = value
        print(last)
