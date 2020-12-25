#!/usr/bin/env python3

"""
    AoC2020, 11th day, 2nd star.
    
    https://adventofcode.com/2020/day/11
"""

import copy

def visibles(board, x, y):
    visibles = []
    steps = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for step in steps:
        i,j = x,y
        while i+step[0] >= 0 and i+step[0] < len(board) and j+step[1] >= 0 and j+step[1] < len(board[0]):
            i += step[0]
            j += step[1]
            if board[i][j] == 'L' or board[i][j] == '#':
                visibles.append((i,j))
                break
    return visibles

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
                
                for (x,y) in visibles(grid,i,j):
                    if grid[x][y] == '#':
                        occ += 1
                
                if grid[i][j] == 'L' and occ == 0:
                    #print('L')
                    l[i][j] = '#'
                    movements += 1
                elif grid[i][j] == '#' and occ >= 5:
                    #print('#')
                    l[i][j] = 'L'
                    movements += 1
        
        grid =copy.deepcopy(l)
    
    seats = 0
    
    for x in l:
        seats += x.count('#')
    
    print(seats)
