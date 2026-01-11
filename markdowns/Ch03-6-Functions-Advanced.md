# Advanced Topics on Functions

<a href="https://colab.research.google.com/github/rambasnet/Python-Fundamentals/blob/master/notebooks/Ch03-6-Functions-Advanced.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

## Topics
- handle variable length arguments
- lambda expressions
- higher-order functions
- nested functions
- functions as returned values
- currying
- function decorators

## Variable length arguments
- when not sure how many arguments will be passed to a function (e.g., print())
- `*args` (non-keyworded variable length arguments)
- `*kwargs` (keyworded variable length arguments)
- e.g., built-in `print` function uses variable length arguments and keyworded arguments

### print(*object, sep=' ', end='\n', file=sys.stdout, flush=False)


```python
# variable length arguments demo
def someFunction(a, b, c, *varargs, **kwargs):
    print('a = ', a)
    print('b = ', b)
    print('c = ', c)
    print('*args = ', varargs)
    print('type of args = ', type(varargs))
    print('**kwargs = ', kwargs)
    print('type of kwargs = ', type(kwargs))
```


```python
# call someFunction with some arguments
someFunction(1, 'Apple', 4.5, 5, [2.5, 'b'], fname='Jake', num=1)
```

    a =  1
    b =  Apple
    c =  4.5
    *args =  (5, [2.5, 'b'])
    type of args =  <class 'tuple'>
    **kwargs =  {'fname': 'Jake', 'num': 1}
    type of kwargs =  <class 'dict'>


## Lambda Functions/Expressions
- anonymous functions (no name)
- typically used in conjunction with higher order functions such as: map(), reduce(), filter()
- Reference: http://www.secnetix.de/olli/Python/lambda_functions.hawk

### lambda function properties and usage
- single line simple functions
- no explicit return keyword is used
- always contains an expression that is implictly returned
- can use a lambda definition anywere a function is expected without assigning to a variable
- syntax: 
```python
    lambda argument(s): expression
```
- see Ch08-2 Lists Advanced chapter for lambda applications on some higher order built-in functions

### difference between lambda and regular function


```python
# regular function
def func(x): return x**2
```


```python
print(func(4))
```

    16



```python
type(func)
```




    function




```python
print(func)
```

    <function func at 0x7fe02aec0c10>



```python
g = lambda x: x**2 # no name, no parenthesis, and no return keyword
# a function that takes x and returns x**2
```


```python
type(g)
```




    function




```python
print(g)
```

    <function <lambda> at 0x7fe02aec0d30>



```python
g(4)
```




    16



## Higher-order functions
https://composingprograms.com/pages/16-higher-order-functions.html
- functions that manipulate other functions are called higher order functions
- functions take function(s) as argument(s)
    - typically, lambda expressions are passed as arguments
- functions can define and return a local function


```python
# computer summations of n natural numbers
# func is a function applied to all the natural numbers between 1 and n inclusive
def sum_naturals(func, n):
    total, k = 0, 1
    while k <= n:
        total += func(k)
        k += 1
    return total
    
```


```python
n = 100
```


```python
# pass lambda function
print(f'sum of first {n} natural numbers = {sum_naturals(lambda x: x, n)}')
```


```python
# of course you can pass regular function
def even(n):
    return n if n%2 == 0 else 0
```


```python
print(f'sum of even numbers from 1 to {n} = {sum_naturals(even, n)}')
```

    sum of even numbers from 1 to 100 = 2550



```python
# sum of odd numbers from 1 to 100
print(f'sum of odd numbers from 1 to {n} = {sum_naturals(lambda x: x if x%2==1 else 0, n)}')
```

    sum of odd numbers from 1 to 100 = 2500


## Nested functions
- functions can be defined inside a function with local scope
- locally defined functions also have access to the names defined in their parent function
    - this technique is called lexical scoping
- helps keep the global frame clean and less cluter with functions that are only used inside some functions
- let's redefine sum_natural function again with local functions

### Visualize using [PythonTutor.com](http://pythontutor.com/visualize.html#code=def%20sum_naturals1%28n,%20number_type%3D%22all%22%29%3A%0A%20%20%20%20def%20even%28x%29%3A%0A%20%20%20%20%20%20%20%20return%20x%20if%20x%252%20%3D%3D%200%20else%200%0A%20%20%20%20%0A%20%20%20%20def%20odd%28x%29%3A%0A%20%20%20%20%20%20%20%20return%20x%20if%20x%252%20%3D%3D%201%20else%200%0A%20%20%20%20%0A%20%20%20%20def%20func%28x%29%3A%0A%20%20%20%20%20%20%20%20%23%20local%20function%20has%20access%20to%20global%20variables%20as%20well%20as%20parent%20frames%0A%20%20%20%20%20%20%20%20if%20number_type%20%3D%3D%20'even'%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20x%20if%20x%252%20%3D%3D%200%20else%200%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20x%20if%20x%252%20%3D%3D%201%20else%200%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20total,%20k%20%3D%200,%201%0A%20%20%20%20while%20k%20%3C%3D%20n%3A%0A%20%20%20%20%20%20%20%20if%20number_type%20!%3D%20'all'%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20total%20%2B%3D%20func%28k%29%0A%20%20%20%20%20%20%20%20%23elif%20number_type%20%3D%3D%20'odd'%3A%0A%20%20%20%20%20%20%20%20%23%20%20%20%20total%20%2B%3D%20odd%28k%29%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20total%20%2B%3D%20k%0A%20%20%20%20%20%20%20%20k%20%2B%3D%201%0A%20%20%20%20return%20total%0A%20%20%20%20%0An%20%3D%2010%20%20%0Aprint%28f'sum%20of%20even%20numbers%20from%201%20to%20%7Bn%7D%20%3D%20%7Bsum_naturals1%28n,%20%22even%22%29%7D'%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
# compute summations of n natural numbers
# by default find sum of all the natural numbers between 1 and n inclusive
def sum_naturals1(n, number_type="all"):
    def even(x):
        return x if x%2 == 0 else 0
    
    def odd(x):
        return x if x%2 == 1 else 0
    
    def func(x):
        # local function has access to global variables as well as parent frames
        if number_type == 'even':
            return x if x%2 == 0 else 0
        else:
            return x if x%2 == 1 else 0
            
    total, k = 0, 1
    while k <= n:
        if number_type != 'all':
            total += func(k)
        #elif number_type == 'odd':
        #    total += odd(k)
        else:
            total += k
        k += 1
    return total
```


```python
n = 100
print(f'sum of first {n} natural numbers = {sum_naturals1(n)}')
```

    sum of first 100 natural numbers = 5050



```python
print(f'sum of even numbers from 1 to {n} = {sum_naturals1(n, "even")}')
```

    sum of even numbers from 1 to 100 = 2550



```python
# sum of odd numbers from 1 to 100
print(f'sum of odd numbers from 1 to {n} = {sum_naturals1(n, "odd")}')
```

    sum of odd numbers from 1 to 100 = 2500


## Functions as returned values
- functions can return a function
- locally defined functions maintain their parent environment when they are returned


```python
def number_type(ntype='all'):
    def even(x):
        return x if x%2 == 0 else 0
    
    def odd(x):
        return x if x%2 == 1 else 0
    
    def _(x): # function to return x as it is; any()
        return x
    
    if ntype == 'all':
        return _
    elif ntype == 'even':
        return even
    else:
        return odd
