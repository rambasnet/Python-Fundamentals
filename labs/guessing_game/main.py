"""
Game Application - Guess the Number 
"""

__author__ = "FIXME"
__date__ = "FIXME"
__license__ = "MIT"
__course__ = "CSCI 110 Lab"
__semester__ = "Fall 2023"

from typing import Any, List, Dict
import time
from utility import functions
import settings
from game import play_game, clear_screen, pause, get_menu_option


def game_intro() -> None:
    clear_screen()
    print('Welcome to the game...')
    time.sleep(1)
    print(settings.ASCII)
    time.sleep(1)
    print("Let's start by entering your name.")
    print('Are you ready?')
    pause()


def main() -> None:
    """ 
    Main function for the game.
    """
    game_intro()
    data = functions.read_data(settings.SCORE_BOARD_FILE)
    if not data:
        data = []

    # Ask who's playing?
    player = functions.get_player_info()
    p = functions.find_player_in_db(data, player['name'])
    if p is None:
        data.append(player)
    else:
        player = p

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
            functions.save_data(settings.SCORE_BOARD_FILE, data)
            print(
                f'saving score board to the file {settings.SCORE_BOARD_FILE}')
            print("Goodbye!")
            input('Enter to exit...')
            break


def view_scoreboard(data: List[Any]) -> None:
    """Display data in tabular format.

    Args:
        data (dict): data of all the players in the database
    """
    # FIXME - print data in tabular format


if __name__ == "__main__":
    main()
