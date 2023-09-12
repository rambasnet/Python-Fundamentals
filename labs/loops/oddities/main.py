"""
Loops and Unittest Lab
Updated By: FIXME
CSCI 110 Lab
Date: FIXME

Read and solve - Oddities: https://open.kattis.com/problems/oddities 

Algorithm:
		1. Read N
		2. Repeat N times:
      1. Read the input number
      2. Check if the number is odd or even
      3. Print the result as shown in the sample output
"""

import sys

def odd_even(number: int):
  """Checks if the number is odd or even

  Args:
      number (int): number to check odd or even

  Returns:
      str: 'odd' if the number is odd, 'even' otherwise
  """
  # FIXME 1: if the number divided by 2 has 0 remainder, return 'even'
  # otherwise, return 'odd'
  ans = "FIXME"
  return ans

def main():
  """Main function that solves the problem
  """
  # step 1. read data
  N = read_int_data()
  # FIXME 2 - step 2. repeat N times
  # FIXME 2.1 - read the input number
  # FIXME 2.2 - call answer function passing the number as an argument
  # FIXME 2.3 - print the answer as shown in the sample output

# Function reads the data from std input and returns it
def read_int_data():
  """Reads the data from std input and returns it

  Returns:
      int: data read from std input as an int
  """
  # FIXME 3: using input read and store the data into data variable
  # FIXME 4: convert the data into an int and return it
  pass

def answer(num: int):
  """Creates the final answer and returns it given the number

  Args:
      num (int): number to check odd or even

  Returns:
      bool : True if the number is even, False otherwise
  """
  ans = odd_even(num)
  return f'{num} is {ans}'

if __name__ == "__main__":
  # FIXME 10: call main function
  pass
