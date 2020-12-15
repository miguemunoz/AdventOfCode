#!/usr/bin/env python3

"""
    AoC2020, 15th day, 1st star.
    
    https://adventofcode.com/2015/day/15
"""

with open('input.txt') as f:
    for line in f:
        numbers = [int(x) for x in line.split(',')]
        for cnt in range(2020-len(numbers)):
            last = numbers[-1]
            if last in numbers[:-1]:
                idx = numbers[:-1][::-1].index(last)
                numbers.append(len(numbers)-(len(numbers)-idx-1))
            else:
                numbers.append(0)
        print(numbers[-1])
