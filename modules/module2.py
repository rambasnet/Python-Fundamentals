"""
This is module 2. Defines question, answer and
circumference function
"""
import math
#import module1

question = "What is your quest?"
answer = "To seek the holy grail."


def circumference(radius):
    """
        Given radius of a circle, finds and returns its circumference.
    """
    return math.pi*radius*2


if __name__ == '__main__':
    print(question)
    print(answer)
    print("circumference = {:.2f}".format(circumference(3)))
