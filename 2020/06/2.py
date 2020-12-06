from functools import reduce

yes = 0

answered = []

with open('input.txt') as f:
    
    questions =  [x for x in f.readlines()]
    
    for line in questions:
        if line != '\n':
            answered.append(set(line.strip()))
        else:
            answered = reduce((lambda x, y: x.intersection(y)), answered)
            yes += len(answered)
            answered = []
    
    print(yes)
