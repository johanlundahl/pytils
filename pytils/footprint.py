import time
from datetime import datetime

def elapsed_time(func):
  def wrapper(*args, **kwargs):
    start = datetime.now()
    res = func(*args, **kwargs)
    elapsed = datetime.now() - start
    print('{} elapsed in {}'.format(func.__name__, elapsed))
    return res
  return wrapper

def called_at(func):
  def wrapper(*args, **kwargs):
    start = datetime.now()
    print('{} {}{}'.format(start, func.__name__, args))
    return func(*args, **kwargs)
  return wrapper

