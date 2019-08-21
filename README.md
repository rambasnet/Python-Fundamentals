# FDS Python: Fundamentals and Data Structures with Python

These jupyter notebooks are based on open-source textbook How to Think Like a Computer Scientist: Learning with Python 3 (RLE) by Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers found online [here](http://openbookproject.net/thinkcs/python/english3e/index.html).

The primary goal of these notebooks is to help instructors easily adopt the open-source textbook to teach programming and problem solving using Python in an interactive and hands-on approach (a.k.a. learning-by-doing). Some new chapters with new and importanct concepts and topics have been added and some existing chapters have been slightly reordered. These notebooks primarily consist of outlines of theoritical concepts, kewwords and definitions along with code, [code visualization](https://pythontutor.com) compounded by interesting and challenging [intercollegiate programming contests problems](https://open.kattis.com) where applicable to help students engage in challenging concepts of coding and problem solving.

See paper.md for statement of need.

## Notebook mapping with corresponding book chapter

| Notebook ->                       | Think Python3 Textbook                                    |
| --------------------------------- | --------------------------------------------------------- |
| Ch00-TableOfContents              | Start here                                                |
| Ch01-Introduction                 | Chapter 1: The way of the program                         |
| Ch02-Data-Variables               | Chapter 2: Variables, expressions, and statements         |
| Ch03-1-Functions-Built-in         | Examples of some built-in functions                       |
| Ch03-2-Functions-Library          | Examples of standard libraries, e.g., math                |
| Ch03-3-Functions-UserDefined      | Chapter 4 and 6: Functions and Fruitful functions         |
| Ch04-Conditionals                 | Chapter 5: Conditionals                                   |
| Ch05-Iterations                   | Chapter 7: Iteration - for and while loops                |
| Ch06-Strings                      | Chapter 8: Strings                                        |
| Ch07-Tuples                       | Chapter 9: Tuples                                         |
| Ch08-1-Lists                      | Chapter 11: Lists                                         |
| Ch08-2-Lists-Comprehension-Lambda | List comprehension, Lambda functions, map, reduce, filter |
| Ch09-1-Dictionaries               | Chapter 20: Dictionaries                                  |
| Ch09-2-Dictionaries-Advanced      | zip, OrderedDict                                          |
| Ch10-Files                        | Chapter 13: Files - with, open, binary, urllib            |
| Ch11-Turtles-Events               | Chapter 3 & 10                                            |
| Ch12-Modules                      | Chapter 12: Modules - built-in and user-defined           |
| Ch13-Recursion                    | Chapter 18: Recursion                                     |
| Ch14-OOP                          | Chapter 15, 16 Classes and Basics                         |
| Ch15-Overloading-Polymorphism     | Chapter 21 and 22                                         |
| Ch16-Exceptions                   | Chapter 19 Exceptions                                     |
| Ch17-PyGame                       | Chapter 17 PyGame                                         |
| Ch18-Inheritence                  | Chapter 23 Inheritance                                    |
| Ch19-UnitTest                     | UnitTest Framework                                        |
| Ch20-Memoization-Optimization     | Basics of Dynamic Programming                             |
| Ch21-SqliteDB                     | Intro to Sqlite3 Database                                 |
| Ch22-LinkedLists                  | Chapter 24 Linked Lists                                   |
| Ch23-Stacks                       | Chapter 25 Stacks                                         |
| Ch24-Queues                       | Chapter 26 Queues                                         |
| Ch25-Trees                        | Chapter 27 Trees                                          |

## Who can use these notebooks

### University and High-school Coding Instructors

Depending on the course level and topics covered, instructors can pick and choose appropriate chapters. E.g., we've used Chapter 1 - 15 (skipping some chapters such as Functions-Lambda) in Beginning programing 3/4-credit university courses (CS0 and CS1) where students have no prior experience to programming. On the other hand, we've also used all the chapters for 2-credit advanced programing courses where students have some prior programming experiences in Python or other programming languages (CS1, CS2 level).

### Self learners

Depending on their skill and interest level, learners can move as swiftly as appropriate through the chapters. Try solving some exercises towards the end of each chapter before moving on for self-assessment of the mastery of the materials.

## How to use these notebooks

### Important

In order to learn coding, it's very important to actually type code on your own from scratch and NOT copy paste! You can run provided cells to see the output, follow along and learn from it but it's important that you either start a new notebook or add cells and write your own code from scratch to practice the concepts covered with many similar examples and solve the exercises provided.

### Online service

You can launch an interactive session of this project using online Binder service:
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/rambasnet/thinkpythonnotebooks/master) or Google Colab. Each chapter, where applicable, provides [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com) to simply click and run the notebook in Google's Colab environment.

### On a local system

To run these notebooks interactively and save your work locally, you need <a href="https://www.python.org/" target="_blank">Python 3</a> and <a href="http://jupyter.org/" target="_blank"> Jupyter Notebook </a> -- an interactive web-based editor that allows you to create and share documents that contain live code and data. Anaconda or Miniconda is the recommended way to install Python and other packages on all modern platforms.

#### Installing via Anaconda or Miniconda

Anaconda or Miniconda has Python 3 and many other packages that you can easily install on any platform (Windows, Linux, and Mac). First, install Anaconda: http://docs.continuum.io/anaconda/install/ or Miniconda https://conda.io/docs/user-guide/install/index.html

After installing anaconda or miniconda, open a terminal and run the following commands:

```
    conda update conda
    conda install notebook
```

#### Running the notebook server

Once Python 3 and Jupyter Notebook are installed, open a terminal change working directory using cd command to go into the folder where this repo is cloned and run the notebook from there:

```
    cd <directory where this repo is cloned>
    jupyter notebook
```

This will start a Jupyter session in your browser. Open Ch00-TableOfContents notebook and start there or open any chapter and start coding...

## Contributing

Contributions are accepted via pull requests. You can also open issues on bugs, typos or any corrections and suggest improvements on the notebooks.

## Copyright and License

&copy; 2019 Ram Basnet and T. Doleck. Permission is granted to copy, distribute and/or modify this document
under the terms of the GNU Free Documentation License, Version 1.3
or any later version published by the Free Software Foundation. See LICENSE file for details.
