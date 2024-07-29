# test_string_calculator.py
from string_calculator import add
import pytest 

def test_empty_string():
    assert add("") == 0

def test_single_number():
    assert add("1") == 1

def test_two_numbers():
    assert add("1,5") == 6

def test_newline_delimiter():
    assert add("1\n2,3") == 6

def test_custom_delimiter():
    assert add("//;\n1;2") == 3

def test_negative_numbers():
    with pytest.raises(ValueError) as exc_info:
        add("-1,2")
    assert str(exc_info.value) == "negative numbers not allowed: -1"

def test_multiple_negative_numbers():
    with pytest.raises(ValueError) as exc_info:
        add("2,-4,3,-5")
    assert str(exc_info.value) == "negative numbers not allowed: -4, -5"

def test_ignore_numbers_over_1000():
    assert add("2,1001") == 2
    assert add("1000,2") == 1002