```


```python
n = 100
print(f'sum of first {n} natural numbers = {sum_naturals(number_type("all"), n)}')
```

    sum of first 100 natural numbers = 5050



```python
print(f'sum of even numbers from 1 to {n} = {sum_naturals(number_type("even"), n)}')
```

    sum of even numbers from 1 to 100 = 2550



```python
# sum of odd numbers from 1 to 100
print(f'sum of odd numbers from 1 to {n} = {sum_naturals(number_type("odd"), n)}')
```

    sum of odd numbers from 1 to 100 = 2500


## Currying

- breaking down the evaluation of a function that takes multiple arguments into evaluating a sequence of single-argument functions
- also used in chaining multiple functions into one

- e.g., given a function `f(x, y)`, we can define a function `g(x)(y)` equivalent to `f(x, y)`
    - `g` is a higher-order function that takes in a single argument `x` and returns another function that takes in a single argument `y`
- a single function can be broken into multiple functions by chaining the smaller functions
    - `f(x) = h(g(x))`
    - the output of inner function `g(x)` is an input for outer function `h()`
    - this transformation is called **currying**


```python
# single function that converts days to seconds
def daysToSeconds(days):
    return days * 24 * 60 * 60;
```


```python
# use the function
daysToSeconds(1)
```




    86400




```python
# currying application
# convert no. of days into seconds
def convertDaysToSeconds(f1, f2, f3):
    """Higer order function that takes 3 functions."""
    def f(x): 
        return f1(f2(f3(x)))
    return f 

def daysToHours(days): 
    """ Function converts days to hours."""
    return days * 24

def hoursToMinutes(hours): 
    """ Function converts hours to minutes."""
    return hours * 60

def minutesToSeconds(minutes): 
    """ Function converts minutes to seconds."""
    return  minutes * 60
```


```python
# create a single function curry
curry = convertDaysToSeconds(minutesToSeconds, hoursToMinutes, daysToHours)
```


```python
# how many seconds in 1 day?
curry(1)
```




    86400




```python
# currying application; function with two arguments
# built-in pow function takes two arguments; 
# let's convert it into a function that takes a single argument
def curried_pow(x):
    def g(y):
        return pow(x, y)
    return g # function preserves the local variables, x and y
```


```python
curried_pow(2)(3) # x=2, y=3; -> pow(2, 3)
# same as 2**3
```




    8




```python
# currying application 2
# let's create a list of integers and map each to a different value
nums = list(range(1, 11))
```


```python
nums
```




    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]




```python
# function maps each element in alist with func() transformation
def my_map(alist, func):
    for i in range(len(alist)):
        alist[i] = func(alist[i])
```


```python
my_map(nums, curried_pow(2))
```


```python
nums
```




    [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]



## Function Decorators
- https://realpython.com/primer-on-python-decorators/
- decorators are higher order functions
- decorators take another function as an argument and decorate it
    - argument function is decorated by extending its behavior without explictly modifying the function itself
    
    
**How about passing arguments to decorated function and its return values?**
1. if the function being decorated takes arguments, provide arguments to the wrapper function
    - wrapper function wraps the argument function
2. if the function being decorated returns a value, call it with `return` statement

**Real-world Applications**
- many frameworks such as Flask, Django provide lots of decorators
    - e.g. @login_required; @app.route("/route_name"), etc.
    - simply define the functions using the library provided decorators!
- Python `functools` library provides many higher order decorators:
https://docs.python.org/3/library/functools.html


```python
# a simple fruitless function without parameter
def hello():
    """Print Hello there!"""
    
    print("Hello there!")
```


```python
hello()
# too simple... let's decorate hello
```

    Hello there!



```python
# a simple decorator function to decorate hello
def hello_decorator(func):
    """Decorate func."""
    
    def wrapper_hello_decorator(*args, **kwargs):
        """Wrapper for hello function."""
        
        print("There's a stranger...")
        # code ...
        # call the actual function
        #func()
        func(*args, **kwargs)
        print("Have a great time!")
        # code ...
    return wrapper_hello_decorator
```


```python
# hello is decorated now, without modifying the original function
# just the behavior is modified by added extra print() before and after hello
hello_deco = hello_decorator(hello)
```


```python
hello_deco()
```

    There's a stranger...
    Hello there!
    Have a great time!



```python
hello()
```

    Hello there!



```python
# Python provides a better syntax, shortcut!
# use @decorter_function name and define the function that needs to be decorated
@hello_decorator
def say_hi():
    """print Hi there! with some decorations."""
    
    print("Hi there!")
```


```python
say_hi()
```

    There's a stranger...
    Hi there!
    Have a great time!



```python
# let's check the name name and docstring for say_hi
say_hi.__name__
```




    'wrapper_hello_decorator'




```python
say_hi.__doc__
```




    'Wrapper for hello function.'




```python
# decorated function lost its identify! 
# Let's preserve the identify of functions being decorated...
from functools import wraps

# a simple decorator function to decorate hello
def hello_better(func):
    """Decorate func."""
    
    @wraps(func)
    def wrapper_hello_better(*args, **kwargs):
        """Wrapper for hello_better function."""
        
        print("There's a stranger...")
        # code ...
        # call the actual function
        #func()
        func(*args, **kwargs)
        print("Have a great time!")
        # code ...
    return wrapper_hello_better

```


```python
# let's define a new function with hello_better decorator
@hello_better
def greet():
    """Print Good morning!"""
    
    print('Good morning!')

```


```python
greet()
```

    There's a stranger...
    Good morning!
    Have a great time!



```python
# let's check the identity of greet
greet.__name__
```




    'greet'




```python
greet.__doc__
```




    'Print Good morning!'




```python
# another function decorator example...
# a simple count down function
def countDown(from_number):
    """A simple recurisve countdown function."""
    
    if from_number <= 0:
        print('Blast off!')
    else:
        print(from_number)
        countDown(from_number-1)
```


```python
# Doesn't slow down the countdown!
countDown(10)
```

    10
    9
    8
    7
    6
    5
    4
    3
    2
    1
    Blast off!



```python
# let's slow the countDown by a second by wrapping it up with function decorator!
import time

# let's write a slow_down wrapper
def slow_down(func):
    """Sleep 1 second before calling the func."""
    
    @wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        """Wrapper function for func."""
        
        time.sleep(1) # sleep for a second
        return func(*args, **kwargs) # call and return the result from the func
    
    return wrapper_slow_down
```


```python
countDownSlow = slow_down(countDown)
```


```python
countDownSlow(10)
```

    10
    9
    8
    7
    6
    5
    4
    3
    2
    1
    Blast off!


- if it doesn't work in Jupyter Notebook, use the provided demo in [demos/count_down_wrapper.py](demos/count_down_wrapper.py)

## Python typing

https://docs.python.org/3/library/typing.html

- Since version 3.5, Python started supporting data type as *hints*
- Runtime doesn't enforce function and variable type annotations
- used by third party tools such as type checkers, IDEs, linters, etc.
- `typing` library has all the supported types
- Note: VS Code (v 1.49) type linting on Mac doesn't seem to be working 
- syntax:
```pthon
 var: type = value
```


```python
num: int = 10
```


```python
num
```




    10




```python
name: str = "James Bond"
```


```python
def greeting(name: str) -> str:
    return f'Hello, {name}!'
