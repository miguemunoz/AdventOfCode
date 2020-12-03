
trees = 0

with open('input.txt') as f:
    
    geomap =  [list(x.strip()) * 3200 for x in f.readlines()]
    
    x, y = 0, 0 # start position
    
    while y < len(geomap):
        if geomap[y][x] == '.':
            geomap[y][x] = 'O'
        elif geomap[y][x] == '#':
            geomap[y][x] = 'X'
            trees += 1
        x += 3
        y += 1
    
    print(trees)
