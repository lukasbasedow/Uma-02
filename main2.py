import math

import matplotlib.pyplot as plt

x = [20,30,40,100,90,20]
bins = [0,50,80,100,125,150]
plt.hist(x, bins=bins,normed=True, alpha=0.5, histtype='stepfilled')
plt.show()