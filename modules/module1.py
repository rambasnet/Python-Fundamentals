"""
This is module 1. Declares question, answer, and
areaOfCircle function
"""
import math
import module2

question = "What is the meaning of Life, the Universe, and Everything?"
answer = 42


def areaOfCircle(radius):
    """
    Given radius of a circle, finds and returns its area.
    """
    return math.pi*radius**2


if __name__ == '__main__':
    print('module1.__doc__ = ', __doc__)
    print('module1.__file__ = ', __file__)
    print('module1.__name__ = ', __name__)
    print('module1.__package__ = ', __package__)
    print('module2.__doc__ = ', module2.__doc__)
    print('module2.__file__ = ', module2.__file__)
    print('module2.__name__ = ', module2.__name__)
    print('module2.__package__ = ', module2.__package__)
    print(question)
    print(answer)
    area = areaOfCircle(3)
    print("area = {:.2f}".format(area))
