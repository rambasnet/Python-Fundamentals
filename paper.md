---
title: 'FDS Python: Fundamentals and Data Structures with Python'
tags:
- python programming
- think python3
- beginning programming
- data structures
- interactive python
authors:
- name: Ram B. Basnet
  orcid: 0000-0001-6864-6893
  affiliation: 1
- name: Tenzin Doleck
  orcid: 0000-0000-0000-1234
  affiliation: 2
affiliations:
- name: Colorado Mesa University
  index: 1
- name: McGill University
  index: 2
date: 29 December 2018
bibliography: paper.bib
---

# Summary

FDS Python is a set of Jupyter notebooks that covers fundamental concepts of programming and data structures using Python. These interactive notebooks are based on the open-source textbook Think Python: How to Think Like a Computer Scientist (http://openbookproject.net/thinkcs/python/english3e/index.html#) [@Wentworth2012RLE]. The notebooks consists of summary of the theory/lecture notes and syntax of concepts along with interactive code examples for students to learn from the basic programming concepts to data structures and popular libraries such as turtle, pygame, sqlite3, etc. The mapping of notebook chapters with the textbook chapters is provided in the README.md file.

These notebooks are designed to accommodate beginners as well as experienced programmers who are interested in learning Python. More importantly, the interactive nature of these notebooks force students code to learn and not learn to code. Pythontutor [@GuoSIGCSE2013] (http://pythontutor.com) is utilized to visualize and help students understand concepts better along with problems from open.kattis.com (https://open.kattis.com/) [@Basent2018Kattis] as exercises where appropriate.

# Statement of need

Many universities and high schools around the world teach Python as the first programming language. Simpler, clean and less verbose, prototyping like syntax of Python along with its myriad of applications in various fields from cybersecurity to Data Science makes Python an appropriate language to teach various fundamental programming concepts in Computer Science. Textbook alone can be very verbose and theoretical while students are very eager to learn coding hands-on. Though Python provides a way to quickly write and test code and concepts in interactive "chevron prompt" mode, the codes and results will go away and can not be reproduced after the session is terminated. Moreover, writing multiple line of codes or functions are not that intuitive because of the language's strict syntactic rules on enforcing whitespaces to represent block of codes. Jupyter notebooks can easily overcome these drawbacks while allowing for quickly and interactively trying anywhere from a single to many lines of codes with complete solutions and keeping track of the output results as part of the notes. Students can always open their notes and see what they've done in the past; quickly write and try many similar examples to enforce the understanding of the concepts and continuously keep all the notes together.

The notebooks are complete and can be easily adopted by other instructors who wish to teach Python using a practical, follow-along live coding approach. They are used in university courses (Beginning and Advanced Programming courses) for three semesters in a row at Colorado Mesa University (2017-2018). Instructors in begging programming course can spend more time demonstrating the concepts with many examples. Instructors in advanced or intensive boot camp like courses can skip the theory part on fundamental concepts and focus on syntax allowing to quickly recap the basic concepts and spend more time on the advanced topics and concepts.

# Instructional design

Incremental development is a popular design principal in software engineering. Based on the experience of the authors after teaching programming courses for many years confirmed by creators of similar modules [@Barba2018CFDPython], we've adopted the basic design pattern for creating these notebooks using *computable content* [@Barba2018CFDPython]:
1. Add narrative and brief content
2. Link out to detail contents and documentation
3. Break it down into smaller steps
4. Combine smaller steps into bigger steps
5. Apply concepts to solve common problems
6. Spice with challenge problems/exercises
7. Publish openly online

# References
