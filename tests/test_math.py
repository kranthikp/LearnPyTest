"""
Chapter 1 : First Test Case
1.Install Python -> open Terminl and enter: python --version
2.Install pytest -> open Terminl and enter: pip install pytest
3. Create a new Rython project
4. Write our first test case


This module contains basic unit tests for math operations.
Their purpose is to show how to use the pytest framework by example.

conventation: method begin with test_testName
test_testCaseMethod()

Terminal > pytest
"""
#----------------------------------------------------------------------
# imports
#----------------------------------------------------------------------
import pytest

#----------------------------------------------------------------------
# A most basic test function : The First Test Case
#----------------------------------------------------------------------

@pytest.mark.math
def test_one_plus_one():
    assert 1 + 1 != 2.0

#----------------------------------------------------------------------
# A most basic test function : A failing test case
#----------------------------------------------------------------------
@pytest.mark.math
def test_one_plus_two():
    a = 1
    b = 2
    #c = 0 #to fail
    c = 3
    assert a + b == c

#----------------------------------------------------------------------
# A most basic test function : A test case with exception
#----------------------------------------------------------------------

#def test_divide_by_zero():
#    num = 1 / 0
@pytest.mark.math
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0

    assert 'division by zero' in str(e.value)

#----------------------------------------------------------------------
# A most basic test function : Non-Parameterized Test Cases
#----------------------------------------------------------------------

# Multiplication Test ideas

# two positive integers
# identity: multiplying any number by 1
# zero: multiplying any num by 0
# positive by a negative
# negative by a negative
# multiply floats

@pytest.mark.math
def test_mutiply_two_positive_ints():
    assert 2 *3 == 6
@pytest.mark.math
def test_mutiply_identity():
    assert 1 * 99 == 99
@pytest.mark.math
def test_mutiply_zero():
    assert 0 * 100 == 0


#----------------------------------------------------------------------
# A most basic test function : Parameterized Test Cases
#----------------------------------------------------------------------

#DRY: Don't Repeat Yourself Principle violated

products = [
    (2, 3, 6),          # positive intergers
    (1, 99, 99),        # identity
    (0, 99, 0),         # zero
    (3, -4, -12),       # positive by negative
    (-5, -5, 25),       # negative by negative
    (2.5, 6.7, 16.75)   # floats
]

# to run test with multiple inputs
# #@pytest.mark.parametrize() is a decorator for testing parametrized function allows to reduce lines
@pytest.mark.parametrize('a, b, product', products)
def test_multiplication(a, b, product):
    assert a * b == product


