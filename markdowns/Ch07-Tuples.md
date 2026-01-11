# Tuples
<a href="https://colab.research.google.com/github/rambasnet/Python-Fundamentals/blob/master/notebooks/Ch07-Tuples.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

- http://openbookproject.net/thinkcs/python/english3e/tuples.html
- containers used for grouping data values surrounded with parenthesis
- data values in tuples are called elements/items/members
- two major operations done with tuples are:
    1. packing (creating tuples)
    2. unpacking (storing data into individual variables)


```python
year_born = ("Paris Hilton", 1981) # tuple packing
```


```python
print(year_born)
```

    ('Paris Hilton', 1981)



```python
star = "Paris", 'J', 'Hilton', 1981, 32, 1.2 # tuple packing without parenthesis
```


```python
star
```




    ('Paris', 'J', 'Hilton', 1981, 32, 1.2)




```python
type(star)
```




    tuple




```python
# tuple assignment
fname, mi, lname, year, age, income = star # tuple unpacking 
# no. of variables must match no. values in tuple
```


```python
fname
```




    'Paris'




```python
lname
```




    'Hilton'




```python
print(income)
```

    1.2



```python
# swap values of two variables
a = 100
b = 200
a, b = b, a
```


```python
print(a, b)
```

    200 100


## Member access
- each member of tuple can be accessed using `[ index ]` operator
- index is 0-based or starts from 0


```python
name = ('John', 'A.', 'Smith')
```


```python
print(name[0], name[1], name[2])
```

    John A. Smith


## Length of tuple

- `len()` gives the length (no. of elements) of tuple


```python
len(name)
```




    3



## Tuple membership
- **in** and **not in** boolean operators let's you check for membership


```python
'John' in name
```




    True




```python
'B.' in name
```




    False




```python
'Jake' not in name
```




    True



## Function can return multiple values as Tuple

- multiple comma separated values can be packed and returned as tuple from function 


```python
def maxAndMin(a, b, c, d, e):
    myMax = a #max(a, b, c, d, e)
    if myMax < b:
        myMax = b
    if myMax < c:
        myMax = c
    if myMax < d:
        myMax = d
    if myMax < e:
        myMax = e
    values = [a, b, c, d, e]
    myMin = min(values)
    return myMax, myMin
    
```


```python
ab = maxAndMin(10, 20, 5, 100, 34)
print(f'max = {ab[0]} and min = {ab[1]}')
```

    max = 100 and min = 5


## Tuples are immutable
- can't change tuple in-place or update its elements 
    - similar to string


```python
a = (1, 2, 3)
print(a[0])
```

    1



```python
a[0] = 100
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-6-b6d7a4db9a51> in <module>()
    ----> 1 a[0] = 100
    

    TypeError: 'tuple' object does not support item assignment


## Applications of Tuple

- application of tuples is limited due to its immutability in nature


```python

```
