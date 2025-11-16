from utils import add_numbers, reverse_string

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0

def test_reverse_string():
    assert reverse_string("abc") == "cba"
    assert reverse_string("Hello") == "olleH"
    assert reverse_string("yes") == "sey"
