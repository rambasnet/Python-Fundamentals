import sys
import main

# test function must start with test_ prefix for pytest to recognize it
def test_valid_command():
  """Test valid_command function
  """
  ans = main.valid_command("Simon says do this")
  expected = True
  assert ans == expected, f"Expected: {expected}, but got: {ans}"
  ans = main.valid_command("do this")
  expected = False
  assert ans == expected, f"Expected: {expected}, but got: {ans}"
  # FIXME 7: add a new case to test valid_command function
  # FIXME 8: add a new case to test valid_command function
  print("All test cases passed...", file=sys.stderr)

# test function must start with test_ prefix for pytest to recognize it
def test_answer():
  """Test answer function
  """
  ans = main.answer("Simon says do this")
  expected = " do this"
  assert ans == expected, f"Expected: {expected}, but got: {ans}"
  # FIXME 9: add a new case to test answer function
  # FIXME 10: add a new case to test answer function
  print("All test cases passed...", file=sys.stderr)
