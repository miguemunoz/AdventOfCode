#!/usr/bin/env python3

"""
    AoC2015, 2nd day ( https://adventofcode.com/2015/day/2 )
"""

def aoc2015d2(filename, first_star):

    res = 0

    for line in open(filename):
        l,w,h = [int(x) for x in line.split('x')]
        if first_star:
            res += 2*sum([l*w, w*h, h*l])+min([l*w, w*h, h*l])
        else:
            res += min([l+l+w+w, w+w+h+h, h+h+l+l])+l*w*h

    return res

if __name__ == "__main__":
    print(f'aoc2015d2s1: {aoc2015d2("input.txt", True)}')
    print(f'aoc2015d2s2: {aoc2015d2("input.txt", False)}')
