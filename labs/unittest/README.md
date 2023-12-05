# CS0 Lab - OOP and Unittesting with Unittest Library

Possible Points: 100

Write a Python program to solve the Kattis problem - Bijele - [https://open.kattis.com/problems/bijele](https://open.kattis.com/problems/bijele) . Read the problem statement carefully to design a correct solution using OOP and unittest.

## Install and Use Kattis-cli

- if you've installed kattis-cli before, update it to the latest version

```bash
$ pip install -U kattis-cli
$ python -m pip install -U kattis-cli
```

- if you've not installed kattis-cli before, install it
    
```bash
    $ pip install kattis-cli
    $ python -m pip install kattis-cli
```

## Setup Kattis-cli

- setup kattis-cli by providing logging in to Kattis using your Kattis username and password

```bash
kattis setup
```

## Lab Instructions

- Open your CS0Lab-... repo in VS Code
- Create lab folder **unittest** inside your CS0Lab-... repository
- Inside the lab folder, download the problem metadata and sample files for the problem **bijele** using Kattis-clis
- Use previous lab **OOP and Unittesting** to complete this lab
- Must Use **unittest** library to write unit tests for the class methods
- Write at least two test methods for each class method you're testing

```bash
kattis get bijele
```

- Inside **bijele** folder, type the partial code stub provided and fix all FIXMEs. (80 points)
- Follow best programming practices by using proper white spaces, comments, etc.
`
- Run unit test using pytest and create screenshot when all the test cases pass. Install pytest if required. Pick one of the following ways to run pytest.

```bash
  $ pytest --version
  $ pip install -U pytest
  $ pytest .
  $ python -m pytest .
```


- Test the whole program using Katts-cli. (10 points)

```bash
$ cd bijele
$ kattis test
```

- Create the screenshot of the correct local test result. (10 points)
- Submit the solution to Kattis using Kattis-cli. (10 points)

```bash
$ cd bijele
$ kattis submit
```

- Create screenshot of the kattis final Accepted verdict and save it to the lab folder. (10 points)

- Update your README file (10 points) as shown here: [https://github.com/rambasnet/csci000-astudent](https://github.com/rambasnet/csci000-astudent)

## Submission

- Make sure to format the code using pep8 or black before submission.
- Add all the relevant source file(s), documents, and screenshots into the correct lab folder and do a final add, commit, and push before the due date.

```bash
$ git pull
$ git status
$ git add <filename>… - add each file in the red that is part of this lab
$ git status
$ git commit -m "Final Submission"
$ git push
$ git status
```

- Check and make sure the files are actually pushed to your GitHub repo on github.com.
