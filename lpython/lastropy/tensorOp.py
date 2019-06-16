# -*- coding: utf-8 -*-
"""
Created on Mon May  6 20:43:22 2019

@author: manoj
"""

import tensorly as tl
import numpy as np
tensor = np.random.random((10, 10, 10))
unfolded = tl.unfold(tensor, mode=0)
tl.fold(unfolded, mode=0, shape=tensor.shape)

from tensorly.decomposition import tucker, parafac, non_negative_tucker
factors = parafac(tensor, rank=5)
core, factors = tucker(tensor, ranks=[5, 5, 5])
core, factors = non_negative_tucker(tensor, rank=[5, 5, 5])