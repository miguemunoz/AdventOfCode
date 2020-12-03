from functools import reduce

slopes = [(3,1), (1,1),(5,1),(7,1),(1,2)]

solution = []

with open('input.txt') as f:
    
    geomap =  [list(x.strip()) * 3300 for x in f.readlines()]
    
    for i,j in slopes:
        
        x, y = 0, 0 # start position
        
        trees = 0 # number of trees found for the slope
        
        while y < len(geomap):
            if geomap[y][x] == '.':
                geomap[y][x] = 'O'
            elif geomap[y][x] == '#':
                geomap[y][x] = 'X'
                trees += 1
            x += i
            y += j
        
        solution.append(trees)
    
    print(reduce((lambda x, y: x * y), solution))
