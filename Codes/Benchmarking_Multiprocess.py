import multiprocessing
from multiprocessing import Process
import time

def worker(n):
    for i in range(n):
        result = 0
        for j in range(n):
            result += 1
    return result

def benchmark():
    start_time = time.time()
    n = 10**7
    processes = [Process(target=worker, args=(n,)) for i in range(multiprocessing.cpu_count())]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    return time.time() - start_time

if __name__ == "__main__":
    freeze_support()

print("Time taken to complete the benchmark: ", benchmark(), "seconds")
