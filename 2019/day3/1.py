
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
        wire_coordinates = set()
        for step in wire:
            direction, steps = step[0], int(step[1:])
            for i in range(1, steps+1):
                x,y = ops[direction](x,y)
                wire_coordinates.add((x,y))
        wires.append(wire_coordinates)
    
    i = wires[0]
    for w in wires:
        res = i.intersection(w)
    
    distances = []
    for point in list(res):
        distances.append(abs(point[0])+abs(point[1]))
    
    print(min(distances))
