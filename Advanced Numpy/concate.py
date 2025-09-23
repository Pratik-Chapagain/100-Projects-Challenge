#concate function helps two or more than two arrays to join/concatenate together 

import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

new_arr = np.concatenate((arr1, arr2))

print(new_arr)

