"""
Module to test the Chess class. 
"""

from labs.oop.bijele.chess import Chess


def test__init__() -> None:
    """Test the __init__ method"""
    chess = Chess(1, 1, 2, 2, 2, 8)
    assert chess.king == 1
    assert chess.queen == 1
    assert chess.rooks == 2
    assert chess.bishops == 2
    assert chess.knights == 2
    assert chess.pawns == 8

# add two test function to __init__ method to test the attributes are correctly initialized


def test__str__() -> None:
    """Test the __str__ metho"""
    chess = Chess()
    assert str(chess) == '1 1 2 2 2 8'


# add two test function to __str__ method to test the string representation is correct

def test__diff__():
    """Test the __sub__ method"""
    chess1 = Chess(1, 1, 2, 2, 2, 8)
    chess2 = Chess(0, 1, 1, 2, 1, 8)
    chess3 = chess1 - chess2
    assert chess3.king == 1
    assert chess3.queen == 0
    assert chess3.rooks == 1
    assert chess3.bishops == 0
    assert chess3.knights == 1
    assert chess3.pawns == 0


# add two test function to __sub__ method to test the difference is correct
