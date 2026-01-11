# Lists
<a href="https://colab.research.google.com/github/rambasnet/Python-Fundamentals/blob/master/notebooks/Ch08-1-Lists.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

- http://openbookproject.net/thinkcs/python/english3e/lists.html

## Topics
- list data structure
- syntax to create lists
- methods or operations provided to list objects
- list operators
- list traversal
- list applications and problems

## List
- a type of sequence or container
- ordered collection of values called elements or items
- lists are similar to strings (ordered collections of characters) except that elements of a list can be of any type

## Creating lists
- several ways; the simplest is to enclose the elements in square brackets `[ ]`


```python
alist = [] # an empty list
```


```python
blist = list() # use list constructor
```


```python
type(alist)
```




    list




```python
# creating lists with some elements of same type
list1 = [10, 20, 30, 40]
list2 = ['spam', 'bungee', 'swallow']
```


```python
# lists with elements of different types
list3 = ["hello", 2.0, 10, [10, ('hi', 'world'), 3.5], (1, 'uno')]
```


```python
# print list
print(list3)
```

    ['hello', 2.0, 10, [10, ('hi', 'world'), 3.5], (1, 'uno')]



```python
# quickly create a list of range of numbers between 1 and 19
list4 = list(range(1, 20, 1))
```


```python
print(list4)
```

    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]



```python
# print multiple lists
print(alist, list1, list2, list3)
```

    [] [10, 20, 30, 40] ['spam', 'bungee', 'swallow'] ['hello', 2.0, 10, [10, ('hi', 'world'), 3.5], (1, 'uno')]



```python
# Exercise: create a list of even numbers between 1 and 20 inclusive
```


```python
# Exercise: create a list of odd numbers between 1 and 20 inclusive
```


```python
# Exercise: create a list of numbers from 20 to 1 inclusive
```

## Accessing elements
- same syntax for accessing characters of a string
- use the index operator: `listName[index]`


```python
# let's see what elements are in list1
list1
```




    [10, 20, 30, 40]




```python
# access an element, which one?
list1[0]
```




    10




```python
list3
```




    ['hello', 2.0, 10, [10, ('hi', 'world'), 3.5], (1, 'uno')]




```python
list3[3][0]
```




    10




```python
# list index can be variable as well
index = 0
print(list3[index])
```

    hello



```python
# can you use float value as an index?
list3[1.0]
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-18-1fc6b2fe2f36> in <module>
          1 # can you use float value as an index?
    ----> 2 list3[1.0]
    

    TypeError: list indices must be integers or slices, not float


## Lenght of list

- use `len(listObject)` to find length or number of elements in a list


```python
# how many elements are there in list3?
len(list3)
```




    5




```python
# what happens if you access an index equal to the size of the list
list3[5]
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-20-207cd7e1c880> in <module>
          1 # what happens if you access an index equal to the size of the list
    ----> 2 list3[5]
    

    IndexError: list index out of range



```python
list3
```




    ['hello', 2.0, 10, [10, ('hi', 'world'), 3.5], (1, 'uno')]




```python
# Exercise: access and print the last element of list3
```


```python
# Can we use negative index?
# Can you guess the output of the following code?
print(list3[-1])
```

    (1, 'uno')



```python
# Exercise - access and print 'world' in list3
```

## Checking for membership
- checking if some data/object is a member/element in the given list
- `in` and `not in` boolean operators let's you check for membership


```python
horsemen = ["war", "famine", "pestilence", ["death"]]
'death' in horsemen
```




    False




```python
'War' not in horsemen
```




    True




```python
["death"] in horsemen
```




    True



## Traversing lists
- for or while loop can be used to traverse through each element of a list


```python
list3
```




    ['hello', 2.0, 10, [10, ('hi', 'world'), 3.5], (1, 'uno')]




```python
# common technique; use for loop
for item in list3:
    print(item)
```

    hello
    2.0
    10
    [10, ('hi', 'world'), 3.5]
    (1, 'uno')



```python
for item in list3:
    if isinstance(item, list) or isinstance(item, tuple):
        for l in item:
            print(l)
    else:
        print(item)
```

    hello
    2.0
    10
    10
    ('hi', 'world')
    3.5
    1
    uno



```python
horsemen = ["war", "famine", "pestilence", "death"]
for i in [0, 1, 2, 3]:
    print(horsemen[i])
# better way to do the same thing?
```

    war
    famine
    pestilence
    death



