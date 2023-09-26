# CS0 Lab - User-defined Functions and Unittest

Possible Points: 100

Write a Python program to solve the Kattis problem called thelastproblem: [https://open.kattis.com/problems/thelastproblem](https://open.kattis.com/problems/thelastproblem). Read the problem statement carefully to design a correct solution.

## Lab Instructions

1. Open your CS0Lab-... repo in VS Code.
2. Create lab folder called **lastproblem** inside your repository.
3. Inside the the lab folder, create two files: main.py and test_main.py.
4. Use the partial code stub provided and fix all the FIXMEs. (80 points)
    - Write #fixed after each fixme that you fix.
5. Follow best programming practices by using proper white spaces, comments, etc.

```
IMPORTANT: Never ask the user telling what data to enter for Kattis problems. Kattis knows what to enter.
Directly read the input. Print only the answer as displayed in the sample output.
Print as asked: nothing less; nothing more!
Kattis is a computer program that provides specific input and expects exact output – to a space to give the correct verdict.
```

6. Run unit test using pytest and create screenshot when all the test cases pass. Install pytest if required. Pick one of the following ways to run pytest.

```bash
  $ pytest --version
  $ pip install -U pytest
  $ pytest test_main.py
  $ python -m pytest test_main.py
```

7. Test the whole program manually. While testing, provide input using the same format as described in the Input section and shown in input samples.
8. Upload only the .py scripts to Kattis for testing. You can test your solution as many times as you wish. Kattis uses its own hidden test cases to test your program against. However, your goal is to get the accepted verdict in the first try.
9. Create screenshots showing your local testing and the kattis final Accepted verdict and save them to the lab folder. (10 points)
10. Update your README file (10 points) as shown here: [https://github.com/rambasnet/csci000-astudent](https://github.com/rambasnet/csci000-astudent)

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
