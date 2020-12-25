#!/usr/bin/env python3

"""
    AoC2015, 6th day, 2nd star.
    
    https://adventofcode.com/2015/day/6
"""

import numpy as np

lights = np.zeros((1000,1000))

cmds = {
    "toggle "  : (lambda x : x+2),
    "turn off ": (lambda x : x-1 if x-1 >= 0 else 0),
    "turn on " : (lambda x : x+1),
}

with open('input.txt') as f:

    for line in f:
        for cmd in cmds:
            if line.find(cmd) != -1:
                coordinates = line[len(cmd):].strip().split(" through ")
                x1,y1 = coordinates[0].split(',')
                x2,y2 = coordinates[1].split(',')
                for i in range(int(x1),int(x2)+1):
                    for j in range(int(y1),int(y2)+1):
                        lights[i][j] = cmds[cmd](lights[i][j])
    
    print(int(np.sum(lights)))