```python
print("traversing using indices")
for i in range(len(horsemen)):
    print(horsemen[i])
```

    traversing using indices
    war
    famine
    pestilence
    death



```python
print('traversing each element')
for ele in horsemen:
    print(ele)
```

    traversing each element
    war
    famine
    pestilence
    death


## list operators
- \+ operator concatenates two lists and gives a bigger list
- \* operator repeats a list elements a given number of times


```python
list2
```




    ['spam', 'bungee', 'swallow']




```python
list3
```




    ['hello', 2.0, 10, [10, ('hi', 'world'), 3.5], (1, 'uno')]




```python
list4 = list2 + list3
```


```python
list4
```




    ['spam',
     'bungee',
     'swallow',
     'hello',
     2.0,
     10,
     [10, ('hi', 'world'), 3.5],
     (1, 'uno')]




```python
[0]*10
```




    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]




```python
a = [1, 2, 3]*4
```


```python
a
```




    [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]




```python
b = [a]*3
```


```python
b
```




    [[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],
     [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],
     [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]]




```python
# 2-D list or matrix
matrix = [[1, 2], [3, 4], [5, 6]]
```


```python
print(matrix)
```

    [[1, 2], [3, 4], [5, 6]]



```python
matrix
```




    [[1, 2], [3, 4], [5, 6]]




```python
# How do you replace 5 with 50 in matrix?
matrix[2][0] = 50
```


```python
matrix
```




    [[1, 2], [3, 4], [50, 6]]



## Slicing lists
- all the slice operations that work with strings also work with lists
- syntax: [startIndex : endIndex : step]
- startIndex is inclusive; endIndex is exclusive; step is optional by default 1


```python
# create a list of lower-case alphabets
alphas = ['a', 'b', 'c', 'd', 'e', 'f', 'g'] # add the rest...
```


```python
alphas
```




    ['a', 'b', 'c', 'd', 'e', 'f', 'g']




```python
# there's better way to create lists of all lowercase ascii
import string
alphas = list(string.ascii_lowercase)
```


```python
print(alphas[:])
```

    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



```python
print(alphas[::3])
```

    ['a', 'd', 'g', 'j', 'm', 'p', 's', 'v', 'y']



```python
print(alphas[1:3])
```

    ['b', 'c']



```python
print(alphas[::-1])
```

    ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']


## Lists and strings
- match made in heaven - work together really well :)


```python
# convert string to list of characters
alphaList = list(string.ascii_lowercase)
```


```python
alphaList
```




    ['a',
     'b',
     'c',
     'd',
     'e',
     'f',
     'g',
     'h',
     'i',
     'j',
     'k',
     'l',
     'm',
     'n',
     'o',
     'p',
     'q',
     'r',
     's',
     't',
     'u',
     'v',
     'w',
     'x',
     'y',
     'z']




```python
# convert list to string by joining pairs of chars with a delimiter
alphaStr = '|'.join(alphaList)
```


```python
alphaStr
```




    'a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z'



## lists are mutable
- we can change/replace/update list elements in place


```python
names = ["john", "David", "Alice"]
names[0] = "jake"
```


```python
names
```




    ['jake', 'David', 'Alice']




```python
# How to correct spelling of jake?
names[0][0]
```




    'j'




