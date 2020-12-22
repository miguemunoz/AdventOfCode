#!/usr/bin/env python3

"""
    AoC2020, 7th day ( https://adventofcode.com/2020/day/7 )
"""

def aoc2020d7(filename, first_star=True):
    
    bags = dict()
    
    total = 0
    
    lines =  [x for x in open(filename)]
    
    for line in lines:
        
        name, content = line.split(' contain ')
        
        l = []
        
        if content.find('no other') == -1: # more bags
            
            content = content.split(',')
            
            for c in content:
                n = c.strip()[:1] # number
                w = c.strip()[2:] # name
                w = w.replace('.','')
                w = w.replace('bags','')
                w = w.replace('bag','')
                l.append((w.strip(),n.strip()))
        
        name.replace('.','')
        name = name.replace('bags','')
        name = name.replace('bag','')
        
        bags[name.strip()] = l
    
    s =  list(bags.keys())
    
    if first_star:
        
        for bag in s:
            
            if bag != "shiny gold":
                
                content= set()
                
                for r in bags[bag]:
                    content.add(r[0])
                
                while content:
                    c = content.pop()
                    if c == "shiny gold":
                        total += 1
                        break
                    else:
                        for b in bags[c]:
                            content.add(b[0])
        return total
        
    else:
        
        for bag in s:
            
            if bag == "shiny gold":
                
                content= []
                
                for r in bags[bag]:
                    for i in range(int(r[1])):
                        content.append(r)
                
                for c in content:
                    for b in bags[c[0]]:
                        for i in range(int(b[1])):
                            content.append(b)
                
                return len(content)

if __name__ == "__main__":
    print(f'aoc2020d7s1: {aoc2020d7("input.txt", True)}')
    print(f'aoc2020d6s2: {aoc2020d7("input.txt", False)}')
