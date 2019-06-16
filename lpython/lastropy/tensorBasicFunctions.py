# -*- coding: utf-8 -*-
"""
Created on Mon May  6 20:43:22 2019

@author: manoj
"""

import tensorly as tl
import numpy as np

tl.set_backend('numpy')

tensor = tl.tensor(np.random.random((10, 10, 10)))
min_value = tl.min(tensor)

unfolding = tl.unfold(tensor, mode=0)
U, S, V = tl.partial_svd(unfolding, n_eigenvecs=5)

X = tl.tensor(np.arange(24).reshape((3, 4, 2)))