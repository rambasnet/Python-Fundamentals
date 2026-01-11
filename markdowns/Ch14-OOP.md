# Object Oriented Programming (OOP)
<a href="https://colab.research.google.com/github/rambasnet/Python-Fundamentals/blob/master/notebooks/Ch14-OOP.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>


http://openbookproject.net/thinkcs/python/english3e/classes_and_objects_I.html
http://openbookproject.net/thinkcs/python/english3e/classes_and_objects_II.html

- we've been using procedural programming paradigm; focus on functions/procedures
- OOP paradigm is best used in large and complex modern software systems 
    - OOD (Object Oriented Design) makes it easy to maintain and improve software over time
- focus is on creation of objects which contain both data and functionality together under one name
- typically, each class definition corresponds to some object or concept in the real world with some attributes/properties that maintain its state; and the functions/methods correspond to the ways real-world objects interact

## class
- we've used classes like str, int, float, dict, tuple, etc.
- class keyword lets programmer define their own compound data types
- class is a collection of relevant attributes and methods like real world objects
- syntax:
```
class className:
    [statement-1]
    .
    .
    [statement-N]
```

### a simple Point class
- a class that represents a point in 2-D coordinates


```python
# OK but NOT best practice!
class Point:
    pass
```


```python
# instantiate an object a of type Point
a = Point()
```


```python
type(a)
```


```python
a.x = 0 # dynamically attach attriutes
a.y = 0
print(a.x, a.y)
```


```python
b = Point()
```


```python
b.x
```

### better class example
- with constructor and destructor methods, class attribute and object attributes


```python
class Point:
    """
    Point class to represent and manipulate x and y in 2D coordinates
    """
    count = 0 # class variable/attribute
    
    # constructor to customize the initial state of an object
    # first argument refers to the instance being manipulated;
    # it is customary to name this parameter self; but can be anything
    def __init__(self, xx=0, yy=0):
        """Create a new point with given x and y coords"""
        # x and y are object variables/attributes
        self.x = xx
        self.y = yy
        Point.count += 1 # increment class variable
        
    
    # destructor 
    def __del__(self):
        Point.count -= 1
```


```python
print(Point.count)
```

## class members
- like real world objects, object instances can have both attributes and methods
    - attributes are properties that store data/values
    - methods are operations that operate on or use data/values
- use . dot notation to access members
- `x` and `y` are attributes of Point class
- `__init__()` (constructor) and `__del__()` (destructor) are sepcial methods
    - more on speical methods later
- can have as many relevant attributes and methods that help mimic real-world objects


```python
a = Point()
```


```python
print(a.x, a.y)
```


```python
b = Point(10, 10)
```


```python
print(b.x, b.y)
```


```python
Point.count
```


```python
print(a)
```

    <__main__.Point object at 0x7f850fddcfa0>



```python
# instantiate an object
def someFunction():
    p = Point()
    # what is the access specifier for attributes?
    print('p: x = {} and y = {}'.format(p.x, p.y))
    print("Total point objects = {}".format(Point.count)) # access class variable outside class
    p.__del__() # call destructor explictly
    p1 = Point(10, 100)
    print("p1: x = {} and y = {}".format(p1.x, p1.y))
    print("Total point objects = {}".format(Point.count))

    # Run this cell few times and see the value of Point.count
    # How do you fix this problem? Use __del__ destructor method.

```


```python
someFunction()
```

    p: x = 0 and y = 0
    Total point objects = 3
    p1: x = 10 and y = 100
    Total point objects = 4



```python
print("Total point objects = {}".format(Point.count))
```

    Total point objects = 2



```python
p = Point()
# what is the access specifier for attributes?
print('p: x = {} and y = {}'.format(p.x, p.y))
print("Total point objects = {}".format(Point.count)) # access class variable outside class
#p.__del__() # call destructor explictly
p1 = Point(10, 100)
print("p1: x = {} and y = {}".format(p1.x, p1.y))
print("Total point objects = {}".format(Point.count))
```

    p: x = 0 and y = 0
    Total point objects = 3
    p1: x = 10 and y = 100
    Total point objects = 4



```python
# let's print objects
print(p, p1)
# not very useful info!
```

    <__main__.Point object at 0x7f850fe356c0> <__main__.Point object at 0x7f850fe097b0>


### visualizing class and instance attributes using pythontutor.com
- https://goo.gl/aGuc4r

### exercise: add a method dist_from_origin() to Point class
- computes and returns the distance from the origin
- test the methods
- provides `__str__` overloaded method to represent objects as string
    - helps in printing objects


```python
def dist_from_origin(self):
    import math
    dist = math.sqrt(self.x**2+self.y**2)
    return dist
```


