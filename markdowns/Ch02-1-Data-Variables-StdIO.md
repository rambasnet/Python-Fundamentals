# Data, Values, Expressions, Statements and Std IO

<a href="https://colab.research.google.com/github/rambasnet/FDSPython-Notebooks/blob/master/notebooks/Ch02-Data-Variables.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>


- http://openbookproject.net/thinkcs/python/english3e/variables_expressions_statements.html

## Topics
- data values and types
- variables
- expressions and statements
- numeric operators and basic computations
- order of operations
- standard input and output
- type casting
- Composition and algorithm

## Values and data types
- a value is one of the fundamental things or data -- like a letter or number -- that a program manipulates 
- these values are clssified into types
- Python fundamentally supports two major data types: numbers and strings
- Boolean (True/False) is also supported type

### Numbers
- Integer (int) 
    - +/- whole numbers: 199, -98, 0
- Float 
    - +/- real numbers - numbers with decimal points: 99.99, -0.01


### Strings
- Python uses **str** abbreviation for String type
- strings are one or more characters represent using single, double or tripple quotes
- according to PEP 8, use single or double quotes and be consistent

## Data Types
- built-in type() function can be used to know type of data
- functions will be covered in Chapter 04


```python
type(100)
```




    int




```python
type(-9)
```




    int




```python
type(1000.99345435)
```




    float




```python
type(-2.345)
```




    float




```python
type('Hello World!')
```




    str




```python
type('A')
```




    str




```python
print("hello")
```

    hello



```python
type("17")
```




    str




```python
type("""Triple double quoted data""")
```




    str




```python
type('''Type of Triple single quote data is''')
```




    str




```python
a = "hello"
```


```python
a
```




    'hello'



## Type conversion/casting
- data needs to be converted from one type to another as needed
- the process is called type casting
- use built-in functions such as str(), int() and float()
- **str(value)** - converts any value into string
- **int(value)** - converts numeric value into int
- **float(value)** - converts numeric value into float


```python
data = 'hello' # Can't convert it into int or float types
```


```python
type(data)
```




    str




```python
data = '100'
type(data)
```




    str




```python
data
```




    '100'




```python
num = int(data)
type(num)
```




    int




```python
num
```




    100




```python
price = float('500.99')
type(price)
```




    float




```python
float('hi')
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Cell In[20], line 1
    ----> 1 float('hi')


    ValueError: could not convert string to float: 'hi'



```python
num = 99.99
strNum = str(num)
type(strNum)
```




    str




```python
type(True)
```




    bool




```python
type(False)
```




    bool



## Statements
- a **statement** is an instruction that the Python interpreter can execute
- we've seen assignment statements so far
- we'll later explore for, if, import, while and other statements

## Expressions
- an **expression** is a combination of values, variables, operators, and calls to functions
- expressions are evaluated giving a results


```python
1+2
```




    3




```python
len('hello')
```




    5




```python
print(2+3*4)
```

    14


## Standard Output
- printing or writing output to common/standard output such as monitor
- way to display the results and interact with the users of your program
- use print() function


```python
print('''"Oh no", she exclaimed, "Ben's bike is broken!"''')
```

    "Oh no", she exclaimed, "Ben's bike is broken!"



```python

```


```python
print(34.55)
```

    34.55



```python
print(2+2)
```

    4


## Escape Sequences
- some letters or sequence of letters have special meaning to Python
- single, double and tripple single or double quotes represent string data
- use backslash \\ to represent these escape sequences, e.g.,
    - \\n - new line
    - \\\\ - back slash
    - \\t - tab
    - \\r - carriage return
    - \\' - single quote
    - \\" - double quote


```python
print('What\'s up\n Shaq O\'Neal?')
```

    What's up
     Shaq O'Neal?



```python
print('hello \there...\n how are you?')
```

    hello 	here...
     how are you?



```python
print('how many back slahses will be printeted? \\\\')
```

    how many back slahses will be printeted? \\



```python
print(r'how many back slahses will be printeted now? \\\\')
```

    how many back slahses will be printeted now? \\\\


## Variables
- variables are identifiers that are used to store values which can be then easily manipulated
- variables give names to data so the data can be easily referenced by their names over and again
- rules and best practices for creating identifiers and variable names:
    - can't be a keyword -- what are the built-in keywords?
    - can start with only alphabets or underscore ( _ )
    - can't have symbols such as $, %, &, white space, etc.
    - can't start with a digit but digits can be used anywhere else in the name
    - use camelCase names or use _ for_multi_word_names
    - use concise yet meaningul and unambigous names for less typing and avoid typos


```python
help('keywords')
```

    
    Here is a list of the Python keywords.  Enter any keyword to get more help.
    
    False               class               from                or
    None                continue            global              pass
    True                def                 if                  raise
    and                 del                 import              return
    as                  elif                in                  try
    assert              else                is                  while
    async               except              lambda              with
    await               finally             nonlocal            yield
    break               for                 not                 
    



```python
# Variable must be defined/declared before you can use
print(x)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    Cell In[35], line 2
          1 # Variable must be defined/declared before you can use
    ----> 2 print(x)


    NameError: name 'x' is not defined



```python
x = 'some value'
```


```python
print(x)
```

    some value



```python
# Exercise: Define a bunch of variables to store some values of different types
var1 = -100
num = -99.99
name = 'John'
lName = 'Smith'
MI = 'A'
grade = 10.5
Name = 'Jake'
grade = 19.9
```

## Dynamic Typing
- type of variables are dynamically evaluated in Python when the assignment statement is executed
- same variable can be uesd to hold different data types


```python
var = 100
```


```python
var = 'hello'
```


```python
var = 99.89
```


```python
var
```




    99.89