```python
names[0][0] = 'J'
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-62-0442e9474c4b> in <module>
    ----> 1 names[0][0] = 'J'
    

    TypeError: 'str' object does not support item assignment



```python
names[0] = 'Jake'
```


```python
names
```




    ['Jake', 'David', 'Alice']




```python
alphas
```




    ['a',
     'b',
     'c',
     'd',
     'e',
     'f',
     'g',
     'h',
     'i',
     'j',
     'k',
     'l',
     'm',
     'n',
     'o',
     'p',
     'q',
     'r',
     's',
     't',
     'u',
     'v',
     'w',
     'x',
     'y',
     'z']




```python
alphas[:4] = ['A', 'B', 'C', 'D']
```


```python
alphas
```




    ['A',
     'B',
     'C',
     'D',
     'e',
     'f',
     'g',
     'h',
     'i',
     'j',
     'k',
     'l',
     'm',
     'n',
     'o',
     'p',
     'q',
     'r',
     's',
     't',
     'u',
     'v',
     'w',
     'x',
     'y',
     'z']




```python
alphas[:4] = []
```


```python
alphas
```




    ['e',
     'f',
     'g',
     'h',
     'i',
     'j',
     'k',
     'l',
     'm',
     'n',
     'o',
     'p',
     'q',
     'r',
     's',
     't',
     'u',
     'v',
     'w',
     'x',
     'y',
     'z']



## Deleting list elements
- del statement removes an element from a list given its index


```python
alphas
```




    ['e',
     'f',
     'g',
     'h',
     'i',
     'j',
     'k',
     'l',
     'm',
     'n',
     'o',
     'p',
     'q',
     'r',
     's',
     't',
     'u',
     'v',
     'w',
     'x',
     'y',
     'z']




```python
del alphas[0]
```


```python
alphas
```




    ['f',
     'g',
     'h',
     'i',
     'j',
     'k',
     'l',
     'm',
     'n',
     'o',
     'p',
     'q',
     'r',
     's',
     't',
     'u',
     'v',
     'w',
     'x',
     'y',
     'z']




```python
del alphas[26]
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-73-80e1a19bb44c> in <module>
    ----> 1 del alphas[26]
    

    IndexError: list assignment index out of range



```python
alphas.index('z')
```




    20




```python
alphas.index(alphas[-1])
```




    20




```python
del alphas[1:3]
```


```python
alphas
```




    ['f',
     'i',
     'j',
     'k',
     'l',
     'm',
     'n',
     'o',
     'p',
     'q',
     'r',
     's',
     't',
     'u',
     'v',
     'w',
     'x',
     'y',
     'z']




```python
indexOfZ = alphas.index('z')
del alphas[indexOfZ]
```


