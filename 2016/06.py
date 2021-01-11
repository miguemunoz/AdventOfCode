#!/usr/bin/env python3

"""
    AoC2016, 6th day ( https://adventofcode.com/2016/day/6 )
"""

import numpy as np
from collections import Counter

def aoc2016d6(filename, first_star):
    with open('input.txt') as f:
        messages = []
        for line in f:
            messages.append([x for x in line.strip()])
        m = np.transpose(np.array(messages, dtype=str))
        corrected = []
        for row in m:
            cnt = Counter(row)
            if first_star:
                corrected.append(cnt.most_common(1)[0][0])
            else:
                corrected.append(cnt.most_common()[::-1][0][0])
        return ''.join(corrected)

if __name__ == "__main__":
    print(f'aoc2016d6s1: {aoc2016d6("input.txt", True)}')
    print(f'aoc2016d6s2: {aoc2016d6("input.txt", False)}')
