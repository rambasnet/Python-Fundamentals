""" 
Module to test functions.py.
"""

from utility import functions


def test_save_data() -> None:
    """Tests save_data function.
    """
    data = {"name": "John Smith", "win": 2, "loss": 1}
    file_name = "test_data.yaml"
    functions.save_data(file_name, data)
    my_data = functions.read_data(file_name)
    assert data == my_data


def test_save_data1() -> None:
    """Tests save_data function.
    """
    file_name = "test_data1.yaml"
    data = [{"name": "John Smith", "win": 2, "loss": 1},
            {"name": "Jake Smith", "win": 1, "loss": 0}]
    functions.save_data(file_name, data)
    my_data = functions.read_data(file_name)
    assert data == my_data


# FIXME1: Add a test function to unittest the save_data and read_data functions.
# FIXME2: Add a test function to unittest the save_data and read_data functions.


def test_get_random_number() -> None:
    """Tests get_random_number function.
    """
    random_number = functions.get_random_number()
    assert random_number >= 1 and random_number <= 20


def test_check_guessed() -> None:
    """Tests check_guessed function.
    """
    assert functions.check_guessed(5, 5) == True


# FIXME3: Add a test function to unittest the check_guessed function.
# FIXME4: Add a test function to unittest the check_guessed function.
