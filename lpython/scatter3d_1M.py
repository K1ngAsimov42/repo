'''
==============
3D scatterplot
==============

Demonstration of a basic scatterplot in 3D.
'''

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


def randrange(n, vmin, vmax):
    '''
    Helper function to make an array of random numbers having shape (n, )
    with each number distributed Uniform(vmin, vmax).
    '''
    return (vmax - vmin)*np.random.rand(n) + vmin

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

n = 10000

# For each set of style and range settings, plot n random points in the box
# defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
# for c, m, zlow, zhigh in [('r', 'o', -10, 1000), ('b', '^', -10, 1000)]:
    # xs = randrange(n, 0, 5000)
    # ys = randrange(n, 0, 1000)
    # zs = randrange(n, zlow, zhigh)
    # ax.scatter(xs, ys, zs, c=c, marker=m)

for c, m, zlow, zhigh in [('r', 'o', -10, 1000)]:
    xs = randrange(n, 0, 5000)
    ys = randrange(n, 0, 5000)
    zs = randrange(n, zlow, zhigh)
    ax.scatter(xs, ys, zs, c=c, marker=5)

for c, m, zlow, zhigh in [('b', 'o', -10, 1000)]:
    xs = randrange(n, 0, 1000)
    ys = randrange(n, 0, 1000)
    zs = randrange(n, zlow, zhigh)
    ax.scatter(xs, ys, zs, c=c, marker=10)
	
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
