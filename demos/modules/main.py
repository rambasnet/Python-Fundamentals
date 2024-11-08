"""
This is named main module. 
Declares question, answer, and areaOfCircle function
"""

import math  # first import standard library modules
import module2  # then import user-defined modules
# what happens if the imported the names following way? Uncomment, run the module and find out...
# from module2 import *

# global variables/CONSTANTS
QUESTION = "What is the meaning of Life, the Universe, and Everything?"
ANSWER = 42

# a function


def area_of_circle(radius):
    """
    Given radius of a circle, finds and returns its area.
    """
    return math.pi*radius**2


def print_module_info() -> None:
    """Prints module information
    """
    import module2
    print(__doc__)
    print(__file__)
    print(__name__)
    print(__package__)
    print('module2.__doc__ = ', module2.__doc__)
    print('module2.__file__ = ', module2.__file__)
    print('module2.__name__ = ', module2.__name__)
    print('module2.__package__ = ', module2.__package__)


def access_module2_names() -> None:
    """Access names defined in module2
    """
    print(module2.QUESTION)
    print(module2.ANSWER)


def access_this_module_names() -> None:
    """Access names defined in this module
    """
    print(QUESTION)
    print(ANSWER)
    area = area_of_circle(3)
    print(f"area = {area:.2f}")


if __name__ == '__main__':
    access_module2_names()
    access_this_module_names()
