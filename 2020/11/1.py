#!/usr/bin/env python3

"""
    AoC2020, 11th day, 1st star.
    
    https://adventofcode.com/2020/day/11
"""

import copy

def get_adjacents(board, x, y):
    adjacents = []
    for i in [x-1, x, x+1]:
        if i >= 0 and i < len(board):
            for j in [y-1, y, y+1]:
                if j >= 0 and j < len(board[0]):
                     if not ((i == x) and (j == y)):
                         adjacents.append((i,j))
    return adjacents

with open('input.txt') as f:

    grid = [list(x.strip()) for x in f.readlines()]
    r = len(grid)
    c = len(grid[0])
    
    movements = 1
    
    while movements > 0:
        
        movements = 0

        l = copy.deepcopy(grid)
        
        for i in range(r):
            for j in range(c):
                occ = 0x0
                for (x,y) in get_adjacents(grid,i,j):
                    if grid[x][y] == '#':
                        occ += 1
                if grid[i][j] == 'L' and occ == 0:
                    #print('L')
                    l[i][j] = '#'
                    movements += 1
                elif grid[i][j] == '#' and occ >= 4:
                    #print('#')
                    l[i][j] = 'L'
                    movements += 1

        grid =copy.deepcopy(l)
        

    seats = 0
    for x in l:
        seats += x.count('#')

    print(seats)


    
