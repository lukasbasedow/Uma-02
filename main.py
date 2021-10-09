import sys

import matplotlib.pyplot as plt
from numpy.random import randint

number = []
size = sys.getsizeof(number)
klassenbreite = 40
bin = 256 / klassenbreite
bin = int(bin)
bins = [0] * bin
fx = []

while size < 16*1048576:
    value = randint(0, 255)
    size = sys.getsizeof(number)
    number.append(value)

for x in range(0,bin):
    for y in number:
        if y < klassenbreite*x:
           bins[x] = bins[x]+1
        if x == 0 & y < klassenbreite:
            bins[x] = bins[x] + 1

for x in bins:
    fx.append(x / (len(number) * klassenbreite))

print(sys.getsizeof(number))
print(fx)
plt.hist(number, bins=bin)
plt.show()