```


```python
greeting(name)
```




    'Hello, James Bond!'




```python
# typing module provides list of supported types
import typing
```


```python
help(typing)
# see DATA section towards the end of the document for all the supported types
```

    Help on module typing:
    
    NAME
        typing - The typing module: Support for gradual typing as defined by PEP 484.
    
    MODULE REFERENCE
        https://docs.python.org/3.8/library/typing
        
        The following documentation is automatically generated from the Python
        source files.  It may be incomplete, incorrect or include features that
        are considered implementation detail and may vary between Python
        implementations.  When in doubt, consult the module reference at the
        location listed above.
    
    DESCRIPTION
        At large scale, the structure of the module is following:
        * Imports and exports, all public names should be explicitly added to __all__.
        * Internal helper functions: these should never be used in code outside this module.
        * _SpecialForm and its instances (special forms): Any, NoReturn, ClassVar, Union, Optional
        * Two classes whose instances can be type arguments in addition to types: ForwardRef and TypeVar
        * The core of internal generics API: _GenericAlias and _VariadicGenericAlias, the latter is
          currently only used by Tuple and Callable. All subscripted types like X[int], Union[int, str],
          etc., are instances of either of these classes.
        * The public counterpart of the generics API consists of two classes: Generic and Protocol.
        * Public helper functions: get_type_hints, overload, cast, no_type_check,
          no_type_check_decorator.
        * Generic aliases for collections.abc ABCs and few additional protocols.
        * Special types: NewType, NamedTuple, TypedDict.
        * Wrapper submodules for re and io related types.
    
    CLASSES
        builtins.dict(builtins.object)
            TypedDict
        builtins.object
            builtins.str
            Generic
                Protocol
                    SupportsAbs
                    SupportsBytes
                    SupportsComplex
                    SupportsFloat
                    SupportsIndex
                    SupportsInt
                    SupportsRound
            NamedTuple
        _Final(builtins.object)
            ForwardRef
            TypeVar(_Final, _Immutable)
        _Immutable(builtins.object)
            TypeVar(_Final, _Immutable)
        
        class ForwardRef(_Final)
         |  ForwardRef(arg, is_argument=True)
         |  
         |  Internal wrapper to hold a forward reference.
         |  
         |  Method resolution order:
         |      ForwardRef
         |      _Final
         |      builtins.object
         |  
         |  Methods defined here:
         |  
         |  __eq__(self, other)
         |      Return self==value.
         |  
         |  __hash__(self)
         |      Return hash(self).
         |  
         |  __init__(self, arg, is_argument=True)
         |      Initialize self.  See help(type(self)) for accurate signature.
         |  
         |  __repr__(self)
         |      Return repr(self).
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  __forward_arg__
         |  
         |  __forward_code__
         |  
         |  __forward_evaluated__
         |  
         |  __forward_is_argument__
         |  
         |  __forward_value__
         |  
         |  ----------------------------------------------------------------------
         |  Class methods inherited from _Final:
         |  
         |  __init_subclass__(*args, **kwds) from builtins.type
         |      This method is called when a class is subclassed.
         |      
         |      The default implementation does nothing. It may be
         |      overridden to extend subclasses.
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors inherited from _Final:
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
        
        class Generic(builtins.object)
         |  Generic(*args, **kwds)
         |  
         |  Abstract base class for generic types.
         |  
         |  A generic type is typically declared by inheriting from
         |  this class parameterized with one or more type variables.
         |  For example, a generic mapping type might be defined as::
         |  
         |    class Mapping(Generic[KT, VT]):
         |        def __getitem__(self, key: KT) -> VT:
         |            ...
         |        # Etc.
         |  
         |  This class can then be used as follows::
         |  
         |    def lookup_name(mapping: Mapping[KT, VT], key: KT, default: VT) -> VT:
         |        try:
         |            return mapping[key]
         |        except KeyError:
         |            return default
         |  
         |  Class methods defined here:
         |  
         |  __class_getitem__(params) from builtins.type
         |  
         |  __init_subclass__(*args, **kwargs) from builtins.type
         |      This method is called when a class is subclassed.
         |      
         |      The default implementation does nothing. It may be
         |      overridden to extend subclasses.
         |  
         |  ----------------------------------------------------------------------
         |  Static methods defined here:
         |  
         |  __new__(cls, *args, **kwds)
         |      Create and return a new object.  See help(type) for accurate signature.
        
        class NamedTuple(builtins.object)
         |  NamedTuple(typename, fields=None, /, **kwargs)
         |  
         |  Typed version of namedtuple.
         |  
         |  Usage in Python versions >= 3.6::
         |  
         |      class Employee(NamedTuple):
         |          name: str
         |          id: int
         |  
         |  This is equivalent to::
         |  
         |      Employee = collections.namedtuple('Employee', ['name', 'id'])
         |  
         |  The resulting class has an extra __annotations__ attribute, giving a
         |  dict that maps field names to types.  (The field names are also in
         |  the _fields attribute, which is part of the namedtuple API.)
         |  Alternative equivalent keyword syntax is also accepted::
         |  
         |      Employee = NamedTuple('Employee', name=str, id=int)
         |  
         |  In Python versions <= 3.5 use::
         |  
         |      Employee = NamedTuple('Employee', [('name', str), ('id', int)])
         |  
         |  Static methods defined here:
         |  
         |  __new__(cls, typename, fields=None, /, **kwargs)
         |      Create and return a new object.  See help(type) for accurate signature.
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  __dict__
         |      dictionary for instance variables (if defined)
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
        
        class Protocol(Generic)
         |  Protocol(*args, **kwds)
         |  
         |  Base class for protocol classes.
         |  
         |  Protocol classes are defined as::
         |  
         |      class Proto(Protocol):
         |          def meth(self) -> int:
         |              ...
         |  
         |  Such classes are primarily used with static type checkers that recognize
         |  structural subtyping (static duck-typing), for example::
         |  
         |      class C:
         |          def meth(self) -> int:
         |              return 0
         |  
         |      def func(x: Proto) -> int:
         |          return x.meth()
         |  
         |      func(C())  # Passes static type check
         |  
         |  See PEP 544 for details. Protocol classes decorated with
         |  @typing.runtime_checkable act as simple-minded runtime protocols that check
         |  only the presence of given attributes, ignoring their type signatures.
         |  Protocol classes can be generic, they are defined as::
         |  
         |      class GenProto(Protocol[T]):
         |          def meth(self) -> T:
         |              ...
         |  
         |  Method resolution order:
         |      Protocol
         |      Generic
         |      builtins.object
         |  
         |  Class methods defined here:
         |  
         |  __init_subclass__(*args, **kwargs) from _ProtocolMeta
         |      This method is called when a class is subclassed.
         |      
         |      The default implementation does nothing. It may be
         |      overridden to extend subclasses.
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes defined here:
         |  
         |  __abstractmethods__ = frozenset()
         |  
         |  __parameters__ = ()
         |  
         |  ----------------------------------------------------------------------
         |  Class methods inherited from Generic:
         |  
         |  __class_getitem__(params) from _ProtocolMeta
         |  
         |  ----------------------------------------------------------------------
         |  Static methods inherited from Generic:
         |  
         |  __new__(cls, *args, **kwds)
         |      Create and return a new object.  See help(type) for accurate signature.
        
        class SupportsAbs(Protocol)
         |  SupportsAbs(*args, **kwds)
         |  
         |  An ABC with one abstract method __abs__ that is covariant in its return type.
         |  
         |  Method resolution order:
         |      SupportsAbs
         |      Protocol
         |      Generic
         |      builtins.object
         |  
         |  Methods defined here:
         |  
         |  __abs__(self) -> +T_co
         |  
         |  __init__ = _no_init(self, *args, **kwargs)
         |  
         |  __subclasshook__ = _proto_hook(other)
         |      # Set (or override) the protocol subclass hook.
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes defined here:
         |  
         |  __abstractmethods__ = frozenset({'__abs__'})
         |  
         |  __orig_bases__ = (typing.Protocol[+T_co],)
         |  
         |  __parameters__ = (+T_co,)
         |  
         |  ----------------------------------------------------------------------
         |  Class methods inherited from Protocol:
         |  
         |  __init_subclass__(*args, **kwargs) from _ProtocolMeta
         |      This method is called when a class is subclassed.
         |      
         |      The default implementation does nothing. It may be
         |      overridden to extend subclasses.
         |  
         |  ----------------------------------------------------------------------
         |  Class methods inherited from Generic:
         |  
         |  __class_getitem__(params) from _ProtocolMeta
         |  
         |  ----------------------------------------------------------------------
         |  Static methods inherited from Generic:
         |  
         |  __new__(cls, *args, **kwds)
         |      Create and return a new object.  See help(type) for accurate signature.
        
        class SupportsBytes(Protocol)
         |  SupportsBytes(*args, **kwds)
         |  
         |  An ABC with one abstract method __bytes__.
         |  
         |  Method resolution order:
         |      SupportsBytes
         |      Protocol
         |      Generic
         |      builtins.object
         |  
         |  Methods defined here:
         |  
         |  __bytes__(self) -> bytes
         |  
         |  __init__ = _no_init(self, *args, **kwargs)
         |  
         |  __subclasshook__ = _proto_hook(other)
         |      # Set (or override) the protocol subclass hook.
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes defined here:
         |  
         |  __abstractmethods__ = frozenset({'__bytes__'})
         |  
         |  __parameters__ = ()
         |  
         |  ----------------------------------------------------------------------
         |  Class methods inherited from Protocol:
         |  
         |  __init_subclass__(*args, **kwargs) from _ProtocolMeta
         |      This method is called when a class is subclassed.
         |      
         |      The default implementation does nothing. It may be
         |      overridden to extend subclasses.
         |  
         |  ----------------------------------------------------------------------
         |  Class methods inherited from Generic:
         |  
         |  __class_getitem__(params) from _ProtocolMeta
         |  
         |  ----------------------------------------------------------------------
         |  Static methods inherited from Generic:
         |  
         |  __new__(cls, *args, **kwds)
         |      Create and return a new object.  See help(type) for accurate signature.
        
        class SupportsComplex(Protocol)
         |  SupportsComplex(*args, **kwds)
         |  
         |  An ABC with one abstract method __complex__.
         |  
         |  Method resolution order:
         |      SupportsComplex
         |      Protocol
         |      Generic
         |      builtins.object
         |  
         |  Methods defined here:
         |  
         |  __complex__(self) -> complex
         |  
         |  __init__ = _no_init(self, *args, **kwargs)
         |  
         |  __subclasshook__ = _proto_hook(other)
         |      # Set (or override) the protocol subclass hook.
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes defined here:
         |  
         |  __abstractmethods__ = frozenset({'__complex__'})
         |  
         |  __parameters__ = ()
         |  
         |  ----------------------------------------------------------------------
         |  Class methods inherited from Protocol:
         |  
         |  __init_subclass__(*args, **kwargs) from _ProtocolMeta
         |      This method is called when a class is subclassed.
         |      
         |      The default implementation does nothing. It may be
         |      overridden to extend subclasses.
         |  
         |  ----------------------------------------------------------------------
         |  Class methods inherited from Generic:
         |  
         |  __class_getitem__(params) from _ProtocolMeta
         |  
         |  ----------------------------------------------------------------------
         |  Static methods inherited from Generic:
         |  
         |  __new__(cls, *args, **kwds)
         |      Create and return a new object.  See help(type) for accurate signature.
        
        class SupportsFloat(Protocol)
         |  SupportsFloat(*args, **kwds)
         |  
         |  An ABC with one abstract method __float__.
         |  
         |  Method resolution order:
         |      SupportsFloat
         |      Protocol
         |      Generic
         |      builtins.object
         |  
         |  Methods defined here:
         |  
         |  __float__(self) -> float
         |  
         |  __init__ = _no_init(self, *args, **kwargs)
         |  
         |  __subclasshook__ = _proto_hook(other)
         |      # Set (or override) the protocol subclass hook.
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes defined here:
         |  
         |  __abstractmethods__ = frozenset({'__float__'})
         |  
         |  __parameters__ = ()
         |  
         |  ----------------------------------------------------------------------
         |  Class methods inherited from Protocol:
         |  
         |  __init_subclass__(*args, **kwargs) from _ProtocolMeta
         |      This method is called when a class is subclassed.
         |      
         |      The default implementation does nothing. It may be
         |      overridden to extend subclasses.
         |  
         |  ----------------------------------------------------------------------
         |  Class methods inherited from Generic:
         |  
         |  __class_getitem__(params) from _ProtocolMeta
         |  
         |  ----------------------------------------------------------------------
         |  Static methods inherited from Generic:
         |  
         |  __new__(cls, *args, **kwds)
         |      Create and return a new object.  See help(type) for accurate signature.
        
        class SupportsIndex(Protocol)
         |  SupportsIndex(*args, **kwds)
         |  
         |  An ABC with one abstract method __index__.
         |  
         |  Method resolution order:
         |      SupportsIndex
         |      Protocol
         |      Generic
         |      builtins.object
         |  
         |  Methods defined here:
         |  
         |  __index__(self) -> int
         |  
         |  __init__ = _no_init(self, *args, **kwargs)
         |  
         |  __subclasshook__ = _proto_hook(other)
         |      # Set (or override) the protocol subclass hook.
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes defined here:
         |  
         |  __abstractmethods__ = frozenset({'__index__'})
         |  
         |  __parameters__ = ()
         |  
         |  ----------------------------------------------------------------------
         |  Class methods inherited from Protocol:
         |  
         |  __init_subclass__(*args, **kwargs) from _ProtocolMeta
         |      This method is called when a class is subclassed.
         |      
         |      The default implementation does nothing. It may be
         |      overridden to extend subclasses.
         |  
         |  ----------------------------------------------------------------------
         |  Class methods inherited from Generic:
         |  
         |  __class_getitem__(params) from _ProtocolMeta
         |  
         |  ----------------------------------------------------------------------
         |  Static methods inherited from Generic:
         |  
         |  __new__(cls, *args, **kwds)
         |      Create and return a new object.  See help(type) for accurate signature.
        
        class SupportsInt(Protocol)
         |  SupportsInt(*args, **kwds)
         |  
         |  An ABC with one abstract method __int__.
         |  
         |  Method resolution order:
         |      SupportsInt
         |      Protocol
         |      Generic
         |      builtins.object
         |  
         |  Methods defined here:
         |  
         |  __init__ = _no_init(self, *args, **kwargs)
         |  
         |  __int__(self) -> int
         |  
         |  __subclasshook__ = _proto_hook(other)
         |      # Set (or override) the protocol subclass hook.
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes defined here:
         |  
         |  __abstractmethods__ = frozenset({'__int__'})
         |  
         |  __parameters__ = ()
         |  
         |  ----------------------------------------------------------------------
         |  Class methods inherited from Protocol:
         |  
         |  __init_subclass__(*args, **kwargs) from _ProtocolMeta
         |      This method is called when a class is subclassed.
         |      
         |      The default implementation does nothing. It may be
         |      overridden to extend subclasses.
         |  
         |  ----------------------------------------------------------------------
         |  Class methods inherited from Generic:
         |  
         |  __class_getitem__(params) from _ProtocolMeta
         |  
         |  ----------------------------------------------------------------------
         |  Static methods inherited from Generic:
         |  
         |  __new__(cls, *args, **kwds)
         |      Create and return a new object.  See help(type) for accurate signature.
        
        class SupportsRound(Protocol)
         |  SupportsRound(*args, **kwds)
         |  
         |  An ABC with one abstract method __round__ that is covariant in its return type.
         |  
         |  Method resolution order:
         |      SupportsRound
         |      Protocol
         |      Generic
         |      builtins.object
         |  
         |  Methods defined here:
         |  
         |  __init__ = _no_init(self, *args, **kwargs)
         |  
         |  __round__(self, ndigits: int = 0) -> +T_co
         |  
         |  __subclasshook__ = _proto_hook(other)
         |      # Set (or override) the protocol subclass hook.
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes defined here:
         |  
         |  __abstractmethods__ = frozenset({'__round__'})
         |  
         |  __orig_bases__ = (typing.Protocol[+T_co],)
         |  
         |  __parameters__ = (+T_co,)
         |  
         |  ----------------------------------------------------------------------
         |  Class methods inherited from Protocol:
         |  
         |  __init_subclass__(*args, **kwargs) from _ProtocolMeta
         |      This method is called when a class is subclassed.
         |      
         |      The default implementation does nothing. It may be
         |      overridden to extend subclasses.
         |  
         |  ----------------------------------------------------------------------
         |  Class methods inherited from Generic:
         |  
         |  __class_getitem__(params) from _ProtocolMeta
         |  
         |  ----------------------------------------------------------------------
         |  Static methods inherited from Generic:
         |  
         |  __new__(cls, *args, **kwds)
         |      Create and return a new object.  See help(type) for accurate signature.
        
        Text = class str(object)
         |  str(object='') -> str
         |  str(bytes_or_buffer[, encoding[, errors]]) -> str
         |  
         |  Create a new string object from the given object. If encoding or
         |  errors is specified, then the object must expose a data buffer
         |  that will be decoded using the given encoding and error handler.
         |  Otherwise, returns the result of object.__str__() (if defined)
         |  or repr(object).
         |  encoding defaults to sys.getdefaultencoding().
         |  errors defaults to 'strict'.
         |  
         |  Methods defined here:
         |  
         |  __add__(self, value, /)
         |      Return self+value.
         |  
         |  __contains__(self, key, /)
         |      Return key in self.
         |  
         |  __eq__(self, value, /)
         |      Return self==value.
         |  
         |  __format__(self, format_spec, /)
         |      Return a formatted version of the string as described by format_spec.
         |  
         |  __ge__(self, value, /)
         |      Return self>=value.
         |  
         |  __getattribute__(self, name, /)
         |      Return getattr(self, name).
         |  
         |  __getitem__(self, key, /)
         |      Return self[key].
         |  
         |  __getnewargs__(...)
         |  
         |  __gt__(self, value, /)
         |      Return self>value.
         |  
         |  __hash__(self, /)
         |      Return hash(self).
         |  
         |  __iter__(self, /)
         |      Implement iter(self).
         |  
         |  __le__(self, value, /)
         |      Return self<=value.
         |  
         |  __len__(self, /)
         |      Return len(self).
         |  
         |  __lt__(self, value, /)
         |      Return self<value.
         |  
         |  __mod__(self, value, /)
         |      Return self%value.
         |  
         |  __mul__(self, value, /)
         |      Return self*value.
         |  
         |  __ne__(self, value, /)
         |      Return self!=value.
         |  
         |  __repr__(self, /)
         |      Return repr(self).
         |  
         |  __rmod__(self, value, /)
         |      Return value%self.
         |  
         |  __rmul__(self, value, /)
         |      Return value*self.
         |  
         |  __sizeof__(self, /)
         |      Return the size of the string in memory, in bytes.
         |  
         |  __str__(self, /)
         |      Return str(self).
         |  
         |  capitalize(self, /)
         |      Return a capitalized version of the string.
         |      
         |      More specifically, make the first character have upper case and the rest lower
         |      case.
         |  
         |  casefold(self, /)
         |      Return a version of the string suitable for caseless comparisons.
         |  
         |  center(self, width, fillchar=' ', /)
         |      Return a centered string of length width.
         |      
         |      Padding is done using the specified fill character (default is a space).
         |  
         |  count(...)
         |      S.count(sub[, start[, end]]) -> int
         |      
         |      Return the number of non-overlapping occurrences of substring sub in
         |      string S[start:end].  Optional arguments start and end are
         |      interpreted as in slice notation.
         |  
         |  encode(self, /, encoding='utf-8', errors='strict')
         |      Encode the string using the codec registered for encoding.
         |      
         |      encoding
         |        The encoding in which to encode the string.
         |      errors
         |        The error handling scheme to use for encoding errors.
         |        The default is 'strict' meaning that encoding errors raise a
         |        UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
         |        'xmlcharrefreplace' as well as any other name registered with
         |        codecs.register_error that can handle UnicodeEncodeErrors.
         |  
         |  endswith(...)
         |      S.endswith(suffix[, start[, end]]) -> bool
         |      
         |      Return True if S ends with the specified suffix, False otherwise.
         |      With optional start, test S beginning at that position.
         |      With optional end, stop comparing S at that position.
         |      suffix can also be a tuple of strings to try.
         |  
         |  expandtabs(self, /, tabsize=8)
         |      Return a copy where all tab characters are expanded using spaces.
         |      
         |      If tabsize is not given, a tab size of 8 characters is assumed.
         |  
         |  find(...)
         |      S.find(sub[, start[, end]]) -> int
         |      
         |      Return the lowest index in S where substring sub is found,
         |      such that sub is contained within S[start:end].  Optional
         |      arguments start and end are interpreted as in slice notation.
         |      
         |      Return -1 on failure.
         |  
         |  format(...)
         |      S.format(*args, **kwargs) -> str
         |      
         |      Return a formatted version of S, using substitutions from args and kwargs.
         |      The substitutions are identified by braces ('{' and '}').
         |  
         |  format_map(...)
         |      S.format_map(mapping) -> str
         |      
         |      Return a formatted version of S, using substitutions from mapping.
         |      The substitutions are identified by braces ('{' and '}').
         |  
         |  index(...)
         |      S.index(sub[, start[, end]]) -> int
         |      
         |      Return the lowest index in S where substring sub is found,
         |      such that sub is contained within S[start:end].  Optional
         |      arguments start and end are interpreted as in slice notation.
         |      
         |      Raises ValueError when the substring is not found.
         |  
         |  isalnum(self, /)
         |      Return True if the string is an alpha-numeric string, False otherwise.
         |      
         |      A string is alpha-numeric if all characters in the string are alpha-numeric and
         |      there is at least one character in the string.
         |  
         |  isalpha(self, /)
         |      Return True if the string is an alphabetic string, False otherwise.
         |      
         |      A string is alphabetic if all characters in the string are alphabetic and there
         |      is at least one character in the string.
         |  
         |  isascii(self, /)
         |      Return True if all characters in the string are ASCII, False otherwise.
         |      
         |      ASCII characters have code points in the range U+0000-U+007F.
         |      Empty string is ASCII too.
         |  
         |  isdecimal(self, /)
         |      Return True if the string is a decimal string, False otherwise.
         |      
         |      A string is a decimal string if all characters in the string are decimal and
         |      there is at least one character in the string.
         |  
         |  isdigit(self, /)
         |      Return True if the string is a digit string, False otherwise.
         |      
         |      A string is a digit string if all characters in the string are digits and there
         |      is at least one character in the string.
         |  
         |  isidentifier(self, /)
         |      Return True if the string is a valid Python identifier, False otherwise.
         |      
         |      Call keyword.iskeyword(s) to test whether string s is a reserved identifier,
         |      such as "def" or "class".
         |  
         |  islower(self, /)
         |      Return True if the string is a lowercase string, False otherwise.
         |      
         |      A string is lowercase if all cased characters in the string are lowercase and
         |      there is at least one cased character in the string.
         |  
         |  isnumeric(self, /)
         |      Return True if the string is a numeric string, False otherwise.
         |      
         |      A string is numeric if all characters in the string are numeric and there is at
         |      least one character in the string.
         |  
         |  isprintable(self, /)
         |      Return True if the string is printable, False otherwise.
         |      
         |      A string is printable if all of its characters are considered printable in
         |      repr() or if it is empty.
         |  
         |  isspace(self, /)
         |      Return True if the string is a whitespace string, False otherwise.
         |      
         |      A string is whitespace if all characters in the string are whitespace and there
         |      is at least one character in the string.
         |  
         |  istitle(self, /)
         |      Return True if the string is a title-cased string, False otherwise.
         |      
         |      In a title-cased string, upper- and title-case characters may only
         |      follow uncased characters and lowercase characters only cased ones.
         |  
         |  isupper(self, /)
         |      Return True if the string is an uppercase string, False otherwise.
         |      
         |      A string is uppercase if all cased characters in the string are uppercase and
         |      there is at least one cased character in the string.
         |  
         |  join(self, iterable, /)
         |      Concatenate any number of strings.
         |      
         |      The string whose method is called is inserted in between each given string.
         |      The result is returned as a new string.
         |      
         |      Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
         |  
         |  ljust(self, width, fillchar=' ', /)
         |      Return a left-justified string of length width.
         |      
         |      Padding is done using the specified fill character (default is a space).
         |  
         |  lower(self, /)
         |      Return a copy of the string converted to lowercase.
         |  
         |  lstrip(self, chars=None, /)
         |      Return a copy of the string with leading whitespace removed.
         |      
         |      If chars is given and not None, remove characters in chars instead.
         |  
         |  partition(self, sep, /)
         |      Partition the string into three parts using the given separator.
         |      
         |      This will search for the separator in the string.  If the separator is found,
         |      returns a 3-tuple containing the part before the separator, the separator
         |      itself, and the part after it.
         |      
         |      If the separator is not found, returns a 3-tuple containing the original string
         |      and two empty strings.
         |  
         |  replace(self, old, new, count=-1, /)
         |      Return a copy with all occurrences of substring old replaced by new.
         |      
         |        count
         |          Maximum number of occurrences to replace.
         |          -1 (the default value) means replace all occurrences.
         |      
         |      If the optional argument count is given, only the first count occurrences are
         |      replaced.
         |  
         |  rfind(...)
         |      S.rfind(sub[, start[, end]]) -> int
         |      
         |      Return the highest index in S where substring sub is found,
         |      such that sub is contained within S[start:end].  Optional
         |      arguments start and end are interpreted as in slice notation.
         |      
         |      Return -1 on failure.
         |  
         |  rindex(...)
         |      S.rindex(sub[, start[, end]]) -> int
         |      
         |      Return the highest index in S where substring sub is found,
         |      such that sub is contained within S[start:end].  Optional
         |      arguments start and end are interpreted as in slice notation.
         |      
         |      Raises ValueError when the substring is not found.
         |  
         |  rjust(self, width, fillchar=' ', /)
         |      Return a right-justified string of length width.
         |      
         |      Padding is done using the specified fill character (default is a space).
         |  
         |  rpartition(self, sep, /)
         |      Partition the string into three parts using the given separator.
         |      
         |      This will search for the separator in the string, starting at the end. If
         |      the separator is found, returns a 3-tuple containing the part before the
         |      separator, the separator itself, and the part after it.
         |      
         |      If the separator is not found, returns a 3-tuple containing two empty strings
         |      and the original string.
         |  
         |  rsplit(self, /, sep=None, maxsplit=-1)
         |      Return a list of the words in the string, using sep as the delimiter string.
         |      
         |        sep
         |          The delimiter according which to split the string.
         |          None (the default value) means split according to any whitespace,
         |          and discard empty strings from the result.
         |        maxsplit
         |          Maximum number of splits to do.
         |          -1 (the default value) means no limit.
         |      
         |      Splits are done starting at the end of the string and working to the front.
         |  
         |  rstrip(self, chars=None, /)
         |      Return a copy of the string with trailing whitespace removed.
         |      
         |      If chars is given and not None, remove characters in chars instead.
         |  
         |  split(self, /, sep=None, maxsplit=-1)
         |      Return a list of the words in the string, using sep as the delimiter string.
         |      
         |      sep
         |        The delimiter according which to split the string.
         |        None (the default value) means split according to any whitespace,
         |        and discard empty strings from the result.
         |      maxsplit
         |        Maximum number of splits to do.
         |        -1 (the default value) means no limit.
         |  
         |  splitlines(self, /, keepends=False)
         |      Return a list of the lines in the string, breaking at line boundaries.
         |      
         |      Line breaks are not included in the resulting list unless keepends is given and
         |      true.
         |  
         |  startswith(...)
         |      S.startswith(prefix[, start[, end]]) -> bool
         |      
         |      Return True if S starts with the specified prefix, False otherwise.
         |      With optional start, test S beginning at that position.
         |      With optional end, stop comparing S at that position.
         |      prefix can also be a tuple of strings to try.
         |  
         |  strip(self, chars=None, /)
         |      Return a copy of the string with leading and trailing whitespace removed.
         |      
         |      If chars is given and not None, remove characters in chars instead.
         |  
         |  swapcase(self, /)
         |      Convert uppercase characters to lowercase and lowercase characters to uppercase.
         |  
         |  title(self, /)
         |      Return a version of the string where each word is titlecased.
         |      
         |      More specifically, words start with uppercased characters and all remaining
         |      cased characters have lower case.
         |  
         |  translate(self, table, /)
         |      Replace each character in the string using the given translation table.
         |      
         |        table
         |          Translation table, which must be a mapping of Unicode ordinals to
         |          Unicode ordinals, strings, or None.
         |      
         |      The table must implement lookup/indexing via __getitem__, for instance a
         |      dictionary or list.  If this operation raises LookupError, the character is
         |      left untouched.  Characters mapped to None are deleted.
         |  
         |  upper(self, /)
         |      Return a copy of the string converted to uppercase.
         |  
         |  zfill(self, width, /)
         |      Pad a numeric string with zeros on the left, to fill a field of the given width.
         |      
         |      The string is never truncated.
         |  
         |  ----------------------------------------------------------------------
         |  Static methods defined here:
         |  
         |  __new__(*args, **kwargs) from builtins.type
         |      Create and return a new object.  See help(type) for accurate signature.
         |  
         |  maketrans(...)
         |      Return a translation table usable for str.translate().
         |      
         |      If there is only one argument, it must be a dictionary mapping Unicode
         |      ordinals (integers) or characters to Unicode ordinals, strings or None.
         |      Character keys will be then converted to ordinals.
         |      If there are two arguments, they must be strings of equal length, and
         |      in the resulting dictionary, each character in x will be mapped to the
         |      character at the same position in y. If there is a third argument, it
         |      must be a string, whose characters will be mapped to None in the result.
        
        class TypeVar(_Final, _Immutable)
         |  TypeVar(name, *constraints, bound=None, covariant=False, contravariant=False)
         |  
         |  Type variable.
         |  
         |  Usage::
         |  
         |    T = TypeVar('T')  # Can be anything
         |    A = TypeVar('A', str, bytes)  # Must be str or bytes
         |  
         |  Type variables exist primarily for the benefit of static type
         |  checkers.  They serve as the parameters for generic types as well
         |  as for generic function definitions.  See class Generic for more
         |  information on generic types.  Generic functions work as follows:
         |  
         |    def repeat(x: T, n: int) -> List[T]:
         |        '''Return a list containing n references to x.'''
         |        return [x]*n
         |  
         |    def longest(x: A, y: A) -> A:
         |        '''Return the longest of two strings.'''
         |        return x if len(x) >= len(y) else y
         |  
         |  The latter example's signature is essentially the overloading
         |  of (str, str) -> str and (bytes, bytes) -> bytes.  Also note
         |  that if the arguments are instances of some subclass of str,
         |  the return type is still plain str.
         |  
         |  At runtime, isinstance(x, T) and issubclass(C, T) will raise TypeError.
         |  
         |  Type variables defined with covariant=True or contravariant=True
         |  can be used to declare covariant or contravariant generic types.
         |  See PEP 484 for more details. By default generic types are invariant
         |  in all type variables.
         |  
         |  Type variables can be introspected. e.g.:
         |  
         |    T.__name__ == 'T'
         |    T.__constraints__ == ()
         |    T.__covariant__ == False
         |    T.__contravariant__ = False
         |    A.__constraints__ == (str, bytes)
         |  
         |  Note that only type variables defined in global scope can be pickled.
         |  
         |  Method resolution order:
         |      TypeVar
         |      _Final
         |      _Immutable
         |      builtins.object
         |  
         |  Methods defined here:
         |  
         |  __init__(self, name, *constraints, bound=None, covariant=False, contravariant=False)
         |      Initialize self.  See help(type(self)) for accurate signature.
         |  
         |  __reduce__(self)
         |      Helper for pickle.
         |  
         |  __repr__(self)
         |      Return repr(self).
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  __bound__
         |  
         |  __constraints__
         |  
         |  __contravariant__
         |  
         |  __covariant__
         |  
         |  __dict__
         |      dictionary for instance variables (if defined)
         |  
         |  ----------------------------------------------------------------------
         |  Class methods inherited from _Final:
         |  
         |  __init_subclass__(*args, **kwds) from builtins.type
         |      This method is called when a class is subclassed.
         |      
         |      The default implementation does nothing. It may be
         |      overridden to extend subclasses.
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors inherited from _Final:
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from _Immutable:
         |  
         |  __copy__(self)
         |  
         |  __deepcopy__(self, memo)
        
        class TypedDict(builtins.dict)
         |  TypedDict(typename, fields=None, /, *, total=True, **kwargs)
         |  
         |  A simple typed namespace. At runtime it is equivalent to a plain dict.
         |  
         |  TypedDict creates a dictionary type that expects all of its
         |  instances to have a certain set of keys, where each key is
         |  associated with a value of a consistent type. This expectation
         |  is not checked at runtime but is only enforced by type checkers.
         |  Usage::
         |  
         |      class Point2D(TypedDict):
         |          x: int
         |          y: int
         |          label: str
         |  
         |      a: Point2D = {'x': 1, 'y': 2, 'label': 'good'}  # OK
         |      b: Point2D = {'z': 3, 'label': 'bad'}           # Fails type check
         |  
         |      assert Point2D(x=1, y=2, label='first') == dict(x=1, y=2, label='first')
         |  
         |  The type info can be accessed via Point2D.__annotations__. TypedDict
         |  supports two additional equivalent forms::
         |  
         |      Point2D = TypedDict('Point2D', x=int, y=int, label=str)
         |      Point2D = TypedDict('Point2D', {'x': int, 'y': int, 'label': str})
         |  
         |  By default, all keys must be present in a TypedDict. It is possible
         |  to override this by specifying totality.
         |  Usage::
         |  
         |      class point2D(TypedDict, total=False):
         |          x: int
         |          y: int
         |  
         |  This means that a point2D TypedDict can have any of the keys omitted.A type
         |  checker is only expected to support a literal False or True as the value of
         |  the total argument. True is the default, and makes all items defined in the
         |  class body be required.
         |  
         |  The class syntax is only supported in Python 3.6+, while two other
         |  syntax forms work for Python 2.7 and 3.2+
         |  
         |  Method resolution order:
         |      TypedDict
         |      builtins.dict
         |      builtins.object
         |  
         |  Static methods defined here:
         |  
         |  __new__ = _typeddict_new(cls, typename, fields=None, /, *, total=True, **kwargs)
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  __dict__
         |      dictionary for instance variables (if defined)
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes defined here:
         |  
         |  __annotations__ = {}
         |  
         |  __total__ = True
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from builtins.dict:
         |  
         |  __contains__(self, key, /)
         |      True if the dictionary has the specified key, else False.
         |  
         |  __delitem__(self, key, /)
         |      Delete self[key].
         |  
         |  __eq__(self, value, /)
         |      Return self==value.
         |  
         |  __ge__(self, value, /)
         |      Return self>=value.
         |  
         |  __getattribute__(self, name, /)
         |      Return getattr(self, name).
         |  
         |  __getitem__(...)
         |      x.__getitem__(y) <==> x[y]
         |  
         |  __gt__(self, value, /)
         |      Return self>value.
         |  
         |  __init__(self, /, *args, **kwargs)
         |      Initialize self.  See help(type(self)) for accurate signature.
         |  
         |  __iter__(self, /)
         |      Implement iter(self).
         |  
         |  __le__(self, value, /)
         |      Return self<=value.
         |  
         |  __len__(self, /)
         |      Return len(self).
         |  
         |  __lt__(self, value, /)
         |      Return self<value.
         |  
         |  __ne__(self, value, /)
         |      Return self!=value.
         |  
         |  __repr__(self, /)
         |      Return repr(self).
         |  
         |  __reversed__(self, /)
         |      Return a reverse iterator over the dict keys.
         |  
         |  __setitem__(self, key, value, /)
         |      Set self[key] to value.
         |  
         |  __sizeof__(...)
         |      D.__sizeof__() -> size of D in memory, in bytes
         |  
         |  clear(...)
         |      D.clear() -> None.  Remove all items from D.
         |  
         |  copy(...)
         |      D.copy() -> a shallow copy of D
         |  
         |  get(self, key, default=None, /)
         |      Return the value for key if key is in the dictionary, else default.
         |  
         |  items(...)
         |      D.items() -> a set-like object providing a view on D's items
         |  
         |  keys(...)
         |      D.keys() -> a set-like object providing a view on D's keys
         |  
         |  pop(...)
         |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
         |      If key is not found, d is returned if given, otherwise KeyError is raised
         |  
         |  popitem(self, /)
         |      Remove and return a (key, value) pair as a 2-tuple.
         |      
         |      Pairs are returned in LIFO (last-in, first-out) order.
         |      Raises KeyError if the dict is empty.
         |  
         |  setdefault(self, key, default=None, /)
         |      Insert key with a value of default if key is not in the dictionary.
         |      
         |      Return the value for key if key is in the dictionary, else default.
         |  
         |  update(...)
         |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
         |      If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
         |      If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
         |      In either case, this is followed by: for k in F:  D[k] = F[k]
         |  
         |  values(...)
         |      D.values() -> an object providing a view on D's values
         |  
         |  ----------------------------------------------------------------------
         |  Class methods inherited from builtins.dict:
         |  
         |  fromkeys(iterable, value=None, /) from _TypedDictMeta
         |      Create a new dictionary with keys from iterable and values set to value.
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes inherited from builtins.dict:
         |  
         |  __hash__ = None
    
    FUNCTIONS
        NewType(name, tp)
            NewType creates simple unique types with almost zero
            runtime overhead. NewType(name, tp) is considered a subtype of tp
            by static type checkers. At runtime, NewType(name, tp) returns
            a dummy function that simply returns its argument. Usage::
            
                UserId = NewType('UserId', int)
            
                def name_by_id(user_id: UserId) -> str:
                    ...
            
                UserId('user')          # Fails type check
            
                name_by_id(42)          # Fails type check
                name_by_id(UserId(42))  # OK
            
                num = UserId(5) + 1     # type: int
        
        cast(typ, val)
            Cast a value to a type.
            
            This returns the value unchanged.  To the type checker this
            signals that the return value has the designated type, but at
            runtime we intentionally don't check anything (we want this
            to be as fast as possible).
        
        final(f)
            A decorator to indicate final methods and final classes.
            
            Use this decorator to indicate to type checkers that the decorated
            method cannot be overridden, and decorated class cannot be subclassed.
            For example:
            
              class Base:
                  @final
                  def done(self) -> None:
                      ...
              class Sub(Base):
                  def done(self) -> None:  # Error reported by type checker
                        ...
            
              @final
              class Leaf:
                  ...
              class Other(Leaf):  # Error reported by type checker
                  ...
            
            There is no runtime checking of these properties.
        
        get_args(tp)
            Get type arguments with all substitutions performed.
            
            For unions, basic simplifications used by Union constructor are performed.
            Examples::
                get_args(Dict[str, int]) == (str, int)
                get_args(int) == ()
                get_args(Union[int, Union[T, int], str][int]) == (int, str)
                get_args(Union[int, Tuple[T, int]][str]) == (int, Tuple[str, int])
                get_args(Callable[[], T][int]) == ([], int)
        
        get_origin(tp)
            Get the unsubscripted version of a type.
            
            This supports generic types, Callable, Tuple, Union, Literal, Final and ClassVar.
            Return None for unsupported types. Examples::
            
                get_origin(Literal[42]) is Literal
                get_origin(int) is None
                get_origin(ClassVar[int]) is ClassVar
                get_origin(Generic) is Generic
                get_origin(Generic[T]) is Generic
                get_origin(Union[T, int]) is Union
                get_origin(List[Tuple[T, T]][int]) == list
        
        get_type_hints(obj, globalns=None, localns=None)
            Return type hints for an object.
            
            This is often the same as obj.__annotations__, but it handles
            forward references encoded as string literals, and if necessary
            adds Optional[t] if a default value equal to None is set.
            
            The argument may be a module, class, method, or function. The annotations
            are returned as a dictionary. For classes, annotations include also
            inherited members.
            
            TypeError is raised if the argument is not of a type that can contain
            annotations, and an empty dictionary is returned if no annotations are
            present.
            
            BEWARE -- the behavior of globalns and localns is counterintuitive
            (unless you are familiar with how eval() and exec() work).  The
            search order is locals first, then globals.
            
            - If no dict arguments are passed, an attempt is made to use the
              globals from obj (or the respective module's globals for classes),
              and these are also used as the locals.  If the object does not appear
              to have globals, an empty dictionary is used.
            
            - If one dict argument is passed, it is used for both globals and
              locals.
            
            - If two dict arguments are passed, they specify globals and
              locals, respectively.
        
        no_type_check(arg)
            Decorator to indicate that annotations are not type hints.
            
            The argument must be a class or function; if it is a class, it
            applies recursively to all methods and classes defined in that class
            (but not to methods defined in its superclasses or subclasses).
            
            This mutates the function(s) or class(es) in place.
        
        no_type_check_decorator(decorator)
            Decorator to give another decorator the @no_type_check effect.
            
            This wraps the decorator with something that wraps the decorated
            function in @no_type_check.
        
        overload(func)
            Decorator for overloaded functions/methods.
            
            In a stub file, place two or more stub definitions for the same
            function in a row, each decorated with @overload.  For example:
            
              @overload
              def utf8(value: None) -> None: ...
              @overload
              def utf8(value: bytes) -> bytes: ...
              @overload
              def utf8(value: str) -> bytes: ...
            
            In a non-stub file (i.e. a regular .py file), do the same but
            follow it with an implementation.  The implementation should *not*
            be decorated with @overload.  For example:
            
              @overload
              def utf8(value: None) -> None: ...
              @overload
              def utf8(value: bytes) -> bytes: ...
              @overload
              def utf8(value: str) -> bytes: ...
              def utf8(value):
                  # implementation goes here
        
        runtime_checkable(cls)
            Mark a protocol class as a runtime protocol.
            
            Such protocol can be used with isinstance() and issubclass().
            Raise TypeError if applied to a non-protocol class.
            This allows a simple-minded structural check very similar to
            one trick ponies in collections.abc such as Iterable.
            For example::
            
                @runtime_checkable
                class Closable(Protocol):
                    def close(self): ...
            
                assert isinstance(open('/some/file'), Closable)
            
            Warning: this will check only the presence of the required methods,
            not their type signatures!
    
    DATA
        AbstractSet = typing.AbstractSet
        Any = typing.Any
        AnyStr = ~AnyStr
        AsyncContextManager = typing.AbstractAsyncContextManager
        AsyncGenerator = typing.AsyncGenerator
        AsyncIterable = typing.AsyncIterable
        AsyncIterator = typing.AsyncIterator
        Awaitable = typing.Awaitable
        ByteString = typing.ByteString
        Callable = typing.Callable
        ChainMap = typing.ChainMap
        ClassVar = typing.ClassVar
        Collection = typing.Collection
        Container = typing.Container
        ContextManager = typing.AbstractContextManager
        Coroutine = typing.Coroutine
        Counter = typing.Counter
        DefaultDict = typing.DefaultDict
        Deque = typing.Deque
        Dict = typing.Dict
        Final = typing.Final
        FrozenSet = typing.FrozenSet
        Generator = typing.Generator
        Hashable = typing.Hashable
        ItemsView = typing.ItemsView
        Iterable = typing.Iterable
        Iterator = typing.Iterator
        KeysView = typing.KeysView
        List = typing.List
        Literal = typing.Literal
        Mapping = typing.Mapping
        MappingView = typing.MappingView
        MutableMapping = typing.MutableMapping
        MutableSequence = typing.MutableSequence
        MutableSet = typing.MutableSet
        NoReturn = typing.NoReturn
        Optional = typing.Optional
        OrderedDict = typing.OrderedDict
        Reversible = typing.Reversible
        Sequence = typing.Sequence
        Set = typing.Set
        Sized = typing.Sized
        TYPE_CHECKING = False
        Tuple = typing.Tuple
        Type = typing.Type
        Union = typing.Union
        ValuesView = typing.ValuesView
        __all__ = ['Any', 'Callable', 'ClassVar', 'Final', 'ForwardRef', 'Gene...
    
    FILE
        /Users/rbasnet/miniconda3/lib/python3.8/typing.py
    
    


## Type aliases

- assigning the type to the alias


```python
# Let's create a Vector type -> List of float
from typing import List
Vector = List[float]
```


```python
def scale(scalar: float, vector: Vector) -> Vector:
    """scale function.
    
    Scales each element in vector by scalar factor.
    """
    return [scalar * num for num in vector]
```


```python
# typechecks; a list of floats qualifies as a Vector.
new_vector = scale(2.0, [1.0, -4.2, 5.4])
```


```python
new_vector
```




    [2.0, -8.4, 10.8]




```python
new_vector1 = scale(2, [1, -4, 5])
```


```python
new_vector1
```




    [2, -8, 10]



## Generators

- special functions that return an iterator that returns a stream of values
- resumable functions that can retain local variable information to resume the function where it left off
- uses `yield` keyword to yield the next value as opposed to `return`
    - when `yield` is reached, the generator's state of execution is suspended and local variables are preserved
- `next(genObject)` calls the built_in `__next__()` method to resume executing, when the function is called again
- similar in concept to `range()`, however it returns listiterator object


```python
def generate_ints(N):
    for i in range(N):
        yield i # this makes the function a generator!
```


```python
gen = generate_ints(10)
```


```python
print(gen)
```

    <generator object generate_ints at 0x7f911282ee40>



```python
next(gen)
```




    0




```python
next(gen)
```




    1




```python
# iterate over the next of the values
for n in gen:
    print(n)
```

    2
    3
    4
    5
    6
    7
    8
    9



```python

```
