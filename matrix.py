import numpy as np
import math

# 1
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
sum_vector = a + b
diff = b - a
print(sum_vector)
print(diff)

# 2
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
sum_vector = a + b
diff = b - a
print(sum_vector)
print(diff)


# 3
A = np.array([1, 2, 3])
B = np.array([4, 5, 6])
dot_product = np.dot(A, B)
print(dot_product)


# 4
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 17, 18]])
dot_product = np.dot(A, B)
print(dot_product)

# 5
A = np.array([1, 1, 2])
sum = 0
for i in A:
    sum += i**2
print(math.sqrt(sum))

# 6
A = np.array([[1, 2], [3, 4]])
transpose_matrix = A.T
print(transpose_matrix)
