
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
        
        if bag != "shiny gold bag":
            
            content= set()
            
            for r in bags[bag]:
                content.add(r[0])
            
            while content:
                c = content.pop()
                if c == "shiny gold bag":
                    total += 1
                    break
                else:
                    for b in bags[c]:
                        content.add(b[0])
    
    print(total)
