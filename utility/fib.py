#! /usr/bin/env python3
import math
""" Fibonacci Module """

def fib(n):
    """ Calculates the n-th Fibonacci number iteratively 
    """
    
    if n < 1:
        raise ValueError("expected integer")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    a, b = 1, 1
    for i in range(2, n+1):
        a, b = b, a + b
    return a

def fibList(n):
    """
    returns first n fibonacci suequence as list 
    """
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1]+fibs[-2])
    return fibs
