'''
Created on Feb 11, 2014

@author: jbarker
'''

import numpy as np
from matplotlib import *
import matplotlib.pyplot as plt


N = 800
r = 2 * np.random.rand(N)
theta = 2 * np.pi * np.random.rand(N)
area = 200 * r**2 * np.random.rand(N)
colors = theta

ax = plt.subplot(111, polar=True)
c = plt.scatter(theta, r, c=colors, s=area, cmap=plt.cm.hsv)
c.set_alpha(0.75)

plt.show()
