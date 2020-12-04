from functools import reduce

fields = {'byr': False, 'iyr': False, 'eyr': False, 'hgt': False, 'hcl': False, 'ecl': False, 'pid': False, 'cid': True}

total = 0

with open('input.txt') as f:
    
    passports =  [x for x in f.readlines()]
    
    validation = fields.copy()
    
    for line in passports:
        if line != '\n':
            entries = line.split()
            for e in entries:
                field, value = e.split(':')
                validation[field] = True
        else:
            if reduce((lambda x, y: x == y == True), validation.values()):
                total += 1
            
            validation = fields.copy()
    
    print(total)
