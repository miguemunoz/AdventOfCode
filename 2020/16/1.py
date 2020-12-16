#!/usr/bin/env python3

"""
    AoC2020, 16th day, 1st star.
    
    https://adventofcode.com/2015/day/16
"""

import re

rules = {}

your = nearby = []

with open('input.txt') as f:

    lines = f.readlines()
    
    # Just parsering...
    for idx, line in enumerate(lines):
        if re.search(r'^[\w\s]+:\s\d+-\d+\sor\s\d+-\d+$', line.strip()):
            key, ranges = line.split(':')[0], line.split(':')[1]
            value = []
            for r in ranges.split(' or '):
                value += [(int(r.strip().split('-')[0]), int(r.strip().split('-')[1]))]
            rules[key] = value
        elif re.search(r'^your ticket:$', line.strip()):
            your = [int(x) for x in lines[idx+1].split(',')]
        elif re.search(r'^nearby tickets:$', line.strip()):
            for j in lines[idx+1:]:
                nearby.append([int(x) for x in j.split(',')])
    
    valid = set()
    
    for ranges in rules.values():
        for r in ranges:
            for i in range(r[0],r[1]+1):
                valid.add(i)
    
    error_rate = 0
    
    for ticket in nearby:
        for field in ticket:
            if field not in valid:
                error_rate += field
    
    print(error_rate)
