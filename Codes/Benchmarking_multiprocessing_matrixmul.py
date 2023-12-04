import multiprocessing
import numpy as np
import time

def worker(n):
    x = np.random.rand(n, n)
    y = np.random.rand(n, n)
    return np.dot(x, y)

def benchmark():
    start_time = time.time()
    n = 2500
    processes = [multiprocessing.Process(target=worker, args=(n,)) for i in range(multiprocessing.cpu_count())]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    return time.time() - start_time

print("Time taken to complete the benchmark: ", benchmark(), "seconds")