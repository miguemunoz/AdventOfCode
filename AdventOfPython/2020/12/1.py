#!/usr/bin/env python3

"""
    AoC2020, 12th day, 1st star.
    
    https://adventofcode.com/2015/day/12
"""

from numpy import array

position = array([0, 0])

directions = array([[1,0], [0,-1], [-1,0], [0,1]])

direction = 0

with open('input.txt') as f:
    for line in f:
        action, value = line[:1],int(line[1:])
        if action == 'N':
            position[1] += value
        elif action == 'S':
            position[1] -= value
        elif action == 'E':
            position[0] += value
        elif action == 'W':
            position[0] -= value
        elif action == 'L':
            direction = (direction - (value // 90)) % len(directions)
        elif action == 'R':
            direction = (direction + (value // 90)) % len(directions)
        elif action == 'F':
            position += directions[direction] * value

    print(abs(position[0])+abs(position[1]))
