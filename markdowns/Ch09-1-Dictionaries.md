# Dictionaries
<a href="https://colab.research.google.com/github/rambasnet/Python-Fundamentals/blob/master/notebooks/Ch09-1-Dictionaries.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

http://openbookproject.net/thinkcs/python/english3e/dictionaries.html

## Topics
- dictionary data types
- create and use dictionary
- dictionary methods and operations
- dictionary applications and problems


## Dictionary
- another compound type/container like lists and tuples
- very useful data structure/container that can store data as lookup table 
- Python's mapping type similar to `map` container, or associative arrays in C++ and other languages
- dictionaries maps keys (immutable type) to values of any type (heterogeneous)
- Python uses complex hash algorithm to index key for fast access
- starting from verion 3.6, Python dict remembers the orders of the elements inserted

## Creating dictionary objects


```python
eng2sp = {} # or
eng2sp1 = dict()
```


```python
print(eng2sp, eng2sp1)
```

    {} {}



```python
type(eng2sp)
```




    dict




```python
eng2sp["One"] = "uno"
eng2sp["two"] = "dos"
eng2sp["three"] = "tres"
eng2sp[4] = "quatro"
eng2sp["five"] = "sinco"
```


```python
eng2sp
```




    {'One': 'uno', 'two': 'dos', 'three': 'tres', 4: 'quatro', 'five': 'sinco'}




```python
key = 'Five'
eng2sp[key] = 'Sinco'
```


```python
print(eng2sp)
```

    {'One': 'uno', 'two': 'dos', 'three': 'tres', 4: 'quatro', 'five': 'sinco', 'Five': 'Sinco'}



```python
print(eng2sp['One'])
```

    uno



```python
symbolNames = {'*':'asterick', '+':"plus", '-': 'minus'}
```


```python
print(eng2sp, symbolNames)
```

    {'One': 'uno', 'two': 'dos', 'three': 'tres', 4: 'quatro', 'five': 'sinco', 'Five': 'Sinco'} {'*': 'asterick', '+': 'plus', '-': 'minus'}



```python
dict1 ={'one': 'uno', 'two': 'dos', 'three': 'tres', '4': 'quatro', 'five': 'sinco'}
```


```python
dict1
```




    {'one': 'uno', 'two': 'dos', 'three': 'tres', '4': 'quatro', 'five': 'sinco'}



## Accessing values
- use index operator ['key'] 
- dict object is mutable


```python
one = 'One'
```


```python
eng2sp[one]
```




    'uno'




```python
eng2sp
```




    {'One': 'uno',
     'two': 'dos',
     'three': 'tres',
     4: 'quatro',
     'five': 'sinco',
     'Five': 'Sinco'}




```python
key = 'ten'
value = 'diez'
eng2sp[key] = value
print(eng2sp['ten'])
```

    diez



```python
eng2sp['One'] = 'Uno'
```


```python
eng2sp
```




    {'One': 'Uno',
     'two': 'dos',
     'three': 'tres',
     4: 'quatro',
     'five': 'sinco',
     'Five': 'Sinco',
     'ten': 'diez'}




```python
eng2sp['One'] = ['uno']
```


```python
eng2sp['One'].append('Uno')
```


```python
eng2sp['One'].insert(0, 'UNO')
```


```python
print(eng2sp)
```

    {'One': ['UNO', 'uno', 'Uno'], 'two': 'dos', 'three': 'tres', 4: 'quatro', 'five': 'sinco', 'Five': 'Sinco', 'ten': 'diez'}



```python
adict = {1: ['uno', 'one'], 2:('two', 'dos'), 3:{'three':'tres'}}
```


```python
print(adict[2][1])
```

    dos



```python
# How do you access tres in adict?
print(adict[3]['three'])
```

    tres


## Dictionary methods


