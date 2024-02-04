# NUMPY ARRAY INDEXING

import numpy as np

arr = np.array([10,20,30,40,50])
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])
print(arr[4])

# Output
''' 10
    20
    30
    40
    50 '''

#*******************************


# Access 2-D Arrays

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print("3rd element on 2nd row : ", arr[1, 2])

# Output
# 3rd element on 2nd row :  8

#*******************************


# Access 3-D Arrays

arr = np.array([[[1,2,3], [4,5,6], [7,8,9], [10,11,12]]])
print(arr[0, 1, 2])

# Output
# 6

#*******************************


# Negative Indexing

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print("Last element from 2nd dimention: ", arr[1, -1])

# Output
# Last element from 2nd dimention:  10





