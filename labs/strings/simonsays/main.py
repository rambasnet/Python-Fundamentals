"""
Strings and Unittest Lab
Updated By: FIXME
CSCI 110 Lab
Date: FIXME

Read and solve - Simon Says: https://open.kattis.com/problems/simonsays  

Algorithm:
		1. Read N
		2. Repeat N times:
      1. Read the input string
      2. Check if the string begins with 'Simon says'
      3. If it does, print the rest of the string after 'Simon says', otherwise ignore the string
"""

import sys

def main():
  """Main function that solves the problem
  """
  # step 1. read data
  N = int(input())
  # FIXME 1 - step 2. repeat the following N times
  # FIXME 2 - read the input string
  # FIXME 3 - call answer function passing the string as an argument
  # FIXME 4 - print the answer if it returns one, otherwise ignore it

def valid_command(command: str):
  """Checks if the string begins with 'Simon says'

  Args:
      command (str): string to check

  Returns:
      bool: True if the string begins with 'Simon says', False otherwise
  """
  # FIXME 5: if the command begins with 'Simon says', return True
  # otherwise, return False
  ans = "FIXME"
  return ans

def answer(command: str):
  """Returns answer given the command or None if the command is not valid

  Args:
      command (str): string to check

  Returns:
      str|None: rest of the string after 'Simon says' if the command is valid, None otherwise
  """
  valid = valid_command(command)
  # FIXME 6: if valid is True, return the rest of the string after 'Simon says', None otherwise
  return None

# test function must start with test_ prefix for pytest to recognize it
def test_valid_command():
  """Test valid_command function
  """
  ans = valid_command("Simon says do this")
  expected = True
  assert ans == expected, f"Expected: {expected}, but got: {ans}"
  ans = valid_command("do this")
  expected = False
  assert ans == expected, f"Expected: {expected}, but got: {ans}"
  # FIXME 7: add a new case to test valid_command function
  # FIXME 8: add a new case to test valid_command function
  print("All test cases passed...", file=sys.stderr)

# test function must start with test_ prefix for pytest to recognize it
def test_answer():
  """Test answer function
  """
  ans = answer("Simon says do this")
  expected = " do this"
  assert ans == expected, f"Expected: {expected}, but got: {ans}"
  # FIXME 9: add a new case to test answer function
  # FIXME 10: add a new case to test answer function
  print("All test cases passed...", file=sys.stderr)


if __name__ == "__main__":
  # call the main function if the script is run from the command line
  main()
