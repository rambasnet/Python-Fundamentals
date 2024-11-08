"""
This is module 2. Defines question, answer and
circumference function
"""
import math
# import module1

QUESTION = "What is your quest?"
ANSWER = "To seek the holy grail."


def circumference(radius):
    """
        Given radius of a circle, finds and returns its circumference.
    """
    return math.pi*radius*2


def test():
    """
    Function to test names defined in this module.
    """
    print(QUESTION)
    print(ANSWER)
    print(f"circumference={circumference(3)}")


# what happens if the import guard is not used and this module is imported?
# comment out the following if statement and directly call test() and run main.py module to find out!
if __name__ == '__main__':
    test()
