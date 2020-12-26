#!/usr/bin/env python3

"""
    AoC2020, 16th day, 2nd star.
    
    https://adventofcode.com/2015/day/16
"""

import re

def parser(filename):
    
    rules = {}
    yours = nearby = []
    
    with open(filename) as f:
        lines = f.readlines()
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
    return rules, yours, nearby

def remove_invalids(rules, nearby):
    
    valid = set()
    
    for ranges in rules.values():
        valid = valid.union(ranges)
    
    for ticket in nearby.copy():
        for field in ticket:
            if field not in valid:
                nearby.remove(ticket)
    
    return nearby

# Parse the input file...

rules, yours, nearby = parser('input.txt')

# Remove invalids...

nearby = remove_invalids(rules, nearby)

# Calculate all the candidates solution...

tickets = nearby + [yours]

solution = {}

for field in rules.keys():
    solution[field] = []
    for idx, column in enumerate(list(zip(*tickets))):
        if set(column).issubset(rules[field]):
            solution[field].append(idx)

# Discards candidates until gets the solution...

already_checked = set()

while len(already_checked) < len(rules.keys()):
    for field in rules.keys():
        if len(solution[field]) == 1 and field not in already_checked:
            already_checked.add(field)
            for s in solution.values():
                if len(s) > 1:
                    s.remove(solution[field][0])

result = 1
for field in solution.keys():
    if re.search(r'^departure', field):
        result *= yours[solution[field].pop()]
print(result)
