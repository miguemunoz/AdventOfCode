
coordinates = {(0,0)}

with open('input.txt') as f:
    for line in f:
        instructions = [list(line[::2]), list(line[1::2])]
        for instruction in instructions:
            current = [0,0]
            for c in instruction:
                if c == '>':
                    current[0] += 1
                elif c == '<':
                    current[0] -= 1
                elif c == '^':
                    current[1] += 1
                elif c == 'v':
                    current[1] -= 1
                coordinates.add(tuple(current))
        print(len(coordinates))
