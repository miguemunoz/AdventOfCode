#!/usr/bin/env python3

# Chine Remainder Theorem implementation
# https://fangya.medium.com/chinese-remainder-theorem-with-python-a483de81fbb8

from functools import reduce

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

"""
    AoC2020, 13th day, 2nd star.
    
    https://adventofcode.com/2020/day/13
"""

with open('input.txt') as f:

    _, buses = f.readlines()
    
    buses = [(int(x[1]),int(x[1])-x[0]) for x in enumerate(buses.split(',')) if x[1] != 'x']
    
    n, a = zip(*buses)
    
    print(int(chinese_remainder(n,a)))
