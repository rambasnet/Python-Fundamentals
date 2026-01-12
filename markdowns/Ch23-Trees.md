# Trees
<a href="https://colab.research.google.com/github/rambasnet/Python-Fundamentals/blob/master/notebooks/Ch23-Trees.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

## External Resources
- Think Python - [http://openbookproject.net/thinkcs/python/english3e/trees.html](http://openbookproject.net/thinkcs/python/english3e/trees.html)


## Overview

- like linked lists, trees are made up of nodes or objects that contain data and references to other nodes
- unlike linked lists, trees can have multiple references to other nodes
- trees are hierarchical data structures that are used to represent relationships between data items
- trees are widely used in computer science for various applications such as searching, sorting, and organizing data
- common types of trees include binary trees, binary search trees, AVL trees, and B-trees, etc.

## Binary Tree
 - is a commonly used tree in which each node contains a reference to atmost two other nodes (possibly None)
- these references are referred to as the left and right subtrees
- like the node of linked list, each node also contains data/cargo
- like linked lists, trees are recursive data structures that are defined recursively:
    1. the empty tree, represented by None, or
    2. a node that contains a data and two tree references (left and right subtree)
- the topmost node in the tree is called the root node
- nodes with no children are called leaf nodes
- nodes that are not leaf nodes are called internal nodes
- the height of a tree is the length of the longest path from the root to a leaf
- trees can be traversed in different ways such as inorder, preorder, and postorder traversal

## Building trees
- similar to building linked-list


```python
class Tree:
    def __init__(self, data, left=None, right=None):
        self.cargo = data
        self.left = left
        self.right = right
        
    def __str__(self):
        return "{}".format(self.cargo)
    
```

### bottom-up way to build-trees
- first create children and link them to the parent


```python
left = Tree(2)
right = Tree(3)
tree = Tree(1, left, right)
```


```python
tree1 = Tree(10, Tree(20), Tree(30))
```


```python
print(tree)
```

    1



```python
print(tree1)
```

    10


## traversing tree

- natural way to traverse a tree is recursively!
- for each node, visit the node and then recursively visit its left and right subtrees
- three common ways to traverse a binary tree:
    - inorder traversal
    - preorder traversal
    - postorder traversal
- each traversal visits the nodes in a different order and is useful for different applications



```python
def findSum(tree):
    if not tree:
        return 0
    return tree.cargo + findSum(tree.left) + findSum(tree.right)
    
```


```python
findSum(tree)
```




    6




```python
findSum(tree1)
```




    60



## Expression trees
- trees are natural way to represent the structure of an expression unambigigously.
- infix expression 1 + 2 * 3 is ambigious unless we know the order of operation that * happens before +
- we can use tree to represent the same expression
    - operands are leaf nodes
    - operator nodes contain references to their operands; operators are binary (two operands)
    
<img src="./resources/tree2.png" />

- applications:
    - translate expressions to postfix, prefix, and infix
    - compilers use expression trees to parse, optimize, and translate programs
    
- three ways to traverse trees: pre-order, in-order and post-order


```python
expression = Tree('+', Tree(1), Tree('*', Tree(2), Tree(3)))
```

### pre-order tree traversal

- contents of the root appear before the contents of the children
- recursive algorithm:
    - visit the node
    - visit left subtree 
    - visit right subtree



```python
def preorder(tree):
    if not tree:
        return
    print(tree.cargo, end=' ')
    preorder(tree.left)
    preorder(tree.right)
    
```


```python
preorder(expression)
```

    + 1 * 2 3 

### in-order tree traversal
- contents of the tree appear in order
- recursive algorithm:
    - visit left subtree
    - visit node
    - visit right subtree


```python
def inorder(tree):
    if not tree:
        return
    inorder(tree.left)
    print(tree.cargo, end=' ')
    inorder(tree.right)
```


```python
inorder(expression)
```

    1 + 2 * 3 


```python
def inorderIndented(tree, level=0):
    if not tree:
        return
    inorderIndented(tree.right, level+1)
    print('   '*level + str(tree.cargo))
    inorderIndented(tree.left, level+1)
```


```python
inorderIndented(expression)
```

          3
       *
          2
    +
       1


### post-order traversal
- recursive algorithm:
    1. visit left subtree
    2. visit right subtree
    3. visit node


```python
def postorder(tree):
    if not tree:
        return
    postorder(tree.left)
    postorder(tree.right)
    print(tree.cargo, end=' ')
```


```python
postorder(expression)
```

    1 2 3 * + 

## building an expression tree
- parse an infix expression and build the corresponding expression tree
- e.g., (3 + 7) * 9 yields the following tree:
<img src="./resources/tree3.png">

1. tokenize expression into python list? How (left as an exercise)
 - (3 + 7) * 9 = ["(", 3, "+", 7, ")", "*", 9, "end"]
2. "end" token is useful for preventing the parser from reading pas the end of the list


```python
def get_token(token_list, expected):
    if token_list[0] == expected:
        del token_list[0]
        return True
    return False
```


```python
# handles operands
def get_number(token_list):
    x = token_list[0]
    if not isinstance(x, int):
        return None
    del token_list[0]
    return Tree(x, None, None) # leaf node
```


```python
token_list = [9, 11, 'end']
x = get_number(token_list)
postorder(x)
```

    9 


```python
print(token_list)
```

    [11, 'end']



```python
def get_product(token_list):
    a = get_number(token_list)
    if get_token(token_list, '*'):
        b = get_number(token_list)
        return Tree('*', a, b)
    return a
```


```python
token_list = [9, '*', 11, 'end']
tree = get_product(token_list)
```


```python
postorder(tree)
```

    9 11 * 


```python
token_list = [9, '+', 11, 'end']
tree = get_product(token_list)
postorder(tree)
```

    9 


```python
# adapt the function for compound product such as 3 * (5 * (7 * 9))
def get_product(token_list):
    a = get_number(token_list)
    if get_token(token_list, '*'):
        b = get_product(token_list)
        return Tree('*', a, b)
    return a
```


```python
token_list = [2, "*", 3, "*", 5 , "*", 7, "end"]
tree = get_product(token_list)
postorder(tree)
```

    2 3 5 7 * * * 


```python
#  a sum can be a tree with + at the root, a product on the left, and a sum on the right. 
# Or, a sum can be just a product.
def get_sum(token_list):
    a = get_product(token_list)
    if get_token(token_list, "+"):
        b = get_sum(token_list)
        return Tree("+", a, b)
    return a
```


```python
token_list = [9, "*", 11, "+", 5, "*", 7, "end"]
tree = get_sum(token_list)
```


```python
postorder(tree)
```

    9 11 * 5 7 * + 


```python
# handle parenthesis
def get_number(token_list):
    if get_token(token_list, "("):
        x = get_sum(token_list)         # Get the subexpression
        get_token(token_list, ")")      # Remove the closing parenthesis
        return x
    else:
        x = token_list[0]
        if not isinstance(x, int):
            return None
        del token_list[0]
        return Tree(x, None, None)
```


```python
# 9 * (11 + 5) * 7
token_list = [9, "*", "(", 11, "+", 5, ")", "*", 7, "end"]
tree = get_sum(token_list)
postorder(tree)
```

    9 11 5 + 7 * * 

## handling errors on malformed expressions


```python
# handle parenthesis
def get_number(token_list):
    if get_token(token_list, "("):
        x = get_sum(token_list)         # Get the subexpression
        if not get_token(token_list, ")"): # Remove the closing parenthesis
            raise ValueError('Missing close parenthesis!')
        return x
    else:
        x = token_list[0]
        if not isinstance(x, int):
            return None
        del token_list[0]
        return Tree(x, None, None)
```


```python
token_list = [9, "*", "(", 11, "+", 5, "*", 7, "end"]
tree = get_sum(token_list)
postorder(tree)
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-55-4140410c22b2> in <module>()
          1 token_list = [9, "*", "(", 11, "+", 5, "*", 7, "end"]
    ----> 2 tree = get_sum(token_list)
          3 postorder(tree)


    <ipython-input-47-840e89a9fc06> in get_sum(token_list)
          2 # Or, a sum can be just a product.
          3 def get_sum(token_list):
    ----> 4     a = get_product(token_list)
          5     if get_token(token_list, "+"):
          6         b = get_sum(token_list)


    <ipython-input-45-dc9c6c17cd73> in get_product(token_list)
          2     a = get_number(token_list)
          3     if get_token(token_list, '*'):
    ----> 4         b = get_product(token_list)
          5         return Tree('*', a, b)
          6     return a


    <ipython-input-45-dc9c6c17cd73> in get_product(token_list)
          1 def get_product(token_list):
    ----> 2     a = get_number(token_list)
          3     if get_token(token_list, '*'):
          4         b = get_product(token_list)
          5         return Tree('*', a, b)


    <ipython-input-54-e5973ec52d85> in get_number(token_list)
          4         x = get_sum(token_list)         # Get the subexpression
          5         if not get_token(token_list, ")"): # Remove the closing parenthesis
    ----> 6             raise ValueError('Missing close parenthesis!')
          7         return x
          8     else:


    ValueError: Missing close parenthesis!


## exercises:

1. Modify inorder function so that it puts parentheses around every operator and pair of operands. Is the output correct and unambiguous? Are the parentheses always necessary?

2. Write a function that takes an expression string and returns a token list.

3. Find other places in the expression tree functions where errors can occur and add appropriate raise statements. Test your code with improperly formed expressions.


```python

```
