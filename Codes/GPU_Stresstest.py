import cupy as cp
import time

def gpu_worker(n):
    x = cp.random.rand(n, n)
    y = cp.random.rand(n, n)
    cp.dot(x, y)

def gpu_benchmark(n):
    start_time = time.time()
    gpu_worker(n)
    return time.time() - start_time

n = 10000
print("Time taken to complete the GPU benchmark: ", gpu_benchmark(n), "seconds")