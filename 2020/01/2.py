
with open('input.txt') as f:
    expenses = [int(x) for x in f.readlines()]
    print([x*y*z for x in expenses for y in expenses for z in expenses if x+y+z == 2020][0])
