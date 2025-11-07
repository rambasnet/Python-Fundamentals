
def add(a: int, b: int) -> int:
    """Add two numbers

    Args:
        a (int): first number
        b (int): second number

    Returns:
        int: sum of a and b
    """
    return a+b


def test_add() -> None:
    """Test add function
    """
    ans = add(10, 20)
    expected = 30
    assert ans == expected


def test_add2() -> None:
    """Test add function
    """
    ans = add(5, 99)
    expected = 104
    assert ans == expected


def test_add3() -> None:
    """Test add function
    """
    ans = add(0, -10)
    excepted = -10
    assert ans == excepted
