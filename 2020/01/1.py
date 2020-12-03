
with open('input.txt') as f:
    expenses = [int(x) for x in f.readlines()]
    print([x*y for x in expenses for y in expenses if x+y == 2020][0])
