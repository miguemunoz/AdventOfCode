
with open('input.txt') as f:
    for line in f:
        print(line.count('(')-line.count(')'))
