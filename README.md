# Think Python Jupyter Notebooks

<h2>How to Think Like a Computer Scientist </h2>

<h3>
Learning with Python3 using Jupyter Notebook (interactive notebook) and pythontutor.com (code visualization)
</h3>

Based on Learning with Python 3 by Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers and Think Python - How to Think Like a Computer Scientist 2nd edition by Jeffrey Elkner, Allen B. Downey, and Chris Meyers

http://openbookproject.net/thinkcs/python/english3e/index.html

Notebook mapping with corresponding chapter:

<table>
    <tr>
        <th>Notebook -></th>              <th>Think Python3 Textbook</th>
    </tr>
    <tr>
        <td>Ch01-Introduction </td>                <td>Chapter 1: The way of the program</td>
    </tr>
    
Ch02-Data-Variables ->               Chapter 2: Variables, expressions, and statements
Ch03-1-Functions-Built-in ->         Examples of some built-in functions
Ch03-2Functions-UserDefined ->       Chapter 4 and 6: Functions and Fruitful functions
    Functions-Lambda -               Lambda functions, map, reduce, filter
    Functions-Recursion ->      Chapter 18: Recursion
Ch04-Conditionals ->            Chapter 5: Conditionals
Ch05-Iterations ->              Chapter 7: Iteration - for and while loops
Ch06-Strings ->                 Chapter 8: Strings
Ch07-Tuples ->                  Chapter 9: Tuples
Ch08-1-Lists ->                 Chapter 11: Lists
Ch08-2-Lists-Comprehension-Lambda -          List comprehension
Ch12-Modules ->              Chapter 12: Modules - built-in and user-defined
Ch13-Files ->                Chapter 13: Files - with, open, binary, urllib
Ch15-OOP ->                  Chapter 15, 16
Ch16-OOP-Polymorphism ->     Chapter 21 
Ch23-Inheritance             Chapter 23: Inheritance
Ch19-Exceptions ->           Chapter 19: Exceptions
Ch20-Dictionaries ->         Chapter 20: Dictionaries
Ch20-Dictionaries-Advanced -  zip(), OrderedDict
Ch21-Memoization-
    Optimizaion-
    TimeComplexity-               Optimizing recursive solutions
Ch22-UnitTest-                       Unit testing python codes
Ch23-SqliteDB-                   Sqlite DB access with sqlite3
</pre>

## Who can use these notebooks

### University and High-school Coding Instructors

Depending on the course level and topics covered, intructors can pick and choose appropriate chapters. E.g., we've used Chapter 1 - 15 (skipping some chapters such as as Functions-Lambda) in Beginning programing 3/4-credit university courses (CS0 and CS1) where students have no prior experience to programming. On the otherhand, we've also used all the chapters for 2-credit advanced programing courses where students have some prior programming experiences in Python or other programming languages (CS1, CS2 level).

### Self learners

Depending on their skill and interest level, learners can move as swiftly as appropairate through the chapters. Try solving some exercises towards the end of each chpater before moving on for self assessment of the mastery of the materails.

## How to use these notebooks

### Important

Inorder to learn coding, it's very important to actually type code on your own from scratch and NOT copy paste! You can run provided cells to see the output, follow along and learn from it but it's important that you either start a new jupyter notebook or add cells and write your own code from scratch to practice the concepts covered with many similar examples and solve the exercises provided.

### Online service

If you do not want to install development environment on a persoanl computer, you can launch an interactive session using the Binder service:
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/rambasnet/thinkpythonnotebooks/master)

### On a local system

To run these notebooks interactvely and save your work locally, you need <a href="https://www.python.org/" target="_blank">Python 3</a> and <a href="http://jupyter.org/" target="_blank"> Jupyter Notebook </a> -- an interactive web-based editor that allows you to create and share documents that contain live code and data. Anaconda or Miniconda is the recommended way to install Python and other packages on all modern platforms.

#### Installing via Anaconda or Miniconda

Anaconda or Miniconda has Python 3 and many other packages that you can easily install on any platform (Windows, Linux, and Mac). First, install Anaconda: http://docs.continuum.io/anaconda/install/ or Miniconda https://conda.io/docs/user-guide/install/index.html

After installing anaconda or miniconda, open a terminal and run the following commands:

    conda update conda
    conda install jupyter

#### Running the notebook server

Once Python 3 and Jupyter Notebook are installed, open a terminal change working directory using cd command to go into the folder where this repo is cloned and run the notebook from there:

    cd <directory where this repo is cloned>
    jupyter notebook

This will start a Jupyter session in your browser. Open a chapter, and start coding...

## Contributing

We'd be glad if you'd like to contribute to this project. Contributions are accepted via pull requests. You can also open issues on bugs, typos or any corrections and suggest improvements on the notebooks.

## Copyright and License

&copy; 2018 Ram B. Basnet and T. Doleck. Permission is granted to copy, distribute and/or modify this document
under the terms of the GNU Free Documentation License, Version 1.3
or any later version published by the Free Software Foundation. See LICENSE file for details.

Please feel free to use the content anyway you find it useful.
