import os
import time
from functools import wraps

import psutil

from setting import logger


def timed_method(func):
    """Decorator to time a method and log the execution time."""

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        logger.info(f"Method {func.__name__} executed in {elapsed_time:.4f} seconds.")
        return result

    return wrapper


def measure_performance(label):
    """Decorator to measure time, CPU, and memory usage of a function"""
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Setup performance measurement
            import tracemalloc
            tracemalloc.start()

            # Measure before execution
            start_time = time.time()
            start_cpu = psutil.cpu_percent(interval=None)
            process = psutil.Process(os.getpid())
            start_memory = process.memory_info().rss / (1024 * 1024) # in MB

            # Execute the function
            result = func(*args, **kwargs)

            # Measure after execution
            end_time = time.time()
            end_cpu = psutil.cpu_percent(interval=None)
            end_memory = process.memory_info().rss / (1024 * 1024) # in MB
            current, peak = tracemalloc.get_traced_memory()

            # Log performance metrics
            logger.info(f"\nPerformance metrics for: {label}")
            logger.info(f"Time taken: {end_time - start_time:.4f} seconds")
            logger.info(f"CPU usage (start/end): {start_cpu}% / {end_cpu}%")
            logger.info(f"Memory usage (start/end): {start_memory:.2f}MB / {end_memory:.2f}MB")
            logger.info(f"Memory allocated during operation: {current / (1024 * 1024):.2f}MB")
            logger.info(f"Peak memory usage: {peak / (1024 * 1024):.2f}MB")

            # Clean up
            tracemalloc.stop()

            return result
        return wrapper
    return decorator