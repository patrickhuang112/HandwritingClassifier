import os, sys
import numpy as np


data_dir = "data/"

train = {}

test = {}

for i in range(1, 90001):
    if np.random.randint(2) > 1:
        true = True
        f = os.listdir(data_dir + 'true')[i]
    else:
        true = False
        f = os.listdir(data_dir + 'false')[i]
        

    if f == '.DS_Store':
        continue
    else:
        train[f] = 1 if true else 0

test = train[-10000:]

train = train[:-10000]

print(len(train), len(test))
