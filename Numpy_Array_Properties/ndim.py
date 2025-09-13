#with the help of this attribute we can check the number of dimensions of an array whether it is 1d 2d or 3d

import numpy as np

arr_1D = np.array([1,2,3])
arr_2D = np.array([[1,2,3],[4,5,6]])
arr_3D = np.array([[[1,2],[3,4],[5,6],[7,8]]])

print(arr_1D.ndim)
print(arr_2D.ndim)
print(arr_3D.ndim)