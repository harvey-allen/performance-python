import time

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