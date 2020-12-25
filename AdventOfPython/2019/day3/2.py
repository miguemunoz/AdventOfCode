
def numsteps(wire, intersection):
    return wire.index(intersection)+1

ops = {
    "R": (lambda x,y : (x + 1, y)),
    "L": (lambda x,y : (x - 1, y)),
    "U": (lambda x,y : (x, y + 1)),
    "D": (lambda x,y : (x, y - 1)),
}

with open('input.txt') as f:
    wires = []
    for line in f:
        wire = [step for step in line.split(',')]
        x,y = (0,0)
        wire_coordinates = []
        for step in wire:
            direction, steps = step[0], int(step[1:])
            for i in range(1, steps+1):
                x,y = ops[direction](x,y)
                wire_coordinates.append((x,y))
        wires.append(wire_coordinates)
    
    i = set(wires[0])
    for w in wires:
        i = i.intersection(set(w))
    
    s = dict()
    for intersection in i:
        s[intersection] = 0x0
        for wire in wires:
            s[intersection] += numsteps(wire, intersection)
    
    print(min(s.values()))

