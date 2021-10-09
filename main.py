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
str4 = str(klassenbreite)
plot = ["0-"+str4]

while size < 16*1048576:
    value = randint(0, 255)
    size = sys.getsizeof(number)
    number.append(value)

for x in range(0,bin):
    if x > 0:
        str1 = str(klassenbreite*(x+1)-klassenbreite)
        str2 = str(klassenbreite*(x+1))
        str3 = '%s-%s' % (str1, str2)
        plot.append(str3)

    for y in number:
        if y in range(klassenbreite*(x+1)-klassenbreite,klassenbreite*(x+1)):
           bins[x] = bins[x]+1

for x in bins:
    fx.append(x / (len(number) * klassenbreite))

print("Size of list: ",sys.getsizeof(number))
print("F(x) bei Klassenbreite: ", klassenbreite," und Variationsbereie: ", bin, fx)
plt.hist(number, bins=bin)
plt.show()
plt.bar(plot,fx)
plt.show()
