# Vector Operations and Angle Calculation using NumPy

import numpy as np

# ---------------------------------
# Part 1: Vector operations & norms
# ---------------------------------
a = np.array([1, 2])
b = np.array([3, -1])

print("=== Vector Operations ===")
print("a+b: ", a + b)
print("a-b: ", a - b)
print("2a: ", 2 * a)
print("3a-2b: ", 3 * a - 2 * b)

print("\n=== Norms ===")
print("L2 norm of a: ", np.linalg.norm(a, 2))
print("L1 norm of a: ", np.linalg.norm(a, 1))

print("\n=== Dot Product ===")
print("Dot Product a·b: ", np.dot(a, b))


# ---------------------------------
# Part 2: Angle between two vectors
# ---------------------------------
a = np.array([1, 2])
b = np.array([2, 3])

dot_product = np.dot(a, b)
norm_a = np.linalg.norm(a, 2)
norm_b = np.linalg.norm(b, 2)

cos_theta = dot_product / (norm_a * norm_b)
theta_radians = np.arccos(cos_theta)
theta_degrees = np.degrees(theta_radians)

print("\n=== Angle Between Vectors ===")
print("Dot product a·b:", dot_product)
print("L2 norm of a:", norm_a)
print("L2 norm of b:", norm_b)
print("Cos(theta):", cos_theta)
print("Angle in radians:", theta_radians)
print("Angle in degrees:", theta_degrees)
