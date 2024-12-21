# -*- coding: utf-8 -*-

import numpy as np
import time
import matplotlib.pyplot as plt





def matrix_multiplication(A, B):
    N = A.shape[0]
    C = np.zeros((N, N), float)
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i, j] += A[i, k] * B[k, j]
    return C

def numpy_dot_multiplication(A, B):
    return np.dot(A, B)

sizes = list(range(10, 100, 10))  # Matrix sizes
explicit_times = []
dot_times = []



# Run tests for different matrix sizes
for N in sizes:
    A = np.random.random((N, N))
    B = np.random.random((N, N))
    
    # Time explicit multiplication
    start_exp = time.time()
    matrix_multiplication(A, B)
    explicit_times.append(time.time() - start_exp)
    
    # Time numpy.dot()
    start_numpy = time.time()
    numpy_dot_multiplication(A, B)
    dot_times.append(time.time() - start_numpy)


plt.figure(figsize=(10, 6))
plt.plot(sizes, explicit_times,'ro-', label='Explicit Multiplication' )
plt.plot(sizes, dot_times, label='numpy.dot()', marker='o')
plt.xlabel('Matrix Size (N)')
plt.ylabel('Computation Time (s)')
plt.title('A Graph of Explicit and Numpy.dot Matrix Multiplication vs Computation Time')
plt.legend()
plt.grid()
plt.show()