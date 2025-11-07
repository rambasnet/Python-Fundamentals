from main import answer, add


def test_answer() -> None:
    """Test answer function
    """
    expected = "Hello World!"
    ans = answer()
    assert ans == expected


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


def test_add3():
    """Test add function
    """
    ans = add(0, -10)
    excepted = -10
    assert ans == excepted
