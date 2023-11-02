""" 
Module for utility functions to support the game.
"""

from typing import Any
import random
import yaml


def get_random_number() -> int:
    """ 
    Returns a random integer between 1 and 20, inclusive.

    Returns:
        int: integer between 1 and 20, inclusive.
    """
    return random.randint(1, 20)


def read_data(yaml_file_path: str) -> list:
    """ 
    Reads data from the given file path and returns a dictionary.

    Args:
        file_path (str): path to the file to read.

    Returns:
        dict: dictionary containing the data read from the file.
    """
    data = []
    try:
        with open(yaml_file_path, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)
    except FileNotFoundError:
        pass
    return data


def save_data(yaml_file_path: str, data: Any) -> None:
    """ 
    Writes data to the given file path.

    Args:
        file_path (str): path to the file to write to.
        data (dict): data to write to the file.
    """
    with open(yaml_file_path, 'w', encoding='utf-8') as file:
        yaml.dump(data, file)


def check_guessed(rand: int, guess: int) -> bool:
    """ 
    Checks if the guessed number is correct.

    Args:
        rand (int): the random number that is hidden.
        guess (int): the user's guessed number.

    Returns:
        bool: True if the guessed number is correct, False otherwise.
    """
    return rand == guess


def get_player_info() -> dict:
    """ 
    Gets new player's info.

    Returns:
        dict: new player's info as dict.
    """
    name = input("What is your name? ")
    return {'name': name.strip(), 'win': 0, 'loss': 0}


def get_number_between_1_20() -> int:
    """ 
    Gets a number between 1 and 20, inclusive.

    Returns:
        int: number between 1 and 20, inclusive.
    """
    while True:
        guess = input("Enter your guess: ")
        if not guess.isdigit():
            print("Invalid guess. Try again.")
            continue
        int_guess = int(guess)
        # FIXME: Add code to check if the guess is between 1 and 20, inclusive.
        # if not a valid number print error and ask them to try again
        return int_guess


def find_player_in_db(database: list[Any], name: str) -> Any:
    """Find and return the player in the database.

    Args:
        database (list[Any]): database of players.
        name (str): player's name to search for.

    Returns:
        None|dict: Returns player as dict if found, None otherwise.
    """
    for player in database:
        if player['name'] == name:
            return player
    return None
