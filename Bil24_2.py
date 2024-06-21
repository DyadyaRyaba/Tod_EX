import numpy as np

# Определение матриц A, B и C
A = np.array([[-1, 2, 4], [-3, 1, 2], [-3, 0, 1]])
B = np.array([[3, -1], [2, 1]])
C = np.array([[7, 2], [11, 8], [8, 4]])

# Вычисление обратных матриц A и B
A_inv = np.linalg.inv(A)
B_inv = np.linalg.inv(B)

# Вычисление матрицы X
X = np.dot(np.dot(A_inv, C), B_inv)

# Вывод результата
print(X)
