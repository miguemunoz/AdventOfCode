#!/usr/bin/env python3

"""
    AoC2020, 13th day, 1st star.
    
    https://adventofcode.com/2020/day/13
"""

def divisors(D, *d):
    for i in d:
        if D % i == 0:
            return i
    return 0

with open('input.txt') as f:
    
    t, buses =  f.readlines()
    
    timestamp = int(t)
    
    buses = [int(x.strip()) for x in buses.split(',') if x != 'x']
    
    while not divisors(timestamp, *buses):
        timestamp += 1
    
    busID = divisors(timestamp, *buses)
    
    print((timestamp-int(t))*busID)
