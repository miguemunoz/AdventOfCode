#!/usr/bin/env python3

"""
    AoC2015, 1st day ( https://adventofcode.com/2015/day/1 )
"""

def aoc2015d1(filename, first_star):
    
    floor = 0
    
    with open(filename) as f:
        for line in f:
            if first_star:
                return line.count('(')-line.count(')')
            else:
                for idx, c in enumerate(line, 1):
                    if c == '(':
                        floor += 1
                    elif c == ')':
                        floor -= 1
                    if floor == -1:
                        return idx

if __name__ == "__main__":
    print(f'aoc2015d1s1: {aoc2015d1("input.txt", True)}')
    print(f'aoc2015d1s2: {aoc2015d1("input.txt", False)}')
