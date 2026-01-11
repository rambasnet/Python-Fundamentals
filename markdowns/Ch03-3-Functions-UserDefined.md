# User-defined Functions
<a href="https://colab.research.google.com/github/rambasnet/FDSPython-Notebooks/blob/master/notebooks/Ch03-3-Functions-UserDefined.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
- http://openbookproject.net/thinkcs/python/english3e/functions.html

## Topics
- how to define and use your own functions
- variables scopes
- how to pass data to functions (by value and reference)
- how to return data from functions
- unit or functional testing with assert

## Functions
- named sequence of statements that execute together to solve some task 
- primary purpose is to help us break the problem into smaller sub-problems or tasks
- two types: fruitful and void/fruitless functions
- must be defined before it can be used or called (two step process)

- concept of function is burrowed from Algebra
- e.g.

    Let's say: $f(x) = x^2+x+1$
    
    $y = f(1) = 1+1+1 = 3$
    
    $y = f(-2) = 4-2+1 = 3$

### Two-step process
1. Define a function
2. Call or use function

### syntax to define function
```python
def functionName( PARAMETER1, PARAMETER2, ... ):
    # STATEMENTS
    return VALUE
```
- PARAMETERS and return statements are OPTIONAL
- function NAME follows the same rules as a variable/identifier name
- recall some built-in functions and object methods have been used in previous chapters...


### syntax to call function
- call function by its name
- use return value(s) if any

```python
VARIABLE = functionName( ARGUMENT1, ARGUMENT2, ...)
```

## Why functions?
**dividing a program into functions or sub-programs have several advantages:**
- give you an opportunity to name a group of statements, which makes your program easier to read and debug
- can make a program smaller by eliminating repetitive code. Later, if you make a change, you only have to make it in one place
- allow you to debug the parts one at a time (in a team) and then assemble them into a working whole
- write once, test, share, and reuse many times (libraries, e.g.)

## Types of functions
- two types: fruitful and fruitless functions

## Fruitless functions
- also called void functions
- they do not **explictly** return a value


```python
# Function definition
# function prints the result but doesn't explictly return anything
def greet():
    print('Hello World!')
```


```python
# Function call
greet()
greet()
```

    Hello World!
    Hello World!



```python
# void/fruitless function; returns None by default
a = greet() # returned value by greet() assigned to a
print('a =', a)
```

    Hello World!
    a = None



```python
type(greet)
```




    function




```python
# function can be assigned to another identifier
myfunc = greet
type(myfunc)
```




    function




```python
myfunc()
```

    Hello World!


## Fruitful functions
- functions that explictly return some value(s) using **return** statement
- more useful functions
- answer returned can be used as intermediate values to solve bigger problems
- can be used and tested independently
- fruitful functions usually take some arguments and return value(s) as answer
- most built-in and library functions are fruitful
- typically return is the last statement to execute; but not necessarily
- function returns back to the caller immidiately after return statement is executed
    - will skip code if any exists after return statement


```python
# fruitful function
def getName():
    name = input("Hi there, enter your full name: ")
    return name
    print(f'Hi {name}, nice meeting you!') # dead code - will not be executed
```


```python
userName = getName()
```

    Hi there, enter your full name: John Smith



```python
userName
```




    'John Smith'




```python
print(f'Hi {userName}, nice meeting you!')
```

    Hi John Smith, nice meeting you!


## Passing data as arguments to functions
- functions are subprograms that may need external data to work with
- you can pass data to functions via parameters/arguments
- can provide 1 or more parameters to pass 1 or more data
- can provide default values to parameters
    - makes the parameter optional when the function is called
- if a function has a required parameter, data must be provided for each required parameter!
    - otherwise, you'll get error!
    
### [Visualize with PythonTutor.com](http://pythontutor.com/visualize.html#code=def%20greet%28name%29%3A%0A%20%20%20%20print%28'Hello%20%7B%7D'.format%28name%29%29%0A%20%20%20%20%0Aprint%28'start'%29%0Agreet%28'John'%29%0Aprint%28'end'%29%0A&cumulative=false&curInstr=0&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
# Function takes one required argument
def greet(name):
    print(f'Hello {name}')
```


```python
# Pass 'John Smith' literal value as an argument for name parameter
greet('John Smith')
```

    Hello John Smith



```python
greet('Jane')
```

    Hello Jane



```python
# Arguments can be variables as well
n = 'Michael Smith'
greet(n)
```

    Hello Michael Smith



```python
n1 = input('Enter your name: ')
greet(n1)
```

    Enter your name: Jake Jones
    Hello Jake Jones



```python
greet()
# How to fix? provide either default value or call it properly
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[22], line 1
    ----> 1 greet()


    TypeError: greet() missing 1 required positional argument: 'name'



```python
# function takes one optional argument
def greet(name="Anonymous"):
    print(f'Hello, {name}')
    
```


```python
# calling greet without an argument
# default value for name will be used!
greet()
```

    Hello, Anonymous



```python
greet('adfasd')
```

    Hello, adfasd



```python
user = input('Enter your name: ')
greet(user) # calling greet with an argument
```

    Enter your name: Jackie Chain
    Hello, Jackie Chain


