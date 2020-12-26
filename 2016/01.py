#!/usr/bin/env python3

"""
    AoC2016, 1st day ( https://adventofcode.com/2016/day/1 )
"""

import operator

def aoc2016d1(filename, first_star):

    locations = set()
    directions = [[0,1],[1,0],[0,-1],[-1,0]]
    idx = 0

    for line in open(filename):
        instructions = [x.strip() for x in line.split(',')]
        position = [0,0]
        locations.add(tuple(position))
        for instruction in instructions:
            if instruction[0] == 'R':
                idx = abs((idx + 1) % len(directions))
            elif instruction[0] == 'L':
                idx = abs((idx - 1) % len(directions))
            if not first_star:
                previous = position.copy()
                for i in range(int(instruction[1:])):
                    previous = tuple(map(operator.add, previous, directions[idx]))
                    if previous in locations:
                        return sum(map(abs,previous))
                    else:
                        locations.add(tuple(previous))
                position = list(previous)
            else:
                position = list(map(operator.add, position, [x * int(instruction[1:]) for x in directions[idx]]))
    return sum(map(abs,position))

if __name__ == "__main__":
    print(f'aoc2016d1s1: {aoc2016d1("input.txt", True)}')
    print(f'aoc2016d1s2: {aoc2016d1("input.txt", False)}')
1