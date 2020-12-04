from functools import reduce

total = 0

fields = {'byr': False, 'iyr': False, 'eyr': False, 'hgt': False, 'hcl': False, 'ecl': False, 'pid': False, 'cid': True}

def validateEntry(field, value):
    
    if field == 'byr':
        if int(value) >= 1920 and int(value) <= 2002 and len(value.strip()) == 4:
            return True
    elif field == 'iyr':
        if int(value) >= 2010 and int(value) <= 2020 and len(value.strip()) == 4:
            return True
    elif field == 'eyr':
        if int(value) >= 2010 and int(value) <= 2030 and len(value.strip()) == 4:
            return True
    elif field == 'hgt':
        unit = value[-2:]
        if unit == 'cm':
            h = int(value[:-2])
            if h >= 150 and h <= 193:
                return True
        elif unit == 'in':
            h = int(value[:-2])
            if h >= 59 and h <= 76:
                return True
    elif field == 'hcl':
        if value[0] == '#' and len(value[1:]) == 6:
            return True
    elif field == 'ecl':
        if value in ['amb','blu','brn','gry','grn', 'hzl','oth']:
            return True
    elif field == 'pid':
        if len(value.strip()) == 9:
            return True
    elif field == 'cid':
            return True
    
    return False

with open('input.txt') as f:
    
    passports =  [x for x in f.readlines()]
    
    validation = fields.copy()
    
    for line in passports:
        # Data...
        if line != '\n':
            entries = line.split()
            for e in entries:
                field, value = e.split(':')
                validation[field] = validateEntry(field, value)
        # Next passport...
        else:
            if reduce((lambda x, y: x == y == True), validation.values()):
                total += 1
            
            validation = fields.copy()
    
    print(total)
