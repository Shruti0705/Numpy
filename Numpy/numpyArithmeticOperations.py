# ARITHMETIC OPERATIONS IN NUMPY ARRAYS

import numpy as np

# Addition

# Code A
var = np.array([1,2,3,4])
varAdd = var + 3
print(varAdd)

# Output
# [4 5 6 7]

# Code B
a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
c = np.add(a,b)
print(c)

# Output
# [ 6  8 10 12]

#******************************


# Subtraction

# Code A
var = np.array([1,2,3,4])
varSub = var - 3
print(varSub)

# Output
# [-2 -1  0  1]

# Code B
a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
c = np.subtract(a,b)
print(c)

# Output
# [-4 -4 -4 -4]

#******************************


# Multiply

# Code A
var = np.array([1,2,3,4])
varMul = var * 3
print(varMul)

# Output
# [ 3  6  9 12]

# Code B
a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
c = np.multiply(a,b)
print(c)

# Output
# [ 5 12 21 32]

#*******************************


# Divide

# Code A
var = np.array([1,2,3,4])
varDiv = var / 3
print(varDiv)

# Output
# [0.33333333 0.66666667 1.         1.33333333]

# Code B
a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
c = np.divide(a,b)
print(c)

# Output
# [0.2        0.33333333 0.42857143 0.5       ]

#*******************************


# Mod

# Code A
var = np.array([1,2,3,4])
varMod = var % 3
print(varMod)

# Output
# [1 2 0 1]

# Code B
a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
c = np.mod(a,b)
print(c)

# Output
# [1 2 3 4]

#*******************************


# Power

# Code A
var = np.array([1,2,3,4])
varPow = var ** 3
print(varPow)

# Output
# [ 1  8 27 64]
