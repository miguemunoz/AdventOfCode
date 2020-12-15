#!/usr/bin/env python3

"""
    AoC2020, 12th day, 2nd star.
    
    https://adventofcode.com/2015/day/12
"""

import numpy as np

position = np.array([0, 0])

directions = np.array([[1,1], [1,-1], [-1,-1], [-1,1]])

waypoint = np.array([10, 1])

direction = 0

with open('input.txt') as f:
    for line in f:
        action, value = line[:1],int(line[1:])
        if action == 'N':
            waypoint[1] += value
        elif action == 'S':
            waypoint[1] -= value
        elif action == 'E':
            waypoint[0] += value
        elif action == 'W':
            waypoint[0] -= value
        elif action == 'L':
            for cnt in range((value // 90) % len(directions)):
                waypoint[0], waypoint[1] = waypoint[1], waypoint[0]
                waypoint[0] *= -1
        elif action == 'R':
            for cnt in range((value // 90) % len(directions)):
                waypoint[0] *= -1
                waypoint[0], waypoint[1] = waypoint[1], waypoint[0]
        elif action == 'F':
            position += waypoint * value
    print(abs(position[0])+abs(position[1]))
