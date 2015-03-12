import numpy as np
import pylab as plt
import itertools

import seaborn as sns
n = 2
colors = sns.color_palette("hls", n)
roots = np.roots( [1,] + [0,]*(n-1) + [1,] )

# Sorted by angle
idx = np.argsort([np.angle(x) for x in roots])
roots = roots[idx]

plt.figure(figsize=(10,10))

for root,c in zip(roots,colors):
    plt.arrow(0,0,root.real,root.imag,ec=c,lw=3)

plt.xlim(-2.25,2.25)
plt.ylim(-2.25,2.25)
plt.show()
