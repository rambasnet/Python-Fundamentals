"""
This module uses the fibos package defined in the root repository folder.
"""

import fibos.fibo as myfib
from fibos import fibo

def main():
  print('First 10 numbers in Fibonacci seris:')
  myfib.fib(10)
  fibo.fib2(10)

if __name__ == "__main__":
  main()

