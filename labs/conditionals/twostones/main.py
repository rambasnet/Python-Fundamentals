"""
Kattis - Take Two Stones
Conditional Logic Lab
Updated By: FIXME
CSCI 110 Lab
Date: FIXME

Read and solve the Kattis problem: https://open.kattis.com/problems/twostones 

Algorithm Steps:
  1. Read the number of stones
  2. Check if the number of stones is odd or even
  3. Check oddity of the number of stones
  4. Print the winner
    4.a. If the number is odd, Alice wins.
    4.b. Otherwise, Bob wins.
"""

import sys

def main():
  if len(sys.argv) == 2 and sys.argv[1] == "test":
    # FIXME 1: call testOddOrEven function that tests oddOrEven function
    # FIXME 2: call the test function that tests answer function
    pass
  else:
    # FIXME 3: read the number of stones
    # FIXME 4: call answer function passing the number of stones as an argument
    # FIXME 5: print the answer as shown in the sample output
    pass

def oddOrEven(number: int):
  # FIXME 4: if the number divided by 2 has 0 remainder, return 'even'
  # otherwise, return 'odd'
  ans = "FIXME"
  return ans

def answer(stone: int):
  evenorodd = oddOrEven(stone)
  if (evenorodd == "odd"):
    return "Alice"
  else:
    return "Bob"

def testOddOrEven():
  number = 99999
  expected = "odd"
  ans = oddOrEven(number)
  assert(oddOrEven(number) == ans), f"Expected: {expected}, but got: {ans}"
  assert(oddOrEven(200) == "even"), f"Expected: even, but got: {oddOrEven(200)}"
  # FIXME 5: Write 3rd test case
  # FIXME 6: Write 4th test case
  print("All test cases passed for oddOrEven()...", file=sys.stderr)

# FIXME 7: Write a function to test answer function
# Write at least 3 test cases

if __name__ == "__main__":
  main() # call main function
