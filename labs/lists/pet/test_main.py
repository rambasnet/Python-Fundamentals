"""Moduel to test important function in main.py
"""

import sys
import main

# test function must start with test_ prefix for pytest to recognize it
def test_answer():
  """Tests answer function
  """
  ans = main.answer([10, 20, 11, 15, 13])
  expected = "2 20"
  assert ans == expected, f"Expected: {expected}, but got: {ans}"
  ans = main.answer([6, 10, 8, 4, 15])
  expected = "5 15"
  assert ans == expected, f"Expected: {expected}, but got: {ans}"
  # FIXME 10: add 2 more test cases
  print("All test cases passed...", file=sys.stderr)


# test function must start with test_ prefix for pytest to recognize it
def test_list_sum():
  """Tests list_sum function
  """
  ans = main.list_sum([6, 7, 8, 10])
  expected = 31
  assert ans == expected, f"Expected: {expected}, but got: {ans}"
  ans = main.list_sum([2, 3, 4, 5])
  expected = 14
  assert ans == expected, f"Expected: {expected}, but got: {ans}"
  # FIXME 9: add 2 more test cases
  print("All test cases passed...", file=sys.stderr)

