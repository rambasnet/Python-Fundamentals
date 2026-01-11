# Unittest

<a href="https://colab.research.google.com/github/rambasnet/Python-Fundamentals/blob/master/notebooks/Ch19-UnitTest.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

## Topics
- unit testing
- test-driven development
- doctest

## Test
- coders/software engineers spend as much time debugging and testing their codes as they spend on developing/writing the codes
- "To err is human, but to preserve in error is diabolic." - anonymous
    - this more than two thousand-years old proverb fits with coding
- "Program testing can be used to show the presence of bugs, but never to show their absence!" - Edsger W. Dijkstra
- code coverage is used to measure the degree to which the source code of a program is executed when a particular test suite runs
- various coverage criteria:
    - function coverage
    - statement coverage
    - branch coverage
    - condition coverage
    - loop coverage
    - data-flow coverage
    - function entry/exit coverage
- full path coverage is usually impractical or impossible
    - module with a succession of $n$ decision in it can have up to $2^n$ paths
    - loops can result in an infinite number of paths

## Test-driven development
- write test cases before or simultaneously along with the code implementation
- 3 simple ways to test your code natively at the functional level
    1. assert statements - natively supported in many languages; as we've used before
    2. doctest - simple, interactive technique, but makes the source code look messy, as they're defined inside the same function and module
    3. unit test - preferred; separates the code with test 

## doctest
- https://docs.python.org/3/library/doctest.html
- to check that a module’s docstrings are up-to-date by verifying that all interactive examples still work as documented.
- to perform regression testing by verifying that interactive examples from a test file or a test object work as expected.
- to write tutorial documentation for a package, liberally illustrated with input-output examples. Depending on whether the examples or the expository text are emphasized, this has the flavor of “literate testing” or “executable documentation”.

### doctest demo
- see `factorial.py` in `demos/utility` package for doctest example
- to run the doctest, run `python -m doctest -v <module.py>` from command line

```python
python -m doctest -v demos/utility/factorial.py
```


```python

```

## Unittest Library Example
- python provides unittest standard library to help with unit testing
- documentation: https://docs.python.org/dev/library/unittest.html#module-unittest
- see `test_fibonacci.py` in `demos/utility` package for unittest example
- `pytest` can also be used to run unittest test cases
- run `pytest -v` from command line to run the test suite

## Exercise
1. Write unittest to test functions in demos/utility/factorial.py module.
2. Solve kattis problems with along with unit testing for each problem


```python

```
