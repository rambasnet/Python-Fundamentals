import sys
import main

# test function must start with test_ prefix for pytest to recognize it
def test_answer():
  """Test answer function
  """
  ans = main.answer(10)
  expected = "10 is even"
  assert ans == expected, f"Expected: {expected}, but got: {ans}"
  ans = main.answer(-199)
  expected = "-199 is odd"
  assert ans == expected, f"Expected: {expected}, but got: {ans}"
  # FIXME 6: add a new test case to test your answer function
  # FIXME 7: add a new test case to test your answer function
  print("All test cases passed...", file=sys.stderr)

def test_odd_even():
  """Test odd_even function
  """
  ans = main.odd_even(10)
  expected = "even"
  assert ans == expected, f"Expected: {expected}, but got: {ans}"
  ans = main.odd_even(-199)
  expected = "odd"
  assert ans == expected, f"Expected: {expected}, but got: {ans}"
  # FIXME 8: add a new test case to test your answer function
  # FIXME 9: add a new test case to test your answer function
  print("All test cases passed...", file=sys.stderr)
  