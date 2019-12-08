import numpy as np
import matplotlib.pyplot as plt

h = 6
w = 25

with open('input.txt') as f:
    for p, line in enumerate(f):
        line = line.strip()
        # extract layers
        layers = [line[i:(i+(h*w))] for i in range(0, len(line), h*w)][::-1]
        # reshape layers
        s = [np.array(list(l), dtype=int).reshape(h,w) for l in layers]
        # create zero matrix
        img = np.zeros((h,w), dtype=int)
        # process image
        for layer in s:
            for i in range(layer.shape[0]):
                for j in range(layer.shape[1]):
                    pixel = layer[i][j]
                    if pixel != 2:
                        img[i][j] = pixel
        # saving image
        plt.imshow(img)
        plt.savefig(f'output{p}.png')
