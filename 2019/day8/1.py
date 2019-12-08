
h = 6
w = 25

with open('input.txt') as f:
    for line in f:
        line = line.strip()
        layers = [line[i:(i+(h*w))] for i in range(0, len(line), h*w)]
        m = layers[0].count('0')
        r = layers[0].count('1') * layers[0].count('2')
        for layer in layers:
            if layer.count('0') < m:
                m = layer.count('0')
                r = layer.count('1') * layer.count('2')
        print(r)
