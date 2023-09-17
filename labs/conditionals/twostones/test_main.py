"""Module to test important functions in main.py
"""

import sys
import main

# test function must start with test_ prefix for pytest to recognize it


def test_odd_even():
    """Function to test odd_even function
    """
    number = 99999
    expected = "odd"
    ans = main.odd_even(number)
    assert (main.odd_even(number) ==
            ans), f"Expected: {expected}, but got: {ans}"
    assert (main.odd_even(200) ==
            "even"), f"Expected: even, but got: {main.odd_even(200)}"
    # FIXME 5: Write 3rd test case
    # FIXME 6: Write 4th test case
    print("All test cases passed for oddOrEven()...", file=sys.stderr)

# FIXME 7: Write a function to test answer function
# Write at least 3 test cases
