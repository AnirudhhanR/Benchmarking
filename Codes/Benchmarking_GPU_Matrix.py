import tensorflow as tf
import time

def gpu_worker():
    with tf.device('GPU:0'):
        x = tf.random.uniform([10000, 10000])
        y = tf.random.uniform([10000, 10000])
        tf.matmul(x, y)

def gpu_benchmark():
    start_time = time.time()
    gpu_worker()
    return time.time() - start_time

print("Time taken to complete the GPU benchmark: ", gpu_benchmark(), "seconds")
