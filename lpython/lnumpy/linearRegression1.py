# Step 1: Import packages
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Step 2a: Provide data
x = [[0, 1], [5, 1], [15, 2], [25, 5], [35, 11], [45, 15], [55, 34], [60, 35]]
y = [4, 5, 20, 14, 32, 22, 38, 43]
print(type(x))

#change x , y to  an ndarray
x, y = np.array(x), np.array(y)
print(type(x))

model = LinearRegression().fit(x, y)
print()
print('intercept:', model.intercept_)
print('slope:', model.coef_)