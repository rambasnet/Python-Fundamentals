## Built-in Functions
<a href="https://colab.research.google.com/github/rambasnet/FDSPython-Notebooks/blob/master/notebooks/Ch03-1-Functions-Built-in.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

- named sequence of code that does some specific task or a function
- we'll learn how to define our own functions in [User Defined Functions chapter](./Ch03-3-Functions-UserDefined.ipynb)
- some built-in functions we've used so far: `type( ), int( ), float( ), str( ), input( ), print( )`, etc.
- Python provides a list of built-in functions that are readily available for use:
https://docs.python.org/3/library/functions.html
- below are examples of some built-in functions that may be useful to know

### bin(x)
- converts an integer number $x$ to a binary string prefixed with "0b".


```python
bin(3)
```




    '0b11'



### format(value, format_spec)
- formats the give value using format spec


```python
help(format)
```

    Help on built-in function format in module builtins:
    
    format(value, format_spec='', /)
        Return value.__format__(format_spec)
        
        format_spec defaults to the empty string.
        See the Format Specification Mini-Language section of help('FORMATTING') for
        details.
    



```python
# If prefix "0b is desired or not, use either of the following ways
print(format(3, '#b'))
print(format(3, 'b'))
```

    0b11
    11


### chr( uniCode )
- returns the string representing a character whose Unicode code point is the integer uniCode
- inverse of ord(character)


```python
print(chr(65))
print(chr(97))
print(chr(8364))
```

    A
    a
    €


### globals() and locals()
- globals() returns a dictionary representing the current global symbol table
- locals() returns a dictionary representing the current local symbol table


```python
globals()
```




    {'__name__': '__main__',
     '__doc__': 'Automatically created module for IPython interactive environment',
     '__package__': None,
     '__loader__': None,
     '__spec__': None,
     '__builtin__': <module 'builtins' (built-in)>,
     '__builtins__': <module 'builtins' (built-in)>,
     '_ih': ['',
      'bin(3)',
      '# If prefix "0b is desired or not, use either of the following ways\nprint(format(3, \'#b\'))\nprint(format(3, \'b\'))',
      'print(chr(65))\nprint(chr(97))\nprint(chr(8364))',
      'globals()'],
     '_oh': {1: '0b11'},
     '_dh': ['/Volumes/Storage/GoogleDrive/CMU/Python/thinkpythonnotebooks'],
     '_sh': <module 'IPython.core.shadowns' from '/Users/rbasnet/miniconda3/lib/python3.7/site-packages/IPython/core/shadowns.py'>,
     'In': ['',
      'bin(3)',
      '# If prefix "0b is desired or not, use either of the following ways\nprint(format(3, \'#b\'))\nprint(format(3, \'b\'))',
      'print(chr(65))\nprint(chr(97))\nprint(chr(8364))',
      'globals()'],
     'Out': {1: '0b11'},
     'get_ipython': <bound method InteractiveShell.get_ipython of <ipykernel.zmqshell.ZMQInteractiveShell object at 0x10f035278>>,
     'exit': <IPython.core.autocall.ZMQExitAutocall at 0x10fa42668>,
     'quit': <IPython.core.autocall.ZMQExitAutocall at 0x10fa42668>,
     '_': '0b11',
     '__': '',
     '___': '',
     '_i': 'print(chr(65))\nprint(chr(97))\nprint(chr(8364))',
     '_ii': '# If prefix "0b is desired or not, use either of the following ways\nprint(format(3, \'#b\'))\nprint(format(3, \'b\'))',
     '_iii': 'bin(3)',
     '_i1': 'bin(3)',
     '_1': '0b11',
     '_i2': '# If prefix "0b is desired or not, use either of the following ways\nprint(format(3, \'#b\'))\nprint(format(3, \'b\'))',
     '_i3': 'print(chr(65))\nprint(chr(97))\nprint(chr(8364))',
     '_i4': 'globals()'}



### hex(x)
- convert an integer number to a lowercase hexadecimal string prefixed with "0x"


```python
print(hex(42))
print(hex(-42))
```

    0x2a
    -0x2a



```python
# Other ways
print(format(255, '#x'))
print(format(255, 'x'))
print(format(255, 'X'))
```

    0xff
    ff
    FF


### oct(x)
- return an octal string representation with "0o" prefix of a given integer x


```python
print(oct(100))
```

    0o144



```python
print(format(10, '#o'))
print(format(10, 'o'))
```

    0o12
    12


### ord(c)
- return an integer representing the Unicode code of a given Unicode character


```python
print(ord(' '))
print(ord('~'))
```

    32
    126


### id(object)
- return the 'identity' of an object
- guaranteed unique integer and constant thoughout its lifetime


```python
x = 10
```


```python
id(x)
```




    4525196800



### divmod(a, b)
- given two non-complex numbers as arguments, return a pair of numbers as tuple consisting of their quotient and remainder using integer division


```python
print(divmod(7, 3)) # Return (quotient, remainder)
quotient, remainder = divmod(7, 3)
print(quotient, remainder)
```

    (2, 1)
    2 1


### eval(expression, globals=None, locals=None)
- the expression argument is parsed and evaluated as Python expression
- syntax errors reported as exceptions


```python
y = 2
print(eval('y**2'))
print(eval('y+2*3'))
```

    4
    8


### max(iterable, ...) or max(arg1, arg2, ...)
- returns the largest item in an iterable or the largest of two or more arguments


```python
print('max=', max(100, 8.9, 999, 1000.5))
```

    max= 1000.5


### min(arg1, arg2, ...)
- returns the smallest of the the arguments (arg1, arg2...)


```python
print('min=', min(100, 8.9, 999, 1000.5))
```

    min= 8.9


### pow(base, exponent) 
- returns base to the power exponent


```python
print('2 to the power 3 =', pow(2, 3))
```

    2 to the power 3 = 8


### print( )
- print(*object, sep=' ', end='\\n', file=sys.stdout, flush=False) prototype
- print takes many arguments and prints arbitrary number of values
- below demos some print examples with different argument values


```python
print('hi', 'hello', sep='', end='')
print('next line?')
```

    hihellonext line?



```python
print('hi', 'hello', sep=' ', end='')
print('next line?')
```

    hi hellonext line?



```python
print('hi', 'hello', 1, 2, 3, sep='$', end='', flush=True)
print('next line?')
```

    hi$hello$1$2$3next line?



```python
print('hi', 'hello', sep='\t', end='\n')
print('next line?')
```

    hi	hello
    next line?


## Kattis Problems

### Buka
- [https://open.kattis.com/problems/buka](https://open.kattis.com/problems/buka)
- Hint: use eval() on 3 input strings

### Ekki dauði opna inni
- [https://open.kattis.com/problems/ekkidaudi](https://open.kattis.com/problems/ekkidaudi)
- Hinit: use .split('|') method on string and just print




```python

```
