# Conditionals - flow-control structures

<a href="https://colab.research.google.com/github/rambasnet/FDSPython-Notebooks/blob/master/notebooks/Ch04-Conditionals.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

- http://openbookproject.net/thinkcs/python/english3e/conditionals.html

## Topics
- conditional statements and types
- comparision operators
- Truth tables

## Conditional/Logical Structures
- conditional statements control the flow of execution of codes
    - makes some block of code to skip or execute based on some conditions
    - loosely speaking, it helps computer think and make decision
- boolean values - True or False
- boolean expressions - comparison operators are used to compare values that result in True or False

## Comparison operators
- allow us to compare data values resulting in True or False outcome
- these are binary operators; take two operands where left hand side is compared with right hand side
- **==** (equal to)
- **!=** (not equal to)
- **>** (greater than)
- **>=** (greater than or equal to)
- **<** (less than)
- **<=** (less than or equal to)
- comparison operators are used to create conditional statements


```python
# Examples of various comparison operators
x = 5
y = 10
```


```python
# Is x equal to y? True or False?
x == y
```




    False




```python
# Is x not equal to y? True of False?
x != y
```




    True




```python
# Is x is greater than y? True or False?
x > y
```




    False




```python
# Is x less than y?
x < y
```




    True




```python
# Is x less than or equal to y?
x <= y
```




    True




```python
# Is x greater than or equal to y
x >= y
```




    False



## Conditional execution
- execute or skip a block of code when some condition is met
- conditional statments are created using keyword **if (condition) **
- three types of conditional selectors
- One-way, Two-way and Multi-way selectors

## One-way selector
- just an if statement by itself
- syntax:

```python
if <boolean expression> == True:
    # execute this block of code
```

- boolean expression can also comapre to False; the ultimate comparison result has to be True!

### [Visualize in PythonTutor.com](http://pythontutor.com/visualize.html#code=a%20%3D%20'apple'%0Aif%20a%20%3D%3D%20'apple'%3A%0A%20%20%20%20print%28'var%20a%20equals%20to%20apple'%29%0Aprint%28'continue%20execution%20here...'%29&cumulative=false&curInstr=0&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
if True:
    print('Hello, there!')
```

    Hello, there!



```python
a = 'apple'
if a == 'apple': # this should evaluate True
    print('value of a equals to apple')
print('continue execution here...')
```

    value of a equals to apple
    continue execution here...



```python
a = 'apple'
if a == 'Apple': # this should evaluate False
    print('value of a equal to Apple') # this block will NOT be executed!
print('continue execution here...')
```

    continue execution here...


## Two-way selector

- if statement followed by else statement
- syntax:

```python
if <boolean expression> == True:
    # execute this block of code
else:
    # otherwise, execute this
    
```

### [Visualize in PythonTutor.com](http://pythontutor.com/visualize.html#code=num1%20%3D%20100.5%0Anum2%20%3D%20100.49999999999999%0A%0Aif%20%20num1%20%3E%20num2%3A%0A%20%20%20%20print%28'%7B%7D%20is%20greater%20than%20%7B%7D'.format%28num1,%20num2%29%29%0Aelse%3A%0A%20%20%20%20print%28'%7B%7D%20is%20NOT%20greater%20than%20%7B%7D'.format%28num1,%20num2%29%29&cumulative=false&curInstr=0&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


```python
num1 = 100.5
num2 = 100.49999999999999

if  num1 > num2:
    print('{} is greater than {}'.format(num1, num2))
else:
    print('{} is NOT greater than {}'.format(num1, num2))
```

    100.5 is greater than 100.49999999999999



```python
if 10 >= 20:
    print ('print 10 is greater than or equal to 20')
else:
    print ('print 10 is NOT greater than or equal to 20')
```

    print 10 is NOT greater than or equal to 20


## Multi-way selector
- similar to multiple-choice questions with only one valid answer
- start from first **if statement**, if a **conditional expression** is evaluated True, the rest **elif** and **else** are ignored

```python
if <condition1>: 
    # block1
    # execute this...
elif <condition2>:
    # block2 
    # execute this
... 
... 
else: 
    # if all the previous conditions are evaluated False; this is the alternative!
    # else block
    # execute code in this block
    
```


```python
# Guess the number entered by user
ans = int(input('Enter a number between 1-5: '))
if ans == 1:
    print('You entered 1')
elif ans == 2:
    print('You entered 2')
elif ans == 3:
    print('You entered 3')
elif ans == 4:
    print('You entered 4')
