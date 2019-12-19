
with open('input.txt') as f:
    
    orbits = dict()
    
    #Getting orbits...
    for line in f:
        orbit = line.strip().split(')')[::-1]
        orbits[orbit[0]] = orbit[1]
    
    paths = 0
    
    # Orbits per planet
    for planet in orbits.keys():
        while (orbits[planet] != 'COM'):
            planet = orbits[planet]
            paths += 1
        paths += 1
    
    # The number is...
    print(paths)
