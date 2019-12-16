
def valid(candidate):
    
    s = list(str(candidate))
    
    # It is a six-digit number...
    if len(s) != 6:
        return False
    
    # Two adjacent digits are the same...
    adjacent = False
    for idx in range(0,len(s)-1):
        #print(s[idx], s[idx])
        if s[idx] == s[idx+1]:
            adjacent = True
    if not adjacent:
        return False
    
    # Going from left to right, the digits never decrease
    for idx in range(0,len(s)-1):
        if s[idx] > s[idx+1]:
            return False
    
    return True

def password_gen(l):
    for candidate in l:
        if valid(candidate):
            yield candidate

r = list(range(240298,784956+1))

print(len(list(password_gen(r))))
