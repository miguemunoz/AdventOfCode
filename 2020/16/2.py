#!/usr/bin/env python3

"""
    AoC2020, 16th day, 2nd star.
    
    https://adventofcode.com/2015/day/16
"""

import re

rules = {}

yours = nearby = []

with open('input.txt') as f:

    lines = f.readlines()
    
    # Just parsering...
    for idx, line in enumerate(lines):
        if re.search(r'^[\w\s]+:\s\d+-\d+\sor\s\d+-\d+$', line.strip()):
            key, ranges = line.split(':')[0], line.split(':')[1]
            value = set()
            for r in ranges.split(' or '):
                value = value.union(set(list(range(int(r.strip().split('-')[0]),int(r.strip().split('-')[1])+1))))
            rules[key] = value
        elif re.search(r'^your ticket:$', line.strip()):
            yours = [int(x) for x in lines[idx+1].split(',')]
        elif re.search(r'^nearby tickets:$', line.strip()):
            for j in lines[idx+1:]:
                nearby.append([int(x) for x in j.split(',')])
    
    valid = set()
    
    for ranges in rules.values():
        valid = valid.union(ranges)
    
    for ticket in nearby.copy():
        for field in ticket:
            if field not in valid:
                nearby.remove(ticket)
    
    tickets = nearby + [yours]
    
    solution = {}
    
    for field in rules.keys():
        solution[field] = []
        for idx, column in enumerate(list(zip(*tickets))):
            if set(column).issubset(rules[field]):
                solution[field].append(idx)
    
    changes = True
    
    checked = set()

    while changes:
        changes = False
        for field in rules.keys():
            if len(solution[field]) == 1 and field not in checked:
                checked.add(field)
                for s in solution.values():
                    if len(s) > 1:
                        s.remove(solution[field][0])
                        changes = True
    
    r = 1
    for field in solution.keys():
            if re.search(r'^departure', field):
                print(solution[field][0])
                r *= yours[solution[field][0]]
    print(r)