elif ans == 5:
    print('You entered 5')
elif ans > 5:
    print('You entered a number larger than 5')
else:
    print('Hmm.... I do not know what you entered!')
```

    Enter a number between 1-5: 2
    You entered 2


### [Visualize in PythonTutor.com](https://goo.gl/ZSm9KS)

## Logical Operators
**and**, **or**, and **not** -- allow to build more complex boolean expressions <br >

**Truth table for and**

| a | b  | a **and** b |
| --- | --- | --- |
| T | T |  T |
|T | F |  F |
|F | T |  F |
|F | F |  F |


**Truth table for or**

| a | b  | a **or** b |
| --- | --- | --- |
| T | T |  T |
|T | F |  T |
|F | T |  T |
|F | F |  F |

**Truth table for not**

|a  |  not a |
|---|---|
|T  |   F |
|F  |   T |

### Order of Evaluations of operators and expressions: 
- Highest to Lowest: http://www.informit.com/articles/article.aspx?p=459269&seqNum=11


```python
# and demo
num = 10
if (num%2 == 0 and num > 0):
    print(f"{num} is even and positive")
```

    10 is even and positive



```python
# and demo
num = -14
if num %2 == 0 and num < 0:
    print(f"{num} is even and negative")
```

    -14 is even and negative



```python
# or demo
# a retimerment calculator
money = int(input('How much money have you saved? '))
ferrari = input('Do you have a farrari? [y/yes | n/no]: ')
if money >= 1000000 or ferrari == 'y' or ferrari == 'yes':
    print('Congrats!! You can retire now.')
else:
    print('Sorry, keep working!!')
```

    How much money have you saved? 100000
    Do you have a farrari? [y/yes | n/no]: yes
    Congrats!! You can retire now.



```python
# not example
if not False:
    print('True')
```

    True



```python
# not demo
# a retimerment calculator
money = int(input('How much money have you saved? '))
ferrari = input('Do you have a farrari? [y/yes | n/no]: ')
if not (money >= 1000000 or ferrari == 'y' or ferrari == 'yes'):
    print('Sorry, keep working!!')
else:
    print('Congrats!! You can retire now.')
```

    How much money have you saved? 10
    Do you have a farrari? [y/yes | n/no]: y
    Congrats!! You can retire now.


## Nested conditionals
- conditional statements can be nested inside another conditional statements
- syntax:

```python
if condition:
    if condition1:
        # do something
    else:
        # do something else
        if condition2:
            # do something...
else:
    # do this...

```


```python
# program that determines if a given number is even or odd, positive or negative 
num = -100
if num == 0:
    print(f'{num} is zero!')
elif num%2 == 0:
    if num > 0:
        print(f"{num} is even and positive")
    else:
        print(f'{num} is even and negative')
else:
    if num > 0:
        print(f"{num} is odd and positive")
    else:
        print(f'{num} is odd and negative')
        
print('done')
```

    -100 is even and negative
    done


### [Visualize in PythonTutor.com](http://pythontutor.com/visualize.html#code=num%20%3D%20-100%0Aif%20num%20%3D%3D%200%3A%0A%20%20%20%20print%28'%7B%7D%20is%20zero!'.format%28num%29%29%0Aelif%20num%252%20%3D%3D%200%3A%0A%20%20%20%20if%20num%20%3E%200%3A%0A%20%20%20%20%20%20%20%20print%28num,%20%22is%20even%20and%20positive%22%29%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20print%28num,%20'is%20even%20and%20negative'%29%0Aelse%3A%0A%20%20%20%20if%20num%20%3E%200%3A%0A%20%20%20%20%20%20%20%20print%28num,%20%22is%20odd%20and%20positive%22%29%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20print%28num,%20'is%20odd%20and%20negative'%29&cumulative=false&curInstr=0&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

## Exercises
Exercise 1: Write a program to test whether a given whole number is even, odd or zero.


```python
x = input('Enter a whole number: ')
x = int(x)
if x == 0:
    print(x, 'is zero')
elif x%2 == 0:
    print(x, 'is even')
else:
    print(x, 'is odd')
```

    Enter a whole number:1
    1 is odd


Exercise 1.1: Rewrite Exercise 1 using a function and write 2 test cases.


```python
def isEvenOddOrZero(num):
    if num == 0:
        return 'zero'
    elif num%2 == 0:
        return 'even'
    else:
        return 'odd'
