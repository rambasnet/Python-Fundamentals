"""
This is the "example" module.

The example module supplies one function, factorial().  For example,
>>> factorial(5)
120
"""

def factorial(n):
    """ given a positive integer n, returns its factorial 
    >>> factorial(1)
    1
    >>> factorial(5)
    120
    >>> factorial(20)
    2432902008176640000
    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0

    Factorials of floats are OK, but the float must be an exact integer:
    >>> factorial(30.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
    >>> factorial(30.0)
    265252859812191058636308480000000

    It must also not be ridiculously large:
    >>> factorial(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: n too large
    """
    import math
    if type(n) != int:
        raise TypeError("an integer is required.")
    if n < 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n+1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

def _test():
    assert factorial(1) == 1, "1! != 1"
    assert factorial(5) == 120, "5! != 120"
    assert factorial(20) == 2432902008176640000
    # factorial of -ve integer
    # factorial of non-integer

def _test1():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    #_test()
    _test1()
