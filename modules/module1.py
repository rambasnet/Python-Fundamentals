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
    print(question)
    print(answer)
    area = areaOfCircle(3)
    print("area = {:.2f}".format(area))
