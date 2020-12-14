#!/usr/bin/env python3

"""
    AoC2015, 2nd day, 2nd star.
    
    https://adventofcode.com/2015/day/2
"""

ribbon = 0

with open('input.txt') as f:
    for line in f:
        l,w,h = [int(x) for x in line.split('x')]
        p = [l+l+w+w, w+w+h+h, h+h+l+l]
        ribbon += min(p)+l*w*h
    print(ribbon)
