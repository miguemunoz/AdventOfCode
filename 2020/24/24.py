#!/usr/bin/env python3

"""
    AoC2020, 24th day ( https://adventofcode.com/2020/day/24 )
"""

import re
import operator
import copy

directions = {'ne' : [+1,-1, 0],
              'se' : [ 0,+1,-1],
              'nw' : [ 0,-1,+1],
              'sw' : [-1,+1, 0],
              'e'  : [+1, 0,-1],
              'w'  : [-1, 0,+1],
}

def flip(candidates, blacks):
    for c in candidates:
        if c not in blacks:
            blacks.add(c)
        else:
            blacks.discard(c)
    return blacks

def neighbours(tile, blacks):
    w = []
    b = []
    for direction in [x for x in directions.values()]: 
        neighbour = tuple(map(operator.add, tile, direction)) # generate all neighbours candidates
        if neighbour in blacks:
            b += [neighbour]
        else:
            w += [neighbour]
    return w, b

def aoc2020d24(filename, first_star=True):
    
    def parse(line):
        return re.compile(r'ne|se|nw|sw|e|w').findall(line.strip())

    instructions = []

    for line in open(filename):
        instructions.append([directions[x] for x in parse(line)])

    blacks = set()
    
    for instruction in instructions:
        current_position = [0, 0, 0] 
        for direction in instruction:
            current_position = tuple(map(operator.add, current_position, direction))
        flip([current_position], blacks)

    if first_star:
        return len(blacks)
    else:
        for day in range(100): # 100 days
            
            whites = []
            candidates = []

            for tile in blacks:
                w, b = neighbours(tile, blacks)
                if len(b) == 0 or len(b) > 2:
                    candidates += [tile]
                whites += w
            
            for tile in whites:
                w, b = neighbours(tile, blacks)
                if len(b) == 2:
                    candidates += [tile]
            
            blacks = flip(list(set(candidates)), blacks)

        return len(blacks)

if __name__ == "__main__":
    print(f'aoc2020d24s1: {aoc2020d24("input.txt", True)}')
    print(f'aoc2020d24s2: {aoc2020d24("input.txt", False)}')
