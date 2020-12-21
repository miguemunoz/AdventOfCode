#!/usr/bin/env python3

"""
    AoC2020, 5th day ( https://adventofcode.com/2020/day/5 )
"""

def aoc2020d5(filename, first_star=True):
    
    ids = []
    
    locations =  [x for x in open(filename)]
    
    for seat in locations:
        row = seat[:7]
        col = seat[7:]
        
        i = list(range(128))
        j = list(range(8))
        
        for c in row:
            if c == 'F':
                i = i[0:len(i)//2]
            elif c == 'B':
                i = i[len(i)//2:len(i)]
        
        for c in col:
            if c == 'L':
                j = j[0:len(j)//2]
            elif c == 'R':
                j = j[len(j)//2:len(j)]
        
        ids.append(i[0]*8+j[0])
    
    ids = sorted(ids)
    
    if not first_star:
        for idx in range(len(ids)-1):
            if ids[idx] == ids[idx+1]-2:
                return ids[idx]+1
    
    return max(ids)

if __name__ == "__main__":
    print(f'aoc2020d5s1: {aoc2020d5("input.txt", True)}')
    print(f'aoc2020d5s2: {aoc2020d5("input.txt", False)}')
