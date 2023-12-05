"""
Date: FIXME

Using OOP concept, solve: Bijele - https://open.kattis.com/problems/bijele 

Algorithm:
    1. Create chess.py module to define the the Chess class
    2. Define the __init__ method to initialize the Chess class
    3. Define the __str__ method to return the string representation of the Chess class
    4. Define the __sub__ method to return the difference between two Chess objects
    5. print the difference as shown in the sample output
"""

from chess import Chess


def main() -> None:
    # the actual chess pieces count
    actual_chess = Chess(1, 1, 2, 2, 2, 8)
    # FIXME - read the chess pieces count from the input
    pieces = 0, 0, 0, 0, 0, 0  # FIXME
    given_chess = Chess(*pieces)
    # FIXME - create a Chess object using the input data
    # FIXME - print the difference between the actual and input chess pieces count
    ans = actual_chess - given_chess  # creates a new Chess object
    print(ans)


if __name__ == "__main__":
    main()
