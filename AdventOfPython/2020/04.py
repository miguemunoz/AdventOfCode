#!/usr/bin/env python3

"""
    AoC2020, 4th day ( https://adventofcode.com/2020/day/4 )
"""

from functools import reduce

passport_fields = {'byr': False,
                   'iyr': False,
                   'eyr': False,
                   'hgt': False,
                   'hcl': False,
                   'ecl': False,
                   'pid': False,
                   'cid': True}

validate_passport_entry = {
    "byr": (lambda x: int(x) >= 1920 and int(x) <= 2002 and len(x.strip()) == 4),
    "iyr": (lambda x: int(x) >= 2010 and int(x) <= 2020 and len(x.strip()) == 4),
    "eyr": (lambda x: int(x) >= 2010 and int(x) <= 2030 and len(x.strip()) == 4),
    "hgt": (lambda x: (x[-2:] == 'cm' and int(x[:-2]) >= 150 and int(x[:-2]) <= 193) or \
                      (x[-2:] == 'in' and int(x[:-2]) >=  59 and int(x[:-2]) <=  76)),
    "hcl": (lambda x: x[0] == '#' and len(x[1:]) == 6),
    "ecl": (lambda x: x in ['amb','blu','brn','gry','grn', 'hzl','oth']),
    "pid": (lambda x: len(x.strip()) == 9),
    "cid": (lambda x: True)
}

def aoc2020d4(filename, first_star=True):
    
    with open(filename) as f:
        
        total = 0
        
        passports =  [x for x in f]
        
        validation = passport_fields.copy()
        
        for line in passports:
            if line != '\n':
                entries = line.split()
                for e in entries:
                    field, value = e.split(':')
                    if first_star:
                        validation[field] = True
                    else:
                        validation[field] = validate_passport_entry[field](value)
            else:
                if reduce((lambda x, y: x == y == True), validation.values()):
                    total += 1
                
                validation = passport_fields.copy()
        
        if reduce((lambda x, y: x == y == True), validation.values()):
            total += 1
    
    return total

if __name__ == "__main__":
    print(f'aoc2020d4s1: {aoc2020d4("input.txt", True)}')
    print(f'aoc2020d4s2: {aoc2020d4("input.txt", False)}')