```python
print(dist_from_origin(p1))
```

    100.4987562112089



```python
class Point:
    """
    Point class represents and manipulates x,y coords
    """
    count = 0
    
    def __init__(self, xx=0, yy=0):
        """Create a new point with given x and y coords"""
        self.x = xx
        self.y = yy
        Point.count += 1
        
    def dist_from_origin(self):
        import math
        dist = math.sqrt(self.x**2+self.y**2)
        return dist
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    # destructor 
    def __del__(self):
        Point.count -= 1
```


```python
p1 = Point(2, 2)
print(p1.dist_from_origin())
```

    2.8284271247461903



```python
p2 = Point(10, 200)
```


```python
p2.dist_from_origin()
```




    200.24984394500785




```python
# let's print p1 object
print(p1)
```

    (2, 2)


## objects are mutable
- can change the state or attributes of an object


```python
p2 = Point(3, 2)
print(p2)
p2.x = "sasf"
p2.y = 10
print(p2)
```

### better approach to change state/attribute is via methods

- move(xx, yy) method is added to class to set new x and y values for a point objects

### Member access specifiers

- Python doesn't support `private`, `public`, `protected` specifiers provided by C++, Java, etc.
- all the members are public by default
- however, you can use leading single `_` and double `__` underscores "convention" to treat members as private 


```python
class Point:
    """
    Point class represents and manipulates x and y coordinates
    """
    
    def __init__(self, xx=0, yy=0):
        """Create a new point with given x and y coords"""
        """_x and _y are protected method"""
        
        self._x = xx
        self._y = yy
        
    def dist_from_origin(self):
        import math
        dist = math.sqrt(self._x**2+self._y**2)
        return dist
    
    def __str__(self): # string representation of the class; useful in printing objects
        return f"({self._x}, {self._y})"
    
    # define getter method to get x
    def getX(self):
        if not self._x:
            return 0
        return self._x
    
    # better syntax
    @property
    def x(self):
        return self._x
    
    # use setters to set attributes
    def setX(self, xx):
        if isinstance(xx, int) or isinstance(xx, float):
            self._x = int(xx)
        elif isinstance(xx, str):
            if xx.isnumeric():
                self._x = int(xx)
                
    # better syntax for setter
    @x.setter
    def x(self, xx: int):
        self.setX(xx)
        
    @property
    def y(self):
        return self._y
        
    @y.setter
    def y(self, yy: int):
        if isinstance(yy, int) or isinstance(yy, float):
            self._y = int(yy)
        elif isinstance(yy, str):
            if yy.isnumeric():
                self._y = int(yy)

    
    def move(self, xx, yy):
        self.x = xx
        self.y = yy
```


```python
p3 = Point()
print(p3)
p3.move(10, 20)
print(p3)
```

    (0, 0)
    (10, 20)



```python
p3.move("a", 2)
```


```python
print(p3)
```

    (10, 2)


## Operator Overloading

