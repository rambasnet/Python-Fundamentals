"""Script to demonstrate typing in Python 3.5 and higher version.

Must install and include path to pylint in VS Code.
"""

# Variable type annotations
num: int = 10
var: float = "Hello"

name: str = "James Bond"
var1: str = 100

def greeting(name: str) -> str:
    return f'Hello, {name}!'

print(greeting('James Bond'))
print(greeting(3434.3434))


