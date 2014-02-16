'''
Created on Feb 11, 2014

@author: jbarker
'''
import numpy as np
import matplotlib.pyplot as plt


N = 1000
x = np.random.rand(N)
y = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2 # 0 to 15 point radiuses

plt.scatter(x, y, s=area, alpha=0.5)
plt.show()