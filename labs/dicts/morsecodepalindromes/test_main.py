"""Module to test functions in main.py 
"""

import main

def test_convert_to_palindrome1():
  actual_ans = main.convert_to_morse('AN')
  expected_ans = '.--.'
  assert actual_ans == expected_ans

# FIXME 6 - write 3 more test cases to test convert_to_palindrome function

def test_ispalindrome1():
  ans = main.is_palindrome('.--.')
  expected = 1
  assert ans == expected

# FIXME 7 - Write 3 more test cases to test is_palindrome function
