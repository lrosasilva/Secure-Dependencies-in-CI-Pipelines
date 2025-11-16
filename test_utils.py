from utils import add_numbers, reverse_string

def test_add_numbers():
    assert add_numbers(2, 3) == 5

def test_reverse_string():
    assert reverse_string("hello") == "olleh"

