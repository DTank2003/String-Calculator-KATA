# test_string_calculator.py
from string_calculator import add

def test_empty_string():
    assert add("") == 0
    