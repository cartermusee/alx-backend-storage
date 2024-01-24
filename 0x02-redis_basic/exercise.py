#!/usr/bin/env python3
"""module for redis"""
import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """function to increase
    method: functon to decoarte
    Returns: a callable
    """
    @wraps(method)
    def wrapper(self, *args, **kwds):
        value = method.__qualname__
        self._redis.incr(value)
        return method(self, *args, **kwds)
    return wrapper

def call_history(method: Callable) -> Callable:
    """call all history function
    Keyword arguments:
    method: a callable func
    Return: callable
    """
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.rpush(inputs, str(args))
        data = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(data))
        return data
    return wrapper

def replay(method: Callable) -> None:
    """history of func
    Keyword arguments:
    method: callables
    Return: none
    """
    name = method.__qualname__
    cache = redis.Redis()
    call = cache.get(name).decode("utf-8")
    print("{} was called {} times".format(name, call))
    inputs = cache.lrange(name + "inputs", 0, -1)
    outputs = cache.lrange(name + "outputs", 0, -1)
    for i, j in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(name, i.decode("utf-8"), j.decode("utf-8")))


class Cache():
    """class for cache"""
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()
    
    @count_calls
    def store(self, data: Union[str, int, bytes, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def  get(self, key: str, fn: Optional[Callable] = None) -> Union[str, int, bytes, float, None]:
        data = self._redis.get(key)

        if data is None:
            return None
        if fn is not None:
            return fn(data)
        
        return data
    
    def get_str(self, key: str) -> str:
        """chenge to string
        Keyword arguments:
        key: the key
        Return: strin
        """
        val = self._redis.get(key)
        return val.decode('utf-8')

    def get_int(self, key: str) -> int:
        """get an int"""
        val = self._redis.get(key)
        try:
            val = int(val.decode('utf-8'))
        except Exception:
            val = 0
        return val