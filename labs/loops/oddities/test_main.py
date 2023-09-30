"""Test cases for main.py"""
import main


def test_answer():
    """Test answer function."""
    ans = main.answer(10)
    expected = "10 is even"
    assert ans == expected, f"Expected: {expected}, but got: {ans}"


def test_answer2():
    """Test answer function for negavitve odd number."""
    ans = main.answer(-199)
    expected = "-199 is odd"
    assert ans == expected, f"Expected: {expected}, but got: {ans}"


# FIXME 6: add a new test case  function to test your answer function
# FIXME 7: add a new test case function to test your answer function


def test_odd_even():
    """Test odd_even function.
    """
    ans = main.odd_even(10)
    expected = "even"
    assert ans == expected, f"Expected: {expected}, but got: {ans}"


def test_odd_even2():
    """Test odd_even function for negavitve odd number
    """
    ans = main.odd_even(-199)
    expected = "odd"
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

# FIXME 8: add a new test case function to test your answer function
# FIXME 9: add a new test case function to test your answer function
