#!/usr/bin/python3

# This is a naive (inefficient) algorithm for finding the nth fibonacci number,
# but it's pretty fast when you add a least recently used cache to fib(n)
# Usage: $ python3 naive_fib.py <n>

from functools import lru_cache
from sys import argv

@lru_cache(maxsize=None)
def fib(n):
  if n == 0 or n == 1:
    return 1
  else:
    return fib(n-1) + fib(n-2)

if __name__=='__main__':
    print(fib(int(argv[1])))

