#!/usr/bin/env python3

"""
    AoC2020, 10th day, 2nd star.
    
    https://adventofcode.com/2020/day/10
"""

import functools

@functools.lru_cache(maxsize=None)
def dp(n):
    if n == jolts[-1]:
        return 1
    else:
        if n not in jolts:
            return 0
        else:
            return dp(n+1) + dp(n+2) + dp(n+3)

with open('input.txt') as f:
    jolts = [int(x) for x in f.readlines()]
    jolts = [0] + jolts + [max(jolts)+3]
    jolts.sort()
    
    print(dp(jolts[0]))
