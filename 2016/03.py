#!/usr/bin/env python3

"""
    AoC2016, 3rd day ( https://adventofcode.com/2016/day/3 )
"""

def aoc2016d3(filename, first_star):

    triangles = []
    valids = []

    with open(filename) as f:
        for line in f.readlines():
            triangles.append([int(x) for x in line.split()])
        if first_star:
            for triangle in triangles:
                x,y,z = sorted(triangle)
                if x + y > z:
                    valids.append([x,y,z])
        else:
            for i in range(0, len(triangles),3):
                groups = list(zip(triangles[i],triangles[i+1],triangles[i+2]))
                for group in groups:
                    x,y,z = sorted(group)
                    if x + y > z:
                        valids.append([x,y,z])
    return len(valids)

if __name__ == "__main__":
    print(f'aoc2016d3s1: {aoc2016d3("input.txt", True)}')
    print(f'aoc2016d3s2: {aoc2016d3("input.txt", False)}')
