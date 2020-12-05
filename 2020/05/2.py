
ids = []

with open('input.txt') as f:
    
    locations =  [x for x in f.readlines()]
    
    for seat in locations:
        row = seat[:7]
        col = seat[7:]
        
        i = list(range(128))
        j = list(range(8))
        
        for c in row:
            if c == 'F':
                i = i[0:len(i)//2]
            elif c == 'B':
                i = i[len(i)//2:len(i)]
        
        for c in col:
            if c == 'L':
                j = j[0:len(j)//2]
            elif c == 'R':
                j = j[len(j)//2:len(j)]
        
        ids.append(i[0]*8+j[0])
    
    ids = sorted(ids)
    
    for idx in range(len(ids)-1):
        if ids[idx] == ids[idx+1]-2:
            print(ids[idx]+1)
    
