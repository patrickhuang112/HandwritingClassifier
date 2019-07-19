import os
import numpy as np


d = 'data/true/'
l = os.listdir(d)
x = len(l) - 1

while x > 10000:
    os.remove((d + l[x]))
    l.pop(x)
    print(len(l))
    x -= 1

