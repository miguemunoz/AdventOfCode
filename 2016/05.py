#!/usr/bin/env python3

"""
    AoC2016, 5th day ( https://adventofcode.com/2016/day/5 )
"""

import hashlib

def valid_checksum(seed=''):
    cnt = 0
    while True:
        checksum = hashlib.md5(seed.strip().encode() + str(cnt).encode()).hexdigest()
        if checksum.startswith('0' * 5):
            yield checksum
        cnt += 1

def aoc2016d5(filename, first_star):
    with open('input.txt') as f:
        for line in f:
            gen = valid_checksum(seed=line.strip())
            if first_star:
                password = []
                for i in range(8):
                    password.append(next(gen)[5])
            else:
                password = [''] * 8
                while password.count('') > 0:
                    candidate = next(gen)
                    if '0' <= candidate[5] <= '7':
                        pos, char = int(candidate[5]), candidate[6]
                        if password[pos] == '':
                            password[pos] = char 
        return ''.join(password)

if __name__ == "__main__":
    print(f'aoc2016d5s1: {aoc2016d5("input.txt", True)}')
    print(f'aoc2016d5s2: {aoc2016d5("input.txt", False)}')
