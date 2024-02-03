# NUMPY ARRAYS WITH RANDOM NUMBERS

import numpy as np

# 1. rand() :- Generates a random value between 0 to 1.

var = np.random.rand(5)
print(var)

# Output
# [0.68852995 0.74367463 0.32080926 0.03031924 0.07312289]

#**************************************************************


# 2. randn() :- Generates a random value close to zero. This may return positive or negative values as well.

var1 = np.random.randn(5)
print(var1)

# Output
# [-0.2248405  -0.30043539  1.38807759  0.39982221  0.25407407]

#****************************************************************


# 3. ranf() :- The function for doing random sampling in numpy. Returns an array of specified shape and
# fills it with random floats in the half open interval [0.0, 1.0).

var2 = np.random.ranf(5)
print(var2)

# Output
# [0.34285902 0.75099703 0.69454144 0.27717777 0.69562607]

#**************************************************************


# 4. randint() :- Generates a random number in a given min and max range.

var3 = np.random.randint(5, 20, 5)
print(var3)

# Output
# [10 12 18 12 10]