## Visualize variable assignments in pythontutor.com
[Click Here](http://pythontutor.com/visualize.html#code=var1%20%3D%20100%0Anum%20%3D%2099.99%0Aname%20%3D%20'John'%0AlName%20%3D%20'Smith'%0AMI%20%3D%20'A'%0Agrade%20%3D%2010.5%0Agrade%20%3D%2019.9%0AName%20%3D%20'Jake'&cumulative=false&curInstr=0&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

## Numeric computation
- numeric computation is usually carried out with experssions involving operators and operands
- **operators** are special tokens/symbols that represent computations like addition, multiplication and division 
- the values an operator uses are called **operands**
- some binary operators that take two operands
    - addition: 10 + 20
    - subtraction: 20 - 10 
    - true division: 10 / 3
    - multiplication: 7 * 9
    - integer division: 10 // 3
    - remainder or modulus operator: 10 % 2
    - power: 2 ** 3


```python
# Exercise: play with some examples of various operators supported by Python
```

## Order of operations
- depends on the rules of precedence

**uses PEMDAS rule from high to low order**

1. Parenthesis
2. Exponentiation
3. Multiplication and Division (left to right)
4. Addition and Subtraction (left to right)



```python
# Some examples
print(2 * 3 ** 2)
```

    18



```python
x = 1
y = 2
z = 3
ans = x+y-z*y**y
print(ans)
```

    -9


## Operations on strings
- $+$ and $*$ operators also work on strings
- Chapter 08 covers more on string data type and operations


```python
# Some examples
fname = "John"
lname = "Smith"
fullName = fname + lname
print(fullName)
```

    JohnSmith



```python
gene = "AGT"*10
```


```python
print(gene)
```

    AGTAGTAGTAGTAGTAGTAGTAGTAGTAGT


## Standard input
- read data from standard or common input such as keyboards
- allows your program to receive data during program execution facilitating user interactions
- input values will have type string even if numbers are entered
- use variables to store the data read from standard input


```python
name = input('What is your name? ')
```

    What is your name?  John Doe



```python
print('hello,', name)
```

    hello, John Doe



```python
num = input('Enter a number =>')
print('You entered: ', num)
print('type of', num, '=', type(num))
```

    Enter a number => 5
    You entered:  5
    type of 5 = <class 'str'>



```python
num
```




    '5'




```python
# str must be casted into int or float depending on the value required
num = int(num)
print('type of', num, '=', type(num))
```

    type of 5 = <class 'int'>


### How to read multiple values in a single line

- use split() method of string class to split the input string into multiple values


```python
# Enter two numbers separated by space, how about three numbers?
values = input()
num1, num2 = values.split()
num1 = int(num1)
num2 = int(num2)
print(f'{num1=} and {num2=}')
```

    num1=10 and num2=20


## Composition
- break a problem into many smaller sub-problems or steps using high-level algorithm steps
- incrementally build the solution using the sub-problems or steps

## Algorithm
- step by step process to solve a given problem
    - like a recipe for a food menu
- what are the steps you'd give a martian to buy grocery on earth?
    - Make a shopping list 
    - Drive to a grocery store
    - Park your car
    - Find items in the list
    - Checkout
    - Load grocery
    - Drive home

## Exercises

#### 1. area and perimeter of a rectangle

 - write a python script that calculates area and perimeter of a rectangle


```python
# Demonstrate composition step by step
# Algorithm steps
# 1. Get length and width of a rectangle
#     a. use hard coded values OR
#     b. prompt user to enter length and width values
#        i. convert length and width into correct data types
# 2. Calculate area = length x width
# 3. Calculate perimeter = 2(length + width)
# 4. Display calculated results
```

#### 2. area and circumference of a circle
- write a python script that calculates area and circumference of a circle
- area of a circle is calculated using equation: $\pi r^{2}$
- perimeter of a circel is calculated using equation: $2 \pi r$
- you can use $\pi=3.14159$


```python
# Demonstrate composition step by step
# Algorithm steps
```

#### 3. Body Mass Index (BMI)
- write a python script that calculates BMI of a person
- BMI is body mass in kg divided by the square of body height in meter with the units of $kg/m^2$
- [https://www.nhlbi.nih.gov/health/educational/lose_wt/BMI/bmicalc.htm](https://www.nhlbi.nih.gov/health/educational/lose_wt/BMI/bmicalc.htm)

#### 4. area and perimeter of a triangle
- write a python script that finds area and perimeter of a triangle given three sides
- Hint: Google and use Heron's formula to find area of triangle

## Kattis Problems

- Concatenate - https://open.kattis.com/problems/skeytasaman 
- Class Photo - https://open.kattis.com/problems/classphoto
- E-Days Ore Cart Pull - https://open.kattis.com/problems/edays
- Parking Pandemonium - https://open.kattis.com/problems/parkingpandemonium
- M-Climb - https://open.kattis.com/problems/mclimb   
- Triangle Area - [https://open.kattis.com/problems/triarea](https://open.kattis.com/problems/triarea)
- Two-sum - https://open.kattis.com/problems/twosum
- Leggja samman - [https://open.kattis.com/problems/leggjasaman](https://open.kattis.com/problems/leggjasaman) 
- R2 - [https://open.kattis.com/problems/r2](https://open.kattis.com/problems/r2)
- Amerískur vinnustaður - [https://open.kattis.com/problems/ameriskur](https://open.kattis.com/problems/ameriskur)
- Fifa - [https://open.kattis.com/problems/fifa](https://open.kattis.com/problems/fifa)
- Diggy Hole - https://open.kattis.com/problems/grafaholur
- Dannebrog - https://open.kattis.com/problems/dannebrog



```python

```
