import numpy as np

# Example matrices
A = np.array([[1,2],
              [3,4]])
B = np.array([[5,6],
              [7,8]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)


# Matrix Addition and Subtraction

C = A+B
print("A + B =\n", C)

D = A-B
print("A - B =\n", D)


# Matrix Multiplication

E = A @ B
print("A * B =\n", E)

X = np.array([[1, 2, 3],
              [4, 5, 6]])
Y = np.array([[7, 8],
              [9, 10],
              [11, 12]])

print("X * Y =\n", np.dot(X, Y))


# Matrix Inverse

G = np.array([[4, 7],
              [2, 6]])

det = np.linalg.det(G)
print("Determinant:", det)

if det != 0:
    G_inv = np.linalg.inv(G)
    print("Inverse of G:\n", G_inv)
    print("Check G * G_inv ≈ I:\n", np.round(G @ G_inv, 2))
else:
    print("Matrix not invertible")





   