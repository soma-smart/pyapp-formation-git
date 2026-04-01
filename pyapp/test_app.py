from pyapp.app import calculate


def test_calculate_add():
    assert calculate("add", 2, 3) == 5


def test_calculate_subtract():
    assert calculate("sub", 10, 4) == 6


def test_calculate_with_negative_numbers():
    assert calculate("add", -1, -4) == -5
