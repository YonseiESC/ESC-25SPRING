import numpy as np
import time

# 데이터 크기 설정
N = 100_000_000

# Python
def python_sum(arr):
    total = 0
    for x in arr:
        total += x
    return total

# NumPy
def numpy_sum(arr):
    return np.sum(arr)

data = np.arange(N, dtype=np.float64)

# Python 실행 시간 측정
start_time = time.time()
python_result = python_sum(data)
end_time = time.time()
print(f"Python Result: {python_result}")
print(f"Python Execution Time: {end_time - start_time:.6f} seconds")

# NumPy 실행 시간 측정
start_time = time.time()
numpy_result = numpy_sum(data)
end_time = time.time()
print(f"NumPy Result: {numpy_result}")
print(f"NumPy Execution Time: {end_time - start_time:.6f} seconds")
