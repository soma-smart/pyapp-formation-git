from pyapp.app import add, subtract


def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-1, -4) == -5


def test_subtract_positive_numbers():
    assert subtract(10, 4) == 6