```


```python
def test():
    assert isEvenOddOrZero(10) == 'even'
    assert isEvenOddOrZero(0) == 'zero'
    assert isEvenOddOrZero(19) == 'odd'
    print('all test cases passed...')
```


```python
test()
```

    all test cases passed...


Exercise 2. Write a function that returns whether the given whole number is positive or negative. Also write at least 2 test cases.


```python
def positiveNegativeOrZero(num):
    if num == 0:
        return 'zero'
    elif num > 0:
        return 'positive'
    else:
        return 'negative'
```


```python
def test_positiveNegativeOrZero():
    assert positiveNegativeOrZero(0) == 'zero'
    assert positiveNegativeOrZero(100) == 'positive'
    assert positiveNegativeOrZero(-99.99) == 'negative'
    print('all test cases passed for positiveNegativeOrZero()')
```


```python
test_positiveNegativeOrZero()
```

    all test cases passed for positiveNegativeOrZero()


Exercise 3: Write a program that converts students' grade value (0-100) to corresponding letter grade (A-F) where
    
`
90 and above is A
80 and above is B
70 and above is C
60 and above is B
59 and below is F
`

Write test cases to test each outcome.

Exercise 4: Write a program that helps someone decide where to go eat lunch depending on amount of money one has in their pocket.

Exercise 5: Given a day of week as integer (say 1 for Sunday) write a program that tells whether that day is weekend, or weekday and the actual name of the day.

Exercise 6: Write a program that determines whether someone is eligible to vote in the US federal election.

Exercise 7: Write a function day_name that converts an integer number 0 to 6 into the name of a day. Assume day 0 is “Sunday”. Once again, return None if the argument to the function is not valid.


```python
def day_name(day):
    pass
```


```python
# Here are some tests that should pass
def test_day_name():
    assert day_name(3) == "Wednesday"
    assert day_name(6) == "Saturday"
    assert day_name(42) == None
    print('all test cases passed for day_name()')
```


```python
test_day_name()
```


    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    <ipython-input-3-97913494fc66> in <module>()
    ----> 1 test_day_name()
    

    <ipython-input-2-3f7d21d757ff> in test_day_name()
          1 def test_day_name():
    ----> 2     assert day_name(3) == "Wednesday"
          3     assert day_name(6) == "Saturday"
          4     assert day_name(42) == None
          5     print('all test cases passed for day_name()')


    AssertionError: 


Exercise 8: Write a function that helps answer questions like ‘“Today is Wednesday. I leave on holiday in 19 days time. What day will that be?”’ So the function must take a day name and a delta argument (the number of days to add) and should return the resulting day name.s


```python
def day_add(dayName, delta):
    pass
```


```python
# Here are some tests that should pass
def test_day_add():
    assert day_add("Monday", 4) ==  "Friday"
    assert day_add("Tuesday", 0) == "Tuesday"
    assert day_add("Tuesday", 14) == "Tuesday"
    assert day_add("Sunday", 100) == "Tuesday"
    assert day_add("Sunday", -1) == "Saturday"
    assert day_add("Sunday", -7) == "Sunday"
    assert day_add("Tuesday", -100) == "Sunday"
    print('all test cases passed for day_add()')
```


```python
test_day_add()
```

## Kattis problems

- Almost every problem involve some form of conditional statements
- The following problems are good examples of conditional statements and the concepts covered so far:

- Elevators - https://open.kattis.com/problems/elevators
- Veður - Vindhraði - [https://open.kattis.com/problems/vedurvindhradi](https://open.kattis.com/problems/vedurvindhradi)
- A Terrible Fortress - https://open.kattis.com/problems/aterriblefortress
- Úllen dúllen doff - [https://open.kattis.com/problems/ullendullendoff](https://open.kattis.com/problems/ullendullendoff)
- Sith - [https://open.kattis.com/problems/sith](https://open.kattis.com/problems/sith)
- Two Stones - [https://open.kattis.com/problems/twostones](https://open.kattis.com/problems/twostones)
- Adding Trouble - [https://open.kattis.com/problems/adding](https://open.kattis.com/problems/adding)
- Staying Frosty https://open.kattis.com/problems/stayingfrosty
- Wake up call https://open.kattis.com/problems/wakeupcall
- Pigeon-holes - https://open.kattis.com/problems/dufuskuffur
- Driving Dilemma - https://open.kattis.com/problems/drivingdilemma
- L33T H4X0R - https://open.kattis.com/problems/l33th4x0r
- Ski Traffic - https://open.kattis.com/problems/skitraffic





```python

```
