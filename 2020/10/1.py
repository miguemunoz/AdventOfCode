#!/usr/bin/env python3

"""
    AoC2020, 10th day, 1st star.
    
    https://adventofcode.com/2020/day/10
"""

with open('input.txt') as f:

    jolts = [int(x) for x in f.readlines()]
    jolts = [0] + jolts + [max(jolts)+3]
    jolts.sort()
    
    for idx in range(len(jolts)-1):
       jolts[idx] = jolts[idx+1] - jolts[idx]

    print(jolts.count(3) * jolts.count(1))
