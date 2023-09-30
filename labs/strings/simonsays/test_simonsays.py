"""Test cases for simonsays.py
"""

import simonsays


def test_valid_command():
    """Test valid_command function.
    """
    ans = simonsays.valid_command("Simon says do this")
    expected = True
    assert ans == expected, f"Expected: {expected}, but got: {ans}"


def test_valid_command2():
    """Test valid_command function."""
    ans = simonsays.valid_command("do this")
    expected = False
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

# FIXME 7: add a new test case function to test valid_command function

# FIXME 8: add a new test case function to test valid_command function


def test_answer():
    """Test answer function.
    """
    ans = simonsays.answer("Simon says do this")
    expected = " do this"
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

# FIXME 9: add a new test case function to test answer function

# FIXME 10: add a new test case function to test answer function
