import time
from functools import wraps


def measure(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        result.elapsed = time.perf_counter() - start
        return result
    return wrapper