```python
help(dict)
```

    Help on class dict in module builtins:
    
    class dict(object)
     |  dict() -> new empty dictionary
     |  dict(mapping) -> new dictionary initialized from a mapping object's
     |      (key, value) pairs
     |  dict(iterable) -> new dictionary initialized as if via:
     |      d = {}
     |      for k, v in iterable:
     |          d[k] = v
     |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
     |      in the keyword argument list.  For example:  dict(one=1, two=2)
     |  
     |  Methods defined here:
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
     |  popitem(...)
     |      D.popitem() -> (k, v), remove and return some (key, value) pair as a
     |      2-tuple; but raise KeyError if D is empty.
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
     |  Class methods defined here:
     |  
     |  fromkeys(iterable, value=None, /) from builtins.type
     |      Create a new dictionary with keys from iterable and values set to value.
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
for k in eng2sp.keys(): # the keys are ordered based on their insertion order
    print("key {} maps to value {}".format(k, eng2sp[k]))
```

    key One maps to value ['UNO', 'uno', 0, 'Uno']
    key two maps to value dos
    key three maps to value tres
    key 4 maps to value quatro
    key five maps to value sinco
    key Five maps to value Sinco
    key ten maps to value diez



```python
print(list(eng2sp.keys()))
```

    ['One', 'two', 'three', 4, 'five', 'Five', 'ten']



```python
print(list(eng2sp.values()))
```

    [['UNO', 'uno', 'Uno'], 'dos', 'tres', 'quatro', 'sinco', 'Sinco', 'diez']



```python
# iterate over keys
for k in eng2sp:
    print('key = {} value = {}'.format(k, eng2sp.get(k)))
```

    key = One value = ['UNO', 'uno', 'Uno']
    key = two value = dos
    key = three value = tres
    key = 4 value = quatro
    key = five value = sinco
    key = Five value = Sinco
    key = ten value = diez



```python
# get method returns None if the key is not found
print(eng2sp.get('asdfsf'))
```

    None



```python
# can also return default value if key doesn't exist
print(eng2sp.get("Ondfe", '?'))
```

    ?



```python
# iterate over values
for val in eng2sp.values():
    print("value = ", val)
```

    value =  ['UNO', 'uno', 'Uno']
    value =  dos
    value =  tres
    value =  quatro
    value =  sinco
    value =  Sinco
    value =  diez



```python
values = list(eng2sp.values())
```


```python
values
```




    [['UNO', 'uno', 'Uno'], 'dos', 'tres', 'quatro', 'sinco', 'Sinco', 'diez']




```python
items = list(eng2sp.items())
```


```python
print(items)
```

    [('One', ['UNO', 'uno', 'Uno']), ('two', 'dos'), ('three', 'tres'), (4, 'quatro'), ('five', 'sinco'), ('Five', 'Sinco'), ('ten', 'diez')]



```python
dict2 = dict(items)
print(dict2)
```

    {'One': ['UNO', 'uno', 'Uno'], 'two': 'dos', 'three': 'tres', 4: 'quatro', 'five': 'sinco', 'Five': 'Sinco', 'ten': 'diez'}



```python
for k, v in eng2sp.items():
    print('{} -> {}'.format(k, v))
