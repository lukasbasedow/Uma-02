import sys

import matplotlib.pyplot as plt
from numpy.random import randint

number = []
size = sys.getsizeof(number)
counter = 0

while size < 16*1048576:
    value = randint(0, 255)
    size = sys.getsizeof(number)
    counter = counter +1
    number.append(value)

print(counter)
print(sys.getsizeof(number))
plt.hist(number, bins=25)
plt.show()
