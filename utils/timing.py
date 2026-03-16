import time
from functools import wraps
from typing import Callable, TypeVar, Any

F = TypeVar("F", bound=Callable[..., Any])


def measure(func: F) -> F:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        result.elapsed = time.perf_counter() - start
        return result
    return wrapper  # type: ignore[return-value]
