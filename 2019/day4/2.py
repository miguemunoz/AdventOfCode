
def valid(candidate):

    s = list(str(candidate))
    #print(s)
    # It is a six-digit number...
    if len(s) != 6:
        return False
    
    
    # Two adjacent digits are the same...
    adjacent = dict()
    for idx in range(0,len(s)-1):
        adjacent[s[idx]] = 0x0
    for idx in range(0,len(s)-1):
        if s[idx] == s[idx+1]:
            adjacent[s[idx]] += 1
    
    found = False
    for i in adjacent.values():
        if i == 1:
            found = True
    if not found:
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

#r = [112233,123444,111122]

print(len(list(password_gen(r))))
    