```python
print(alphas)
```

    ['f', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']


## Objects and references
- **is** operator can be used to test if two objects are referencing the same memory location
    - meaning they're essentially the same object with the same values


```python
# even though a and b are two separate objects is still evaluates to True
a = 'apple'
b = 'apple'
a is b
```




    True




```python
# even though c and d are two separate objects is still evaluates to True
c = 10
d = 10
c is d
```




    True




```python
# what about tuple?
e = (1, 2)
f = (1, 2)
print(e == f)
print(e is f)
```

    True
    False



```python
# What about lists?
l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 == l2)
print(l1 is l2)
```

    True
    False


## Copying lists (Shallow copy vs Deep copy)
- see [PythonTutor.com to visualize aliasing](http://pythontutor.com/visualize.html#code=import%20copy%0A%0Aa%20%3D%20%5B1,%20%5B2,%203%5D%5D%0Ab%20%3D%20a%0Ac%20%3D%20a.copy%28%29%0Ad%20%3D%20a%5B%3A%5D%0Af%20%3D%20copy.deepcopy%28a%29&cumulative=false&curInstr=0&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)
- assignment *=* operator does shallow copy


```python
a = [1, 2, 3]
b = a
print(a is b)
print(a == b)
```

    True
    True



```python
b[0] = 10
print(a)
print(b)
```

    [10, 2, 3]
    [10, 2, 3]



```python
# How do you actually clone lists - do a deep copy?
c = a[:] # easy way shallow copy
d = a.copy() # shallow copy
import copy
e = copy.deepcopy(b)
```


```python
c is a
```




    False




```python
d is a
```




    False




```python
b is e
```




    False



## List methods
- list objects have a bunch methods that can be invoked to work with list
- run help(list)


```python
help(list)
```

    Help on class list in module builtins:
    
    class list(object)
     |  list(iterable=(), /)
     |  
     |  Built-in mutable sequence.
     |  
     |  If no argument is given, the constructor creates a new empty list.
     |  The argument must be an iterable if specified.
     |  
     |  Methods defined here:
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __contains__(self, key, /)
     |      Return key in self.
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
     |  __iadd__(self, value, /)
     |      Implement self+=value.
     |  
     |  __imul__(self, value, /)
     |      Implement self*=value.
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
     |  __mul__(self, value, /)
     |      Return self*value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __reversed__(self, /)
     |      Return a reverse iterator over the list.
     |  
     |  __rmul__(self, value, /)
     |      Return value*self.
     |  
     |  __setitem__(self, key, value, /)
     |      Set self[key] to value.
     |  
     |  __sizeof__(self, /)
     |      Return the size of the list in memory, in bytes.
     |  
     |  append(self, object, /)
     |      Append object to the end of the list.
     |  
     |  clear(self, /)
     |      Remove all items from list.
     |  
     |  copy(self, /)
     |      Return a shallow copy of the list.
     |  
     |  count(self, value, /)
     |      Return number of occurrences of value.
     |  
     |  extend(self, iterable, /)
     |      Extend list by appending elements from the iterable.
     |  
     |  index(self, value, start=0, stop=9223372036854775807, /)
     |      Return first index of value.
     |      
     |      Raises ValueError if the value is not present.
     |  
     |  insert(self, index, object, /)
     |      Insert object before index.
     |  
     |  pop(self, index=-1, /)
     |      Remove and return item at index (default last).
     |      
     |      Raises IndexError if list is empty or index is out of range.
     |  
     |  remove(self, value, /)
     |      Remove first occurrence of value.
     |      
     |      Raises ValueError if the value is not present.
     |  
     |  reverse(self, /)
     |      Reverse *IN PLACE*.
     |  
     |  sort(self, /, *, key=None, reverse=False)
     |      Sort the list in ascending order and return None.
     |      
     |      The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
     |      order of two equal elements is maintained).
     |      
     |      If a key function is given, apply it once to each list item and sort them,
     |      ascending or descending, according to their function values.
     |      
     |      The reverse flag can be set to sort in descending order.
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __hash__ = None
    



```python
a = []
a.append(1)
a.append(2)
a.append([2, 3])
```


```python
a
```




    [1, 2, [2, 3]]




```python
a.extend([3, 4])
```


```python
a
```




    [1, 2, [2, 3], 3, 4]




```python
a.append([5, 6])
```


```python
a
```




    [1, 2, [2, 3], 3, 4, [5, 6]]




```python
a.insert(0, 'hi')
```


```python
a
```




    ['hi', 1, 2, [2, 3], 3, 4, [5, 6]]




```python
a.reverse()
```


```python
a[0].reverse()
```


```python
a
```




    [[6, 5], 4, 3, [2, 3], 2, 1, 'hi']




```python
a.sort()
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-102-2ed0d7de6146> in <module>
    ----> 1 a.sort()
    

    TypeError: '<' not supported between instances of 'int' and 'list'



```python
# let's create a list of numbers in descending order to sort
blist = list(range(10, 0, -1))
```


```python
blist
```




    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]




```python
blist.sort()
```


```python
print(blist)
```

    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



```python
# sort blist in reverse/descending order
blist.sort(reverse=True)
```


```python
blist
```




    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]




```python
m = max(blist)
mI = blist.index(m)
```


```python
print(mI)
```

    0



```python
min(blist)
```




    1




```python
# how many 100s are in blist?
print(blist.count(100))
```

    0


## List applications

### convert a string to list of integers


```python
nums = input('Enter 5 numbers separated by space: ')
```

    Enter 5 numbers separated by space: 10 15 1 3 4



```python
nums
```




    '10 15 1 3 4'




```python
nums = nums.split(' ')
```


```python
nums
```




    ['10', '15', '1', '3', '4']




```python
intNums = []
for n in nums:
    intN = int(n)
    intNums.append(intN)
```


```python
intNums
```




    [10, 15, 1, 3, 4]




```python
intNums.sort(reverse=True)
```


```python
intNums
```




    [15, 10, 4, 3, 1]



### convert list of integers to string


```python
' '.join(intNums)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-9-0dd63a44d5ec> in <module>
    ----> 1 ' '.join(intNums)
    

    TypeError: sequence item 0: expected str instance, int found



```python
strNum = []
for n in intNums:
    strNum.append(str(n))
```


```python
strNum
```




    ['15', '10', '4', '3', '1']




```python
strNum = ' '.join(strNum)
```


```python
strNum
```




    '15 10 4 3 1'



## Passing list to function - passed-by-reference
- mutable types such as list are passed-by-reference 
- a reference/location is passed instead of a copy of the data


```python
def getData(someList):# someList is formal parameter
    for i in range(5):
        a = int(input('enter a number: '))
        someList.append(a)
```


```python
alist = []
getData(alist) # alist is actual parameter/argument
```

    enter a number: 100
    enter a number: 99
    enter a number: 75
    enter a number: 33
    enter a number: 13



```python
# when formal parameter is updated, actual parameter is also updated
alist
```




    [100, 99, 75, 33, 13]



### [visualize - pass-by-reference with pythontutor.com](http://pythontutor.com/visualize.html#code=def%20getData%28someList%29%3A%23%20someList%20is%20formal%20parameter%0A%20%20%20%20for%20i%20in%20range%285%29%3A%0A%20%20%20%20%20%20%20%20a%20%3D%20int%28input%28'enter%20a%20number%3A%20'%29%29%0A%20%20%20%20%20%20%20%20someList.append%28a%29%0A%0Aalist%20%3D%20%5B%5D%0AgetData%28alist%29%20%23%20alist%20is%20actual%20argument&cumulative=false&curInstr=0&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

## return list from functions
- lists can be returned from functions


```python
def getMaxMin(alist):
    m = max(alist)
    minVal = min(alist)
    return [m, minVal]
    
```


```python
alist = range(-1000, 2000000)
print(getMaxMin(alist))
```

    [1999999, -1000]



```python
assert getMaxMin(alist) == [1999999, -1000]
```

## Casting list into tuple and back
- since tuples are immutable it may be benefitial to cast them into lists and update
- can convert list back to tuple again


```python
atuple = (1, 2, 3)
alist = list(atuple)
print(alist)
```

    [1, 2, 3]



```python
btuple = tuple(alist)
```


```python
print(btuple)
```

    (1, 2, 3)



```python
atuple == btuple
```




    True




```python
# eventhough the elements are equal; the types of two objects are not
print(atuple, alist)
print(atuple == alist)
```

    (1, 2, 3) [1, 2, 3]
    False


## Exercises
1. Practice with the rest of the methods of list

2. Draw memory state snapshot for a and b after the following Python code is executed:

```python
a = [1, 2, 3]
b = a[:]
b[0] = 5
```

3. Lists can be used to represent mathematical vectors. Write a function `add_vectors(u, v)` that takes two lists of numbers of the same length, and returns a new list containing the sums of the corresponding elements of each. The following test cases must pass once the add_vectors is complete.


```python
def add_vectors(a, b):
    pass
```


```python
# test cases
assert add_vectors([1, 1], [1, 1]) == [2, 2], 'vectors not added correctly'
assert add_vectors([1, 2], [1, 4]) == [2, 6], 'vectors not added correctly'
assert add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4], 'vectors not added correctly'
```


    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    <ipython-input-27-f13d12d55331> in <module>
          1 # test cases
    ----> 2 assert add_vectors([1, 1], [1, 1]) == [2, 2], 'vectors not added correctly'
          3 assert add_vectors([1, 2], [1, 4]) == [2, 6], 'vectors not added correctly'
          4 assert add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4], 'vectors not added correctly'


    AssertionError: vectors not added correctly


