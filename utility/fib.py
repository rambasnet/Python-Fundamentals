#! /usr/bin/env python3

""" Fibonacci Module """

def fib(n):
    """ Calculates the n-th Fibonacci number iteratively 

    >>> fib(1)
    1
    >>> fib(3)
    2
    >>> fib(10)
    55
    >>> fib(13)
    233
    >>> fib(15)
    610
    >>> fib(-1)
    Traceback (most recent call last):
        ...
    ValueError: expected integer
    """
    if n < 1:
        raise ValueError("expected integer")

    a, b = 1, 1
    for i in range(2, n+1):
        a, b = b, a + b
    return a

def fibList(n):
    """ Creates and retuns a list of Fibonacci 
    numbers up to the n-th generation 
    
    >>> fibList(2)
    [1, 1]
    >>> fibList(5)
    [1, 1, 2, 3, 5]
    
    """

    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1]+fibs[-2])
    return fibs

def _test():
    import doctest
    """
    if fib(0) == 0 and fib(10) == 55 and fib(50) == 12586269025:
        print("Test for the fib function was successful!")
    else:
        print("The fib function is returning wrong values!")
    """
    #assert fib(0)==0, "fib(0) didn't return 0"
    #assert fib(2)==2, "fib(2) didn't return 2"
    doctest.testmod()
    
if __name__ == "__main__":
    _test()