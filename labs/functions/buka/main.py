"""
Built-in and Library Functions Lab
Updated By: FIXME
CSCI 110 Lab
Date: FIXME

Solution to Kattis problem - Buka: https://open.kattis.com/problems/buka

Algorithm steps:
  1. read the first operand into a variable
  3. read the operator into a variable
  3. read the 2nd operand into a variable
  4. concatenate the varialbes into a single string
  5. run the eval into the concatenated string
  6. print the result of the eval as the answer
"""

import sys

# define a main function
def main():
  """Main function that solves the problem
  """
  # read the first operand into A variable
  A = input()
  # FIXME3 - read the operator into a variable named operator
  # FIXME4 - read the 2nd operand into a B variable
  # FIXME5 - concatenate all three variables into a single variable called equation
  ans = '' # FIXME - call eval(equation) and assign the return value into ans variable
  # print the answer using sys library's stdout.write() method
  sys.stdout.write(f'{ans}\n')

# call main() funtion to execute it
main()

