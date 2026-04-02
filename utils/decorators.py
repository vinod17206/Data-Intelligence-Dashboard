
import time
from functools import wraps
from datetime import datetime

def log_function(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] {func.__name__} called at {datetime.now()}")
        return func(*args, **kwargs)
    return wrapper

def time_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        print(f"[TIME] {func.__name__}: {time.time()-start:.4f}s")
        return result
    return wrapper
