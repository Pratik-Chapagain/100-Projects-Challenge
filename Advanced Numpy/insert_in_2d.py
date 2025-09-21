import numpy as np

arr_2d = np.array([[10,20,30], [40,50,60]])
print(arr_2d)

#insert a new row at index 1
new_arr_2d = np.insert(arr_2d, 1, [5,6], axis=0)
print(new_arr_2d)
