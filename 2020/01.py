#!/usr/bin/env python3

"""
    AoC2020, 1st day ( https://adventofcode.com/2020/day/1 )
"""

def aoc2020d1(filename, first_star):
    
    expenses = [int(expense) for expense in open(filename)]
    
    if first_star:
            return [x*y for x in expenses for y in expenses if x+y == 2020][0]
        else:
            return [x*y*z for x in expenses for y in expenses for z in expenses if x+y+z == 2020][0]

if __name__ == "__main__":
    print(f'aoc2020d1s1: {aoc2020d1("input.txt", True)}')
    print(f'aoc2020d1s2: {aoc2020d1("input.txt", False)}')
