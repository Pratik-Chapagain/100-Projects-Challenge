import numpy as np

# 1. 1D array 0–9
arr1 = np.arange(10)
print(arr1)   # [0 1 2 3 4 5 6 7 8 9]

# 2. 3x3 ones
arr2 = np.ones((3,3))
print(arr2)
# [[1. 1. 1.]
#  [1. 1. 1.]
#  [1. 1. 1.]]

# 3. Even numbers 10–30
arr3 = np.arange(10, 31, 2)
print(arr3)   # [10 12 14 16 18 20 22 24 26 28 30]



# 4. Reshape 1–12 into (3,4)
arr4 = np.arange(1, 13).reshape(3,4)
print(arr4)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

# 5. Reshape same array into (2,6)
arr5 = np.arange(1, 13).reshape(2,6)
print(arr5)
# [[ 1  2  3  4  5  6]
#  [ 7  8  9 10 11 12]]


# 6. From [10,20,30,40,50,60]
arr6 = np.array([10, 20, 30, 40, 50, 60])
print(arr6[0])       # 10
print(arr6[-1])      # 60
print(arr6[1:4])     # [20 30 40]
print(arr6[::2])     # [10 30 50]

# 7. From 2D array
arr7 = np.array([[5,10,15],
                 [20,25,30],
                 [35,40,45]])

print(arr7[1,2])   # 30 (row1,col2)
print(arr7[2,:])   # [35 40 45] (row2)
print(arr7[:,0])   # [ 5 20 35] (col0)


# 8. Array operations
arr8 = np.array([1,2,3,4,5])
print(arr8 + 10)   # [11 12 13 14 15]
print(arr8 * 3)    # [ 3  6  9 12 15]
print(arr8 + arr8) # [ 2  4  6  8 10]
