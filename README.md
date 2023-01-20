# FDS Python: Fundamentals and Data Structures with Python

These jupyter notebooks are based on open-source textbook "How to Think Like a Computer Scientist: Learning with Python 3 (RLE)" by Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers found online [here](http://openbookproject.net/thinkcs/python/english3e/index.html).

The primary goal of these notebooks is to help instructors easily adopt the open-source textbook to teach programming and problem solving using Python in an interactive and hands-on approach (a.k.a. learning-by-doing). Some new chapters with important concepts and topics have been added and some existing chapters have been slightly reordered. These notebooks primarily consist of outlines of theoritical concepts, keywords and definitions along with code, [code visualization](https://pythontutor.com) compounded by appropriately challenging [intercollegiate programming contests problems](https://open.kattis.com) where applicable to help students engage in the challenging concepts of coding and problem solving.

See [paper.md](paper.md) file for statement of need.

## Notebook mapping with corresponding book chapter

Note: If book chapter is missing, texbook doesn't provide one on the topic

| Notebook -> | Think Python3 Textbook |
| ---------   | ---------- |
| [Ch01-Introduction](Ch01-Introduction.ipynb) | Chapter 1: The way of the program |
| [Ch02-1-Data, Variables, Std IO](Ch02-1-Data-Variables-StdIO.ipynb) | Chapter 2: Data, Variables and Standard IO |
| [Ch02-2-BitwiseOperators](Ch02-2-BitwiseOperators.ipynb) | Number Systems & Bitwise Operators |
| [Ch03-1-Functions-Built-in](Ch03-1-Functions-Built-in.ipynb) | Examples of some built-in functions |
| [Ch03-2-Functions-Library](Ch03-2-Functions-Library.ipynb) | Examples of standard libraries, e.g., math                |
| [Ch03-3-Functions-UserDefined](Ch03-3-Functions-UserDefined.ipynb)| Chapter 4 and 6: Functions and Fruitful functions |
| [Ch03-4-Functions-Advanced](Ch03-4-Functions-Advanced.ipynb) | Some advanced topics on function |
| [Ch04-Conditionals](Ch04-Conditionals.ipynb) | Chapter 5: Conditionals  |
| [Ch05-Iterations](Ch05-Iterations.ipynb) | Chapter 7: Iteration - for and while loops |
| [Ch06-Strings](Ch06-Strings.ipynb) | Chapter 8: Strings |
| [Ch07-Tuples](Ch07-Tuples.ipynb) | Chapter 9: Tuples |
| [Ch08-1-Lists](Ch08-1-Lists.ipynb) | Chapter 11: Lists  |
| [Ch08-2-Lists-Advanced](Ch08-2-Lists-Comprehension-Lambda.ipynb) | List comprehension, Lambda function, map, reduce, filter  |
| [Ch09-1-Dictionaries](Ch09-1-Dictionaries.ipynb) | Chapter 20: Dictionaries |
| [Ch09-2-Built-in-DataStructures](Ch09-2-Built-in-DataStructures.ipynb) | zip, set, Collections: OrderedDict, defaultdict, Counter  |
| [Ch10-1-Files](Ch10-1-Files.ipynb) | Chapter 13: Files - with, open, text file |
| [Ch10-2-Files-Advanced](Ch10-2-Files-Advanced.ipynb)  | Chapter 13: urllib, pickle, binary files, checksums  |
| [Ch11-Turtles-Events](Ch11-Turtles-Events.ipynb) | Chapter 3 & 10 |
| [Ch12-ModulesAndPackages](Ch12-Modules.ipynb) | Chapter 12: Modules - built-in and user-defined |
| [Ch13-Recursion](Ch13-Recursion.ipynb) | Chapter 18: Recursion  |
| [Ch14-OOP](Ch14-OOP.ipynb) | Chapter 15, 16 Classes and Basics  |
| [Ch15-Overloading-Polymorphism](Ch15-Overloading-Polymorphism.ipynb) | Chapter 21 and 22 |
| [Ch16-Exceptions](Ch16-Exceptions.ipynb) | Chapter 19 Exceptions  |
| [Ch17-PyGame](Ch17-PyGame.ipynb) | Chapter 17 PyGame |
| [Ch18-Inheritance](Ch18-Inheritance.ipynb) | Chapter 23 Inheritance |
| [Ch19-Unittest](Ch19-UnitTest.ipynb) | UnitTest Framework |
| [Ch20-LinkedLists](Ch20-LinkedLists.ipynb) | Chapter 24 Linked Lists |
| [Ch21-Stacks](Ch21-Stacks.ipynb) | Chapter 25 Stacks |
| [Ch22-Queues](Ch22-Queues.ipynb) | Chapter 26 Queues |
| [Ch23-Trees](Ch23-Trees.ipynb) | Chapter 25 Trees |
| [Ch24-CodeOptimization](Ch24-CodeOptimization-ExecutionTime.ipynb) | Code Optimization |
| [Ch25-DynamicProgramming](Ch25-DynamicProgramming.ipynb) | Intro to Dynamic Programming |
| [Ch26-Sqlite](Ch26-SqliteDB.ipynb) | Sqlite Database |

## PDF Format

- pdf version of all the notebooks can be found in [pdfs](https://github.com/rambasnet/Python-Notebooks/tree/master/pdfs) folder

## Who can use these notebooks

### University and High-school Coding Instructors

Depending on the course level and topics covered, instructors can pick and choose appropriate chapters. E.g., we've used Chapter 1 - 15 (skipping some chapters such as Functions-Lambda) in Beginning programing 3/4-credit university courses (CS0 and CS1) where students have no prior experience to programming. On the other hand, we've also used all the chapters for 2-credit advanced programing courses where students have some prior programming experiences in Python or other programming languages (CS1, CS2 level).

### Self learners

Depending on their skill and interest level, learners can move as swiftly as appropriate through the chapters. Try solving some exercises towards the end of each chapter before moving on to self-assess the mastery of the materials.

## How to use these notebooks

### Important

In order to learn coding, it's very important to actually type code on your own from scratch and NOT copy paste! You can run provided cells to see the output, follow along and learn from it. However, it's very important that you either start a new notebook or add cells and write your own code from scratch to practice the concepts covered with many similar examples and solve the exercises provided.

### Online services

You can launch an interactive session of this project using online Binder service:
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/rambasnet/thinkpythonnotebooks/master) or Google Colab. Each chapter, where applicable, provides [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com) to simply click and run the notebook in Google's Colab environment.

### On a local system

To run these notebooks interactively and save your work locally, you need [Python 3][https://www.python.org/] and [Jupyter Notebook](http://jupyter.org/) -- an interactive web-based editor that allows you to create and share documents that contain live code and data. Anaconda or Miniconda is the recommended way to install Python and other packages on all modern platforms.

#### Installing via Anaconda or Miniconda

Anaconda or Miniconda has Python 3 and many other packages that you can easily install on any platform (Windows, Linux, and Mac). First, install Anaconda: [http://docs.continuum.io/anaconda/install/](http://docs.continuum.io/anaconda/install/) or Miniconda [https://conda.io/docs/user-guide/install/index.html](https://conda.io/docs/user-guide/install/index.html) for Python 3.

After installing anaconda or miniconda, open a terminal or cmd prompt and run the following commands:

```bash
    conda update conda
    conda install notebook # or
    conda install -c conda-forge retrolab # uses notebook
```

#### Running the notebooks in VS Code

- Python notebooks can be run natively in VS Code. Simply open the notebook file with extension ipynb in VS Code and run each cell; add new cell, etc. right from VS Code.

#### Running the notebooks using jupyter notebook server

Once Python 3 and Jupyter Notebook are installed, open a terminal change working directory using cd command to go into the folder where this repo is cloned and run the notebook from there:

```bash
    cd <directory where this repo is cloned>
    jupyter notebook # or
    jupyter retro
```

This will start a Jupyter session in your browser. Open any chapter and start coding...

## Contributing

Contributions are accepted via pull requests. You can also open issues on bugs, typos or any corrections and suggest improvements on the notebooks.

## Copyright and License

&copy; 2019 Ram Basnet and T. Doleck. Permission is granted to copy, distribute and/or modify this document
under the terms of the GNU Free Documentation License, Version 1.3
or any later version published by the Free Software Foundation. See LICENSE file for details.
