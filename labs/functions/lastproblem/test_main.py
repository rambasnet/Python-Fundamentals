"""Module to test functions from main.py
"""

import sys
import main

# test function must start with test_ prefix for pytest to recognize it


def test_answer():
    """Test answer function
    """
    ans = main.answer("Alice")
    expected = "Thank you, Alice, and farewell!"
    assert ans == expected, f"Expected: {expected}, but got: {ans}"
    ans = main.answer("Bob")
    expected = "Thank you, Bob and farewell!"  # FIXME 5: fix the expected output
    assert ans == expected, f"Expected: {expected}, but got: {ans}"
    # FIXME 6: add a new test case to test your answer function
    # FIXME 7: add a new test case to test your answer function
    # FIXME 8: add a new test case to test your answer function
    # FIXME 9: add a new test case to test your answer function
    print("All test cases passed...", file=sys.stderr)


if __name__ == "__main__":
    test_answer()
