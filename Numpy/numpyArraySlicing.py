# NUMPY ARRAY SLICING

import numpy as np

# Slicing elements within the given range

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])

# Output
# [2 3 4 5]

#***************************************


# Slicing elements from index 4 to the end of the array

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[4:])

# Output
# [5 6 7]

#***************************************


# Slice elements from the beginning to index 5 (not included):

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[:5])

# Output
# [1 2 3 4 5]

#***************************************


# Negative Slicing

#Slice from the index 3 from the end to index 1 from the end:

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:-1])

# Output
# [5 6]

#****************************************


# STEP
# Use the step value to determine the step of the slicing

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2])

# Output
# [2 4]

#****************************************


#Slicing 2-D Arrays

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])

# Output
# [7 8 9]

#****************************************


arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 1:4])

# Output
# [[2 3 4]
#   [7 8 9]]
