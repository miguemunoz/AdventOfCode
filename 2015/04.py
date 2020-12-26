#!/usr/bin/env python3

"""
    AoC2015, 4th day ( https://adventofcode.com/2015/day/4 )
"""

import hashlib 

def aoc2015d4(filename, first_star):
    with open('input.txt') as f:
        for line in f:
            cnt = 0
            while True:
                result = hashlib.md5(line.strip().encode() + str(cnt).encode()).hexdigest()
                zeroes = 5 if first_star else 6
                if result.startswith('0' * zeroes):
                     return cnt
                cnt += 1

if __name__ == "__main__":
    print(f'aoc2015d4s1: {aoc2015d4("input.txt", True)}')
    print(f'aoc2015d4s2: {aoc2015d4("input.txt", False)}')