- https://docs.python.org/3/reference/datamodel.html
- Python lets you overload special operators (e.g., +, -, /, //, %, etc.) for your class
- Goal is to make your class as easy and seamless to use as possible



```python
class Point:
    """
    Point class represents and manipulates x and y coordinates
    """
    
    def __init__(self, xx=0, yy=0):
        """Create a new point with given x and y coords"""
        """_x and _y are protected method"""
        
        self._x = xx
        self._y = yy
        
    def dist_from_origin(self):
        import math
        dist = math.sqrt(self._x**2+self._y**2)
        return dist
    
    def __str__(self): # string representation of the class; useful in printing objects
        return f"({self._x}, {self._y})"
    
    @property
    def x(self):
        if not self._x:
            return 0
        return self._x
    
    @x.setter
    def x(self, xx: int):
        if isinstance(xx, int) or isinstance(xx, float):
            self._x = int(xx)
        elif isinstance(xx, str):
            if xx.isnumeric():
                self._x = int(xx)
        
    @property
    def y(self):
        return self._y
        
    @y.setter
    def y(self, yy: int):
        if isinstance(yy, int) or isinstance(yy, float):
            self._y = int(yy)
        elif isinstance(yy, str):
            if yy.isnumeric():
                self._y = int(yy)

    
    def move(self, xx, yy):
        self.x = xx
        
    def __add__(self, other: "Point"):
        """Overload + operator"""
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Point(new_x, new_y)
    
    
    def __eq__(self, other: "Point"):
        return self.x == other.x and self.y == other.y
```


```python
p1 = Point(2, 4)
p2 = Point(3, 5)
p3 = p1+p2
print(p3)
```

    (5, 9)



```python
assert p1 != p2
```


```python
assert p1 == p2
```


    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    Cell In[25], line 1
    ----> 1 assert p1 == p2


    AssertionError: 


## sameness - alias or deep copy


```python
import copy
p2 = Point(3, 4)
p3 = p2 # alias or deepcopy?
print(p2 is p3) # checks if two references refer to the same object
p4 = copy.deepcopy(p2)
print(p2 is p4)
```

## Passing objects as arguments to functions


```python
def print_point(pt: Point):
    pt.x = 100
    pt.y = 100
    print(pt)
```


```python
p = Point(10, 10)
print_point(p)
```


```python
print(p)
```

## are objects passed by value or reference?
- how can you tell?
- write a simple program to test.

## returning object instances from functions
- object(s) can be returned from functions


```python
def midpoint(p1, p2):
    """Returns the midpoint of points p1 and p2"""
    mx = (p1.getX() + p2.getX())//2
    my = (p1.getY() + p2.getY())//2
    return Point(mx, my)
```


```python
p = Point(4, 6)
q = Point(6, 4)
r = midpoint(p, q)
#print_point(r) # better way to do this: use __str__() special method
print(r)
```

exercise 1: In-class demo: Design a class to represent a triangle and implement methods to calculate area and perimeter.


## Composition
- class can include another class as a member
- let's say we want to represent a rectangle in a 2-D coordinates (XY plane)
- corner represents the top left point on a XY plane


```python
class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return  "({0}, {1}, {2})".format(self.corner, self.width, self.height)

```


```python
box = Rectangle(Point(0, 0), 100, 200)
bomb = Rectangle(Point(100, 80), 5, 10)    # In my video game
print("box: ", box)
print("bomb: ", bomb)
```

## Copying objects
- can be challenging as assigning one object to another simply creates an alias
    - does shallow copy
- use `deepcopy` for the proper copy of objects


```python
r1 = Rectangle(Point(1, 1), 10, 5)
r2 = copy.copy(r1)
```


```python
# r1 is not r2
r1 is r2
```


```python
# but two corners are same
r1.corner is r2.corner
```


```python
# let's test alias by moving r1 to a different location
r1.corner.move(10, 10)
```


```python
# you can see r2 is moved to that location as well
print(r1)
print(r2)
```


```python
# fix: use deepcopy from copy module
r3 = copy.deepcopy(r1)
```


```python
r1 is r3
```


```python
print(r1, r3)
```


```python
r1.corner.move(20, 20)
# r1 is moved but not r3
print(r1, r3)
```

## Class method types
- there are three types of methods: `instance methods`, `class methods` and `static methods`

- Python provides `@classmethod` and `@staticmethod` function decorators
- `object/instance` methods take `self` (notational) or some parameter as the first argument that points to the instance
    - which can then be used to act on instance data
    - instance methods can freely access attributes and other methods on the same object
    - intance methods are typical member functions
    
- class methods take class name (as a variable) as the first argument
    - don't need instances; the class name is itself is used
    - ususally `cls` or some parameter is used as the first argument that points to the class
    - class method can only access and modify class attributes (state)
    
- static methods are much like `static` keyword in Java
    - mainly contain logic pertaining to the class without the need for specific instance data
    - static methods takes neither `self` nor `cls`
    - can't acess both object attributes (state) and class attributes (state)
    
- for details: https://realpython.com/instance-class-and-static-methods-demystified/


```python
# Simple demo
class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'
    
```


```python
c = MyClass()
```


```python
c.method()
```


```python
MyClass.classmethod()
```


```python
MyClass.staticmethod()
```


```python
class Grades:
    def __init__(self, grades):
        self.grades = grades

    @classmethod
    def from_csv(cls, grade_csv_str):
        grades = list(map(int, grade_csv_str.split(',')))
        cls.validate(grades)
        return cls(grades)


    @staticmethod
    def validate(grades):
        for g in grades:
            if g < 0 or g > 100:
                raise Exception()

```


```python
try:
    # Try out some valid grades
    class_grades_valid = Grades.from_csv('90,80,85,94,70')
    print('Got grades:', class_grades_valid.grades)

    # Should fail with invalid grades
    class_grades_invalid = Grades.from_csv('92,-15,99,101,77,65,100')
    print(class_grades_invalid.grades)
except:
    print('Invalid!')
```


```python
# class_grades_valid object is created from valid grades
print('Got grades:', class_grades_valid.grades)
```


```python
# because of exception due to invalid grades, class_grades_invalid object is never created
print(class_grades_invalid.grades)
```

## Kattis Problems

- Premier Leagure Table - https://open.kattis.com/problems/premierleague
    - Hint: use class to represent each team with relevant attributes and methods


