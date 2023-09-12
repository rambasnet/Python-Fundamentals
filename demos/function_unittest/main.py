"""
Kattis problem - <NAME>
CSCI 110
<SEMESTER> <YEAR>
Author: <YOUR NAME>
Date: <TODYA'S DATE>

Problem Satement: <BRIEFFLY DESCRIBE WHAT THE PROBLEM IS ABOUT>

Algorithm Steps:
1. 
2.
...
"""

def answer() -> str:
  """Function returns "Hello World!" string.

  Returns:
      str: returns "Hello World!"
  """
  return 'Hello World!'

def add(a: int, b:int) -> int:
  """Function adds two integers and returns the sum.

  Args:
      a (int): 1st operand
      b (int): 2nd operand

  Returns:
      int: return sum of a and b
  """
  return a+b

def main():
  """Main function that solves the problem.
  """

  # Read data
  # call anwer() function
  # print final answer
  ans = answer()
  print(ans)

if __name__ == "__main__":
  # call main() if the module is run as the main module
  main()