## Kattis problems
- the following Kattis problems can be solved using list

- Culture Shock - https://open.kattis.com/problems/cultureshock
- Dice Game - https://open.kattis.com/problems/dicegame
- Height Ordering - https://open.kattis.com/problems/height
- What does the fox say? - https://open.kattis.com/problems/whatdoesthefoxsay
- Army Strength (Easy) - https://open.kattis.com/problems/armystrengtheasy
- Army Strength (Hard) - https://open.kattis.com/problems/armystrengthhard
- Black Friday - https://open.kattis.com/problems/blackfriday
- E-Clips - https://open.kattis.com/problems/eclips
- Exact Change - https://open.kattis.com/problems/exactchange
- Oddities - https://open.kattis.com/problems/oddities
    - Hint: use two loops, division and modulo
- Tic-Tac-Toe Solver - https://open.kattis.com/problems/tictactoesolver
    - Hint: 2-D List or List of strings - simply check 8 winning ways from each X or O char - just like in tic-tac-toe
- Sudoku Verify - https://open.kattis.com/problems/sudokuverify
    - Hint: 2-D List or List of strings - check rows, columns and 3x3 sub-grids for validity
- Alphabetical Aristocrats - https://open.kattis.com/problems/alphabeticalaristocrats
    - Hint: use list of tuple to store the actual name and name to sort and sort them using built-in sort method
### List sorting with two keys
- Roll Call - https://open.kattis.com/problems/rollcall
- Cooking Water - https://open.kattis.com/problems/cookingwater


```python

```
