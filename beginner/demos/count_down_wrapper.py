#! /usr/bin/env python3
"""Module to demonstrate Function Decorators."""

__author__ = "Ram Basnet"
__copyright__ = "Copyright 2018"
__license__ = "MIT"

import time
import os
from functools import wraps 
# wraps - decorator function for preserving the name of the function being decorated

def clearScreen(func):
    """Use system command to clear screen: https://docs.python.org/3/library/os.html"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        if os.name == 'nt': # nt, posix, java
            os.system('cls')
        else:
            os.system('clear')
        return func(*args, **kwargs)
    return wrapper

def slow_down(func):
    """Sleep 1 second before calling the function."""
    
    @wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1) # sleep for a second
        return func(*args, **kwargs) # call and return the result from the func
    return wrapper_slow_down


# a simple count down function
@slow_down
# @clearScreen  # TODO: uncomment this line to apply clearScreen decorator
def countDown(from_number):
    """A simple recursive countDown function that uses 2 function decorators."""

    if from_number <= 0:
        print('Blast off!')
    else:
        print(from_number)
        countDown(from_number-1)


if __name__ == "__main__":
    countDown(10)