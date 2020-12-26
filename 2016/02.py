#!/usr/bin/env python3

"""
    AoC2016, 2nd day ( https://adventofcode.com/2016/day/2 )
"""

def aoc2016d2(filename, first_star):

    keypad = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

    fancy_keypad = (('X','X','1','X','X'),
                    ('X','2','3','4','X'),
                    ('5','6','7','8','9'),
                    ('X','A','B','C','X'),
                    ('X','X','D','X','X'))
    
    code = []
    
    if first_star:
        position = [1,1]
    else:
        keypad = fancy_keypad
        position = [2,0]
    
    for line in open(filename):
        commands = list(line.strip())
        for cmd in commands:
            previous = position.copy()
            if cmd == 'U':
                if position[0]-1 >= 0:
                    position[0] -= 1
                else:
                    position[0] = 0
            elif cmd == 'L':
                if position[1]-1 >= 0:
                    position[1] -= 1
                else:
                    position[1] = 0
            elif cmd == 'R':
                if position[1]+1 < len(keypad[0]):
                    position[1] += 1
                else:
                    position[1] = len(keypad[0])-1
            elif cmd == 'D':
                if position[0]+1 < len(keypad):
                    position[0] += 1
                else:
                    position[0] = len(keypad)-1
            if keypad[position[0]][position[1]] == 'X':
                position = previous.copy()
        code.append(str(keypad[position[0]][position[1]]))
    return ''.join(code)

if __name__ == "__main__":
    print(f'aoc2016d2s1: {aoc2016d2("input.txt", True)}')
    print(f'aoc2016d2s2: {aoc2016d2("input.txt", False)}')
