"""
Kattis - The Last Problem
User-defined functions and Unittest Lab
Updated By: FIXME
CSCI 110 Lab
Date: FIXME

Read and solve - The Last Problem: https://open.kattis.com/problems/thelastproblem

Algorithm:
		1. Read the input string using function
		3. Create the output as asked and print it using function
    3. Test functions using test cases
"""

import sys

def main():
  # step1. read data
  data = readData()
  # FIXME 1: Call answer function passing data as an argument
  # store the returned result into ans variable
  ans = "FIXME"
  # print answer
  # FIXME 2: print the answer as shown in the sample output

# Function reads the data from std input and returns it
def readData():
  # FIXME 3: using inpyt read and store the data into data variable
  # FIXME 4: return data
  pass

# Function creates the twilight output and returns it
def answer(data):
  # FIXME 5: create the output as asked and store it into ans variable
	ans = f"Thank you, {data}, and farewell!"
	return ans

def testAnswer():
  ans = answer("Alice")
  expected = "Thank you, Alice, and farewell!"
  assert ans == expected, f"Expected: {expected}, but got: {ans}"
  ans = answer("Bob")
  expected = "Thank you, Bob, and farewell!" # FIXME 5: fix the expected output
  assert ans == expected, f"Expected: {expected}, but got: {ans}"
  # FIXME 6: add a new test case to test your answer function
  # FIXME 7: add a new test case to test your answer function
  # FIXME 8: add a new test case to test your answer function
  # FIXME 9: add a new test case to test your answer function
  print("All test cases passed...", file=sys.stderr)

if __name__ == "__main__":
  testAnswer() # call testAnswer function
  # FIXME 10: call main function
