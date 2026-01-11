# Exceptions
<a href="https://colab.research.google.com/github/rambasnet/Python-Fundamentals/blob/master/notebooks/Ch16-Exceptions.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>


http://openbookproject.net/thinkcs/python/english3e/exceptions.html
- dealing with bugs is normal part of programming
- debugging is a very handy programming skill

## category of bugs
- syntax errors
- logical/semantic errors
- runtime errors/exceptions

## exceptions
- when runtime error occurs, it creates and throws an exception object
- program halts; Python prints out the traceback with exception name and message
- https://docs.python.org/3/tutorial/errors.html


```python
print(55/0)
```


    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    <ipython-input-1-86210e37274a> in <module>
    ----> 1 print(55/0)
    

    ZeroDivisionError: division by zero



```python
alist = []
print(alist[0])
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-2-00bfde7948e0> in <module>
          1 alist = []
    ----> 2 print(alist[0])
    

    IndexError: list index out of range



```python
atup = ('a', 'b', 'c')
atup[0] = 'A'
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-3-92001c61f3b5> in <module>
          1 atup = ('a', 'b', 'c')
    ----> 2 atup[0] = 'A'
    

    TypeError: 'tuple' object does not support item assignment


- each exception has two parts- Name: description

## catching exceptions
- use try and except blocks
- try statement has several separate clauses/parts
<pre>
    try:
        # statement(s) thay may potentially throw(s) exception
    except ExceptionName1:
        # catch specific exception ExceptionName1
        # statement(s) to handle the exception
    [except ExceptionName2 as err:
        # statements
    ]
    [except:
        # catch any error not caught by previous except blocks
    ]
    [else:
        # follows all except clause
        # executes if try clause does NOT raise an exception
    ]
    [finally:
        # clean-up actions that must be executed under all circumstances; 
        # exectued on the way out when try block is left via a break, continue, or return statement
    ]
</pre>
- <em>[ ] optional </em> 

### example 1


```python
try:
    x = int(input("Enter dividend: "))
    y = int(input("Enter divisor: "))
    quotient = x/y
    remainder = x%y
except ZeroDivisionError as ex:
    print('Exception occured:', ex)
    print('arguments:', ex.args)
except ValueError as ex:
    print(ex)
except Exception as ex1:
    print('Some exception occured...', ex1)
except:
    print('some exception flew by...')
else:
    print("quotient=", quotient)
    print("remainder=", remainder)
finally:
    print("executing finally clause")
```

    Enter dividend: 10
    Enter divisor: 2
    quotient= 5.0
    remainder= 0
    executing finally clause



```python
int(input('enter a number'))
```

    enter a numberadsf



    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-9-8f4f55f39064> in <module>
    ----> 1 int(input('enter a number'))
    

    ValueError: invalid literal for int() with base 10: 'adsf'


### example 2
- input validation


```python
while True:
    try:
        x = int(input("Please enter a integer: "))
        break
    except ValueError:
        print("Oops! That was not a valid number. Try again...")
```

    Please enter a number: adf
    Oops! That was not a valid number. Try again...
    Please enter a number: asdf
    Oops! That was not a valid number. Try again...
    Please enter a number: asdf
    Oops! That was not a valid number. Try again...
    Please enter a number: sdasf
    Oops! That was not a valid number. Try again...
    Please enter a number: 2434.3534
    Oops! That was not a valid number. Try again...
    Please enter a number: 3534



```python
x
```




    3534



## raising exceptions
- raise statement allows programer to throw their own exceptions
- Python provides several built-in exceptions
    - e.g.: NameError, ModuleNotFoundError, MemoryError, etc.
    - for details: https://docs.python.org/3/library/exceptions.html

### example 1


```python
raise NameError("MyException")
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-15-64e59e30969a> in <module>
    ----> 1 raise NameError("MyException")
    

    NameError: MyException



```python
# except and raise execption
try:
    raise NameError('My Exception')
except NameError:
    print('An exception flew by...')
    raise
```

    An exception flew by...



    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-16-06305128be25> in <module>
          1 # except and raise execption
          2 try:
    ----> 3     raise NameError('My Exception')
          4 except NameError:
          5     print('An exception flew by...')


    NameError: My Exception


## user-defined exceptions
- one can define their own exceptions and raise them as needed
- should typically derive from the Exception class, either directly or indirectly

### example 1


```python
class InputError(Exception):
    """
    Exception raised for errors in the input.
    
    Attributes:
    expression -- input expression in which the error occured
    message -- explaination of the error
    """
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
    
```


```python
help(InputError)
```


```python
def getInteger():
    x = input('Enter an integer number: ')
    if not x.isdigit():
        raise InputError(x, 'That is not an integer!')
    return int(x)
```


```python
x = getInteger()
print(x)
```

## catch user-defined exception


```python
try:
    x = getInteger() #may throw InputError
except InputError as ie:
    print('Exception:', ie)
    # can throw ie again
else:
    print('{}^2 = {}'.format(x, x**2))
```


```python

```
