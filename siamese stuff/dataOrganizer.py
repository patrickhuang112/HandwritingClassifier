import os
import numpy as np

data_dir = "data/"

for d in os.listdir(data_dir):

    if d == ".DS_Store":
        continue
    
    f = np.random.randint(2)
    f = os.listdir(data_dir + d)[-f]

    os.system("cp {} {}".format(data_dir + d + '/' + f, "newdata/false2"))


print("complete")
