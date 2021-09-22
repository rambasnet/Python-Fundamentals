"""
This is named main module. 
Declares question, answer, and areaOfCircle function
"""

import math # first import standard library modules
import module2 # then import user-defined modules
# what happens if the imported the names following way? Uncomment, run the module and find out...
# from module2 import *

# global variables
question = "What is the meaning of Life, the Universe, and Everything?"
answer = 42

# a function
def areaOfCircle(radius):
    """
    Given radius of a circle, finds and returns its area.
    """
    return math.pi*radius**2

def printModuleInfo():
    import module2
    print(__doc__)
    print(__file__)
    print(__name__)
    print(__package__)
    print('module2.__doc__ = ', module2.__doc__)
    print('module2.__file__ = ', module2.__file__)
    print('module2.__name__ = ', module2.__name__)
    print('module2.__package__ = ', module2.__package__)

def accessModule2Names():
    print(module2.question)
    print(module2.answer)

def accessThisModuleNames():
    print(question)
    print(answer)
    area = areaOfCircle(3)
    print("area = {:.2f}".format(area))

if __name__ == '__main__':
    accessModule2Names()
    accessThisModuleNames()    
