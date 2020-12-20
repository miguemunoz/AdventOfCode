#!/usr/bin/env python3

"""
    AoC2020, 2nd day ( https://adventofcode.com/2020/day/2 )
"""

def aoc2020d2s1(filename):
    
    cnt = 0x0
    
    for line in open(filename):
        
        policy, password = line.split(':')
        idx = policy.split()[0].split('-')
        letter = policy.split()[1]
        
        cnt += 1 if password.count(letter) in range(int(idx[0]),int(idx[1])+1) else 0
    
    return cnt

def aoc2020d2s2(filename):
    
    cnt = 0x0
    
    for line in open(filename):
        
        policy, password = line.split(':')
        idx = policy.split()[0].split('-')
        letter = policy.split()[1]
        
        cnt += 1 if (password[int(idx[0])] == letter) != (password[int(idx[1])] == letter) else 0
    
    return cnt

if __name__ == "__main__":
    print(f'aoc2020d2s1: {aoc2020d2s1("input.txt")}')
    print(f'aoc2020d2s2: {aoc2020d2s2("input.txt")}')
