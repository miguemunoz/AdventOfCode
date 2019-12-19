
def path(orbits, planet):
    path = []
    for p in orbits.keys():
        if planet == p:
            while (orbits[planet] != 'COM'):
                path.append(orbits[planet])
                planet = orbits[planet]
            path.append('COM')
            return path

with open('input.txt') as f:
    
    orbits = dict()
    
    #Getting orbits...
    for line in f:
        orbit = line.strip().split(')')[::-1]
        orbits[orbit[0]] = orbit[1]
    
    # Symmetric difference
    print(len(set(path(orbits, 'YOU')) ^ set(path(orbits, 'SAN'))))