### [Visualize in PythonTutor.com](http://pythontutor.com/visualize.html#code=%23%20global%20and%20local%20scope%20demos%0A%23%20how%20to%20modify%20global%20variable%20inside%20function%0Avar1%20%3D%20%22Alice%22%20%23global%0Adef%20myFunc%28arg1,%20arg2%29%3A%0A%20%20%20%20%23global%20var1%0A%20%20%20%20var1%20%3D%20%22Bob%22%20%23%20global%20or%20local%3F%20How%20can%20we%20access%20global%20var1%3F%0A%20%20%20%20var2%20%3D%20%22John%22%0A%20%20%20%20print%28'var1%20%3D%20%7B%7D'.format%28var1%29%29%0A%20%20%20%20print%28'var2%20%3D%20',%20var2%29%0A%20%20%20%20print%28'arg1%20%3D%20',%20arg1%29%0A%20%20%20%20print%28'arg2%20%3D%20',%20arg2%29%0A%0AmyFunc%281,%20'Apple'%29%0Aprint%28var1%29&cumulative=false&curInstr=0&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

### Exercise 
- Define a function that takes two numbers as arguments and returns the sum of the two numbers as answer


```python
def add(num1, num2):
    """ add function
    
    Take two numeric values: num1 and num2.
    Calculate and return the sum of num1 and num2.
    """
    total = num1 + num2
    return total
```


```python
# displays the function prototype and docstring below it
help(add)
```

    Help on function add in module __main__:
    
    add(num1, num2)
        add function
        
        Take two numeric values: num1 and num2.
        Calculate and return the sum of num1 and num2.
    



```python
import math
help(math.sin)
```

    Help on built-in function sin in module math:
    
    sin(x, /)
        Return the sine of x (measured in radians).
    



```python
# Test add function
print(add(100, 200))
```

    300



```python
t = add(100.99, -10)
print('sum = ', t)
```

    sum =  90.99



```python
num1 = 15
num2 = 10.5
total = add(num1, num2)
print(f'{num1} a+ {num2} = {total}')
```

    15 a+ 10.5 = 25.5


### Exercise
- Define a function that takes two numbers and returns the product of the two numbers.


```python
# Exercise - complete the following function
def multiply(x, y):
    """
    Function take two numbers: x and y.
    Return the product of x and y.
    """
    
    # FIXME
    pass
```


```python
# Help can be run for user-defined functions as well
help(multiply)
```

    Help on function multiply in module __main__:
    
    multiply(x, y)
        Function take two numbers: x and y.
        Return the product of x and y.
    



```python
# Manually test multiply function
```

## Ways of passing data to functions
- data/values are passed to functions in two ways

### pass by value
- fundamental types and literals (string, int, float) are passed by value
    - values passed as arguments are copied to the corresponding parameters

### pass by reference
- advanced container types (tuple, list, dict, etc.) are passed by reference
    - parameters and corresponding arguments become alias pointing to the same memory location
- this topic will be discussed in the corresponding chapter covering those container types


```python
# Pass by value demo
var1 = 'John' # Global variable

def greetSomeone(para1):
    print('hello', para1)
    var1 = 'Jake' # Local variable
    print('hello again', para1)
    
greetSomeone(var1)
print('var1 = ', var1)
```

    hello John
    hello again John
    var1 =  John


### [visualize pass by value with PythonTutor.com](http://pythontutor.com/visualize.html#code=var1%20%3D%20'John'%20%23%20global%20variable%0Adef%20greetSomeone%28para1%29%3A%0A%20%20%20%20print%28'hello',%20para1%29%0A%20%20%20%20var1%20%3D%20'Jake'%20%23%20local%20variable%0A%20%20%20%20print%28'hello%20again',%20para1%29%0A%20%20%20%20%0AgreetSomeone%28var1%29%0Aprint%28'var1%20%3D%20',%20var1%29&cumulative=false&curInstr=0&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

## Fruitful functions returning multiple values
- functions can return more than 1 values
- multiple comma separated values can be returned
- the values are return as Tuple type (more on this later)


```python
def findAreaAndPerimeter(length, width):
    """
    Take length and width of a rectangle.
    Find and return area and perimeter of the rectangle.
    """
    
    area = length*width
    perimeter = 2*(length+width)
    return area, perimeter
```


```python
print(findAreaAndPerimeter(10, 5))
```

    (50, 30)



```python
a, p = findAreaAndPerimeter(20, 10)
print(f'area = {a} and perimeter = {p}')
```

    area = 200 and perimeter = 60


## Function calling a function
- a function can be called from within another function
- a function can call itself -- called recursion (see Chapter 13)


```python
def average(num1, num2):
    sum_of_nums = add(num1, num2)
    return sum_of_nums/2
```


```python
avg = average(10, 20)
print(f'avg of 10 and 20 = {avg}')
```

    avg of 10 and 20 = 15.0


## Exercises

### exercise 1
Write a function that takes two numbers; subtracts the second from the first and returns the difference.
Write two test cases.


```python
# Solution to exercise 1
def sub(num1, num2):
    return num1 - num2
```

### exercise 2

Write a function that converts seconds to hours, minutes and seconds. Function then returns the values in **HH:MM:SS** format (e.g., 01:09:10)



```python
def get_time(seconds):
    pass
```

### exercise 3

Write a function called hypotenuse that returns the length of the hypotenuse of a right triangle given the lengths of the two legs as parameters.


```python
def hypotenuse(leg1, leg2):
    pass
```

### exercise 4

Write a function $slope(x1, y1, x2, y2)$ that returns the slope of the line through the points $(x1, y1)$ and $(x2, y2)$.

Then use a call to slope in a new function named intercept(x1, y1, x2, y2) that returns the y-intercept of the line through the points $(x1, y1)$ and $(x2, y2)$


```python
def slope(x1, y1, x2, y2):
    pass
```


```python
def intercept(x1, y1, x2, y2):
    pass
```

## Kattis problems requiring functions
- functions are not required to solve problems
- you can use function to solve each and every problem or not use one
- function is required if you must write automated unit tests
- function is recommended for breaking a problem into smaller sub-problems and making the solution modular


```python

```
