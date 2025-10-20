import pytest
from mehthematical_calculator import add, subtract, multiply, divide, exponent

def test_add_positive_numbers():
    assert add(6, 9) == 15

def test_add_negative_numbers():
    assert add(-6, 7) == 1

def test_subtract_positive_numbers():
    assert subtract(20, 4) == 16

def test_subtract_large_from_small_numbers():
    assert subtract(2, 5) == -3

def test_multiply_positive_numbers():
    assert multiply(11, 5) == 55

def test_multiply_negative_numbers():
    assert multiply(-3, 4) == -12

def test_multiply_by_zero():
    assert multiply(8, 0) == 0

def test_divide_positive_numbers():
    assert divide(10, 5) == 2

def test_divide_negative_numbers():
    assert divide(-12, 4) == -3

def test_divide_by_one():
    assert divide(21, 1) == 21

def test_divide_by_zero():
    assert divide(3, 0) == None

def test_divide_zero_by_zero():
    assert divide(0, 0) == None

def test_exponent_positive_numbers():
    assert exponent(2, 3) == 8

def test_exponent_zero_power():
    assert exponent(5, 0) == 1
