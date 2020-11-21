
paper = 0

with open('input.txt') as f:
    for line in f:
        l,w,h = [int(x) for x in line.split('x')]
        a = [l*w, w*h, h*l]
        paper += sum(2*a)+min(a)
    print(paper)
