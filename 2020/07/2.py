
bags = {}

total = 0

with open('input.txt') as f:
    
    lines =  [x for x in f.readlines()]
    
    for line in lines:
        
        name, content = line.split(' contain ')
        
        l = []
        
        if content.find('no other') == -1: # more bags
            
            content = content.split(',')
            
            for c in content:
                n = c.strip()[:1] # number
                w = c.strip()[2:] # name
                l.append((w,n))
        
        bags[name] = l
    
    s =  list(bags.keys())
    
    for bag in s:
        
        if bag == "shiny gold bag":
            
            content= []
            
            for r in bags[bag]:
                for i in range(int(r[1])):
                    content.append(r)
            
            for c in content:
                for b in bags[c[0]]:
                    for i in range(int(b[1])):
                        content.append(b)
            
            print(len(content))
