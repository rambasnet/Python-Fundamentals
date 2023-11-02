"""
Game Application - Guess the Number 
"""

__author__ = "FIXME"
__date__ = "FIXME"
__license__ = "MIT"
__course__ = "CSCI 110 Lab"
__semester__ = "Fall 2023"

from typing import Any, List, Dict
from utility import functions
import settings


def clear_screen() -> None:
    """Clears the screen.
    """
    print("\033c", end="")


def pause() -> None:
    """Pauses the screen.
    """
    input("Press Enter to continue...")
    clear_screen()


def get_menu_option() -> int:
    """Prints menu for player to interact with.
    """

    menu = """
    Menu Options
    ============ 
    1. Play Game
    2. View Scoreboard
    3. Quit
    """
    print(menu)
    while True:
        option = input("Enter one of the menu options [1-3]: ")
        if not option.isdigit():
            print("Invalid option. Try again.")
            continue
        int_option = int(option)
        if not 1 <= int_option <= 3:
            print("Invalid option. Try again.")
            continue
        return int_option


def play_game(name: str, max_tries: int) -> bool:
    print(f"Let's play Guess the Number Game, {name}! Good luck...")
    rand = functions.get_random_number()
    print('I am thinking of a number between 1 and 20.')
    print('You have 5 chances to guess the number.')
    tries = 0
    while tries <= max_tries:
        # FIXME: Add code to get the user's guess using the correct function in utility/functions.py.
        # FIXME: check if the user's guess is correct using the correct function in utility/functions.py.
        # FIXME: If the user's guess is correct, print a message and return True for a win.
        return True
    else:
        return False  # return False for a loss


def main() -> None:
    """ 
    Main function for the game.
    """
    clear_screen()
    data = functions.read_data(settings.SCORE_BOARD_FILE)
    if not data:
        data = []
    print('Welcome to the Guess the Number Game!')
    print('=====================================')
    print("Let's start by entering your name.")
    # Ask who's playing?
    player = functions.get_player_info()
    if not functions.find_player_in_db(data, player['name']):
        data.append(player)

    while True:
        clear_screen()
        option = get_menu_option()
        if option == 1:
            win = play_game(player['name'], settings.MAX_TRIES)
            if win:
                player['win'] += 1
            else:
                player['loss'] += 1
        elif option == 2:
            view_scoreboard(data)
        elif option == 3:
            # FIXME - Update data to include the new player's info.
            # FIXME - Add code to save the data to the file using correct function in utility/functions.py.
            functions.save_data(settings.SCORE_BOARD_FILE, data)
            print(
                f'saving score board to the file {settings.SCORE_BOARD_FILE}')
            print("Goodbye!")
            break


def view_scoreboard(data: List[Any]) -> None:
    """Display data in tabular format.

    Args:
        data (dict): data of all the players in the database
    """


if __name__ == "__main__":
    main()
