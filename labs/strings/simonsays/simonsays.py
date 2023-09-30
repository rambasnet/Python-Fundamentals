"""
Strings and Unittest Lab
Updated By: FIXME
CSCI 110 Lab
Date: FIXME

Read and solve - Simon Says: https://open.kattis.com/problems/simonsays  

Algorithm:
    1. Read N
    2. Repeat N times:
        1. Read the input string
        2. Check if the string begins with 'Simon says'
        3. If it does, print the rest of the string after 'Simon says', otherwise ignore the string
"""


def main():
    """Main function that solves the problem.
    """
    # step 1. read data
    N = int(input())
    # FIXME 1 - Repeat steps 2-4 N times
    # FIXME 2 - read the input string
    # FIXME 3 - call answer function passing the string as an argument
    # FIXME 4 - print the answer if it returns one, otherwise ignore it


def valid_command(command: str) -> bool:
    """Checks if the string starts with 'Simon says'.

    Args:
        command (str): string to check.

    Returns:
        bool: True if the string starts with 'Simon says', False otherwise.
    """
    # FIXME 5: if the command begins with 'Simon says', return True
    # otherwise, return False
    ans = "FIXME"
    return ans


def answer(command: str) -> str | None:
    """Returns answer given the command or None if the command is not valid.

    Args:
        command (str): string to check

    Returns:
        str|None: rest of the string after 'Simon says' if the command is valid, None otherwise
    """
    valid = valid_command(command)
    # FIXME 6: if valid is True, return the rest of the string after 'Simon says', None otherwise
    return None


if __name__ == "__main__":
    # call the main function if the script is run from the command line
    main()
