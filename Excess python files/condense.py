import os
import numpy as np


d = 'data/false/'
l = os.listdir(d)
x = len(l) - 1

while x > 5000:
    os.remove((d + l[x]))
    l.pop(x)
    print(len(l))
    x -= 1

