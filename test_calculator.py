import pytest
from mehthematical_calculator import add, subtract, multiply, divide, exponent

def test_add_positive_numbers():
    """Tests that adding positive numbers gets the correct answer"""
    assert add(6, 9) == 15

def test_add_negative_numbers():
    """Tests that adding negative numbers gets the correct answer"""
    assert add(-6, 7) == 1

def test_subtract_positive_numbers():
    """Tests that subtracting positive numbers gets the correct answer"""
    assert subtract(20, 4) == 16

def test_subtract_large_from_small_numbers():
    """Tests that subtracting a large number from a smaller number gets the correct answer"""
    assert subtract(2, 5) == -3

def test_multiply_positive_numbers():
    """Tests that multiplying positive numbers gets the correct answer"""
    assert multiply(11, 5) == 55

def test_multiply_negative_numbers():
    """Tests that multiplying negative numbers gets the correct answer"""
    assert multiply(-3, 4) == -12

def test_multiply_by_zero():
    """Tests that any number multiplied by zero is zero"""
    assert multiply(8, 0) == 0

def test_divide_positive_numbers():
    """Tests that dividing positive numbers gets the correct answer"""
    assert divide(10, 5) == 2

def test_divide_negative_numbers():
    """Tests that dividing negative numbers gets the correct answer"""
    assert divide(-12, 4) == -3

def test_divide_by_one():
    """Tests that dividing by one gets the first number inputted"""
    assert divide(21, 1) == 21

def test_divide_by_zero():
    """Tests that dividing by zero returns nothing"""
    assert divide(3, 0) == None

def test_divide_zero_by_zero():
    """Tests that dividing zero by zero returns nothing"""
    assert divide(0, 0) == None

def test_exponent_positive_numbers():
    """Tests that exponentiation of positive numbers gets the correct answer"""
    assert exponent(2, 3) == 8

def test_exponent_zero_power():
    """Tests that going to the power of zero equals one"""
    assert exponent(5, 0) == 1
