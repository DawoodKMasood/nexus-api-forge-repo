from fastapi import HTTPException
import time
from functools import wraps

def rate_limiter(limit: int, period: int):
    def decorator(func):
        last_reset = time.time()
        calls = 0

        @wraps(func)
        async def wrapper(*args, **kwargs):
            nonlocal last_reset, calls
            now = time.time()
            
            if now - last_reset > period:
                calls = 0
                last_reset = now
            
            if calls >= limit:
                raise HTTPException(status_code=429, detail="Rate limit exceeded")
            
            calls += 1
            return await func(*args, **kwargs)
        
        return wrapper
    return decorator