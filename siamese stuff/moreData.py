import os
import numpy

data_dir = "data/"

other_dir = "newdata/false"

l = os.listdir(other_dir)

for i in os.listdir(data_dir):
    if i == ".DS_Store":
        continue
    n = 3
    print(i)
    os.system("cp {} {}".format(data_dir + i + '/' + os.listdir(data_dir + i)[-n], other_dir + '2/' + i + '.png'))
    print("haw")

print("yee")

