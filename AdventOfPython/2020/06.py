#!/usr/bin/env python3

"""
    AoC2020, 6th day ( https://adventofcode.com/2020/day/6 )
"""

from functools import reduce

def aoc2020d6(filename, first_star=True):
    
    questions =  [x for x in open(filename)]
    
    yes = 0
    
    answered = []
    
    for line in questions:
        if line != '\n':
            answered.append(set(line.strip()))
        else:
            if first_star:
                answered = reduce((lambda x, y: x.union(y)), answered)
            else:
                answered = reduce((lambda x, y: x.intersection(y)), answered)
            yes += len(answered)
            answered = []
    
    if first_star:
        answered = reduce((lambda x, y: x.union(y)), answered)
    else:
        answered = reduce((lambda x, y: x.intersection(y)), answered)
    
    yes += len(answered)
    
    return yes

if __name__ == "__main__":
    print(f'aoc2020d6s1: {aoc2020d6("input.txt", True)}')
    print(f'aoc2020d6s2: {aoc2020d6("input.txt", False)}')
