# NUMPY ARRAY

# Importing numpy as np

import numpy as np


# Arrays filled with 0's

zerosArray = np.zeros(4)
print(zerosArray)

# Output
# [0. 0. 0. 0.]

#***************************


# Arrays filled with 1's

onesArray = np.ones(5)
print(onesArray)

# Output
# [1. 1. 1. 1. 1.]

#****************************


# Empty Array

emptyArr = np.empty(6)
print(emptyArr)

# Output
# [0. 0. 0. 0. 0. 0.]

#*****************************


# Arrays with some range of elements

array = np.arange(7)
print(array)

# Output
# [0 1 2 3 4 5 6]

#******************************


# Array's diagonal elements filled with 1 (Identity Matrix)

diagOnes = np.eye(5)
print(diagOnes)

# Output
'''  [[1. 0. 0. 0. 0.]
     [0. 1. 0. 0. 0.]
     [0. 0. 1. 0. 0.]
     [0. 0. 0. 1. 0.]
     [0. 0. 0. 0. 1.]]
'''

#*****************************


# Arrays with values that are spaced linearly in a specified interval

array = np.linspace(0, 20, num = 5)
print(array)

# Output
# [ 0.  5. 10. 15. 20.]