```

    One -> ['UNO', 'uno', 'Uno']
    two -> dos
    three -> tres
    4 -> quatro
    five -> sinco
    Five -> Sinco
    ten -> diez



```python
print(eng2sp.popitem())
print(eng2sp)
```

    ('ten', 'diez')
    {'One': ['UNO', 'uno', 'Uno'], 'two': 'dos', 'three': 'tres', 4: 'quatro', 'five': 'sinco', 'Five': 'Sinco'}


## Checking keys
- in and not in operators can be used to check if some keys exist in a given dictionary
- knowing if key exists helps automatically create dictionaries and access corresponding values


```python
"One" in eng2sp
```




    True




```python
"Ten" in eng2sp
```




    False




```python
"twenty" not in eng2sp
```




    True



## Copying dictionary objects
- shallow copy vs deep copy


```python
import copy
digits = {1: 'one', 2: 'two', 3: ['three', 'Three', 'THREE']}
digits1 = digits # creates an alias
digits2 = digits.copy() # shallow copy
digits3 = copy.deepcopy(digits) # deep copy
```

### [visualize in pythontutor.com](https://goo.gl/XmvYkB)


```python
from IPython.display import IFrame
src = '''
http://pythontutor.com/iframe-embed.html#code=import%20copy%0Adigits%20%3D%20%7B1%3A%20'one',%202%3A%20'two',%203%3A%20%5B'three',%20'Three',%20'THREE'%5D%7D%0Adigits1%20%3D%20digits%20%23%20creates%20an%20alias%0Adigits2%20%3D%20digits.copy%28%29%20%23%20shallow%20copy%0Adigits3%20%3D%20copy.deepcopy%28digits%29%20%23%20deep%20copy&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=false&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
'''
IFrame(src, width=900, height=600)
```





        <iframe
            width="900"
            height="600"
            src="
http://pythontutor.com/iframe-embed.html#code=import%20copy%0Adigits%20%3D%20%7B1%3A%20'one',%202%3A%20'two',%203%3A%20%5B'three',%20'Three',%20'THREE'%5D%7D%0Adigits1%20%3D%20digits%20%23%20creates%20an%20alias%0Adigits2%20%3D%20digits.copy%28%29%20%23%20shallow%20copy%0Adigits3%20%3D%20copy.deepcopy%28digits%29%20%23%20deep%20copy&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=false&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
"
            frameborder="0"
            allowfullscreen
        ></iframe>




## Passing dictionaries to functions
- dict is a mutable type
- therefore, dict objects are passed by reference


```python
# find the histogram (frequency of each unique character) in a word
def histogram(word, hist):
    for c in word:
        c = c.lower()
        if c in hist:
            hist[c] += 1
        else:
            hist[c] = 1
```


```python
h = {}
histogram('Mississippim', h)
for k, v in h.items():
    print(k, v)
```

    m 2
    i 4
    s 4
    p 2


## Returning dict from functions
- dict objects can be returned from functions


```python
def getHist(word):# = "Mississippi"
    h = {}
    for c in word:
        if c in h:
            h[c] += 1
        else:
            h[c] = 1
    return h
```


```python
hist = getHist('Mississippi')
print(hist)
if 'M' in hist:
    print('M is in histogram')
```

    {'M': 1, 'i': 4, 's': 4, 'p': 2}
    M is in histogram


## Exercises

1. Count and print letter frequency in a given word. Hint: use get method

2. Write a program that reads some text data and prints a frequency table of the letters in alphabetical order. Case should be ignored. A sample output of the program when the user enters the data "ThiS is String with Upper and lower case Letters", would look this:
<pre>
a  2
c  1
d  1
e  5
g  1
h  2
i  4
l  2
n  2
o  1
p  2
r  4
s  5
t  5
u  1
w  2
</pre>

## Kattis Problems 
- some of the problems that can be solved using dict data structure

- Qwerty - https://open.kattis.com/problems/qwerty
- Intervals - https://open.kattis.com/problems/intervals0
- I've Been Everywhere, Man -  https://open.kattis.com/problems/everywhere
- Seven Wonders - https://open.kattis.com/problems/sevenwonders
- ACM Contest Scoring - https://open.kattis.com/problems/acm
- Stacking Cups - https://open.kattis.com/problems/cups
- A New Alphabet - https://open.kattis.com/problems/anewalphabet
- Words for Numbers - https://open.kattis.com/problems/wordsfornumbers
- Babelfish - https://open.kattis.com/problems/babelfish
- Popular Vote - https://open.kattis.com/problems/vote
- Adding Words - https://open.kattis.com/problems/addingwords
- Grandpa Bernie - https://open.kattis.com/problems/grandpabernie
- Judging Troubles - https://open.kattis.com/problems/judging
- Not Amused - https://open.kattis.com/problems/notamused
- Engineering English - https://open.kattis.com/problems/engineeringenglish
- Hardwood Species - https://open.kattis.com/problems/hardwoodspecies
- Conformity - https://open.kattis.com/problems/conformity
- Galactic Collegiate Programming Contest - https://open.kattis.com/problems/gcpc
- Simplicity - https://open.kattis.com/problems/simplicity
- Dialling Digits - https://open.kattis.com/problems/diallingdigits
- Taking Inventory - https://open.kattis.com/problems/takinginventory
- Morse Numbers - https://open.kattis.com/problems/morsenumbers
- Morse Code Palindromes - https://open.kattis.com/problems/morsecodepalindromes


```python

```
