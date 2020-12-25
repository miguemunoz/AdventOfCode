#!/usr/bin/env python3

"""
    AoC2015, 4th day, 1st star.
    
    https://adventofcode.com/2015/day/4
"""
 
import hashlib 

with open('input.txt') as f:
    for line in f:
        cnt = 0
        while True:
            result = hashlib.md5(line.strip().encode() + str(cnt).encode()).hexdigest()
            if result.startswith('0' * 5):
                 print(cnt)
                 exit(0)
            cnt += 1
