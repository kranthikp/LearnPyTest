"""
This module contains basic unit tests for accum operations.
Their purpose is to show how to use the pytest framework by example.

Terminal > pytest
"""

#----------------------------------------------------------------------
# imports
#----------------------------------------------------------------------
import pytest
from stuff.accum1 import Accumulator

#----------------------------------------------------------------------
# Fixtures scope="session" pass as parameter
#----------------------------------------------------------------------

@pytest.fixture
def accum():                    # Arrange: construct accum object
    return Accumulator()

#----------------------------------------------------------------------
#@pytest.fixture
#def accum():                    # Arrange: construct accum object
#    yield Accumulator() #yield instead of return
#    print("DONE-ZO!")
#----------------------------------------------------------------------

#----------------------------------------------------------------------
# Tests
#----------------------------------------------------------------------

def test_accumulator_init(accum):
    assert accum.count == 0

def test_accumulator_add_one(accum):
    accum.add()                 # Act: calls accum object ref
    assert accum.count == 1     # Assert: verify count/error

def test_accumulator_add_three(accum):
    accum.add(3)
    assert accum.count == 3

def test_accumulator_add_twice(accum):
    accum.add()
    accum.add()
    assert accum.count == 2

def test_accumulator_cannot_set_count_directly(accum):
    with pytest.raises(AttributeError, match=r"can't set attribute") as e:
        accum.count = 10


