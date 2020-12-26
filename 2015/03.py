#!/usr/bin/env python3

"""
    AoC2015, 3rd day ( https://adventofcode.com/2015/day/3 )
"""

def aoc2015d3(filename, first_star):
    
    coordinates = {(0,0)}
    
    for line in open(filename):
        instructions = [list(line[::2]), list(line[1::2])] if not first_star else list(line.strip())
        current = [0,0]
        for instruction in instructions:
            if not first_star:
                current = [0,0]
            for c in instruction:
                if c == '>':
                    current[0] += 1
                elif c == '<':
                    current[0] -= 1
                elif c == '^':
                    current[1] += 1
                elif c == 'v':
                    current[1] -= 1
                coordinates.add(tuple(current))
    
    return len(coordinates)

if __name__ == "__main__":
    print(f'aoc2015d3s1: {aoc2015d3("input.txt", True)}')
    print(f'aoc2015d3s2: {aoc2015d3("input.txt", False)}')
