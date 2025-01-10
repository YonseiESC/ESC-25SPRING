import numpy as np
import time

# 데이터 크기 설정
N = 1000
p = 50
M = 500
X = 10 * np.random.random((N,p))
Y = 10 * np.random.random((p,M))

# Computing 

# NumPy without Vectorization
def no_vectorization(X, Y):
    Z = np.zeros((N,M))
    for i in range(N) :
        for j in range(M) :
            for k in range(p) :
                Z[i,j] += X[i, k] * Y[k, j]
    return Z

# NumPy with Vectorization
def vectorization(X, Y):
    return X @ Y

# Vectorization 안했을 때 실행 시간 측정
start_time = time.time()
no_vec_result = no_vectorization(X, Y)
end_time = time.time()
print(f"Execution Time Without Vectorization: {end_time - start_time:.6f} seconds")

# Vectorization 했을 때 실행 시간 측정
start_time = time.time()
vec_result = vectorization(X, Y)
end_time = time.time()
print(f"Are they same?: {np.array_equal(no_vec_result, vec_result)}")
print(f"Are they same (allowing floating-point tolerance)?: {np.allclose(no_vec_result, vec_result, atol=1e-8, rtol=1e-5)}")
print(f"Execution Time With Vectorization: {end_time - start_time:.6f} seconds")
