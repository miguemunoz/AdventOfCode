#!/usr/bin/env python3

""" AoC2015, 1st day, 1st star """

with open('input.txt') as f:
    for line in f:
        print(line.count('(')-line.count(')'))
