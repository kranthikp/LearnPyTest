"""
This module contains basic unit tests for accum operations.
Their purpose is to show how to use the pytest framework by example.

Terminal > pytest
"""

#----------------------------------------------------------------------
# imports
#----------------------------------------------------------------------
import pytest
from stuff.accum import Accumulator

#----------------------------------------------------------------------
# Best Practice: Pattern to follow while writing test cases
# Arrange
# Act
# Assert
#----------------------------------------------------------------------

#----------------------------------------------------------------------
# Tests
#----------------------------------------------------------------------

@pytest.mark.accumulator
def test_accumulator_init():
    accum = Accumulator()
    assert accum.count == 0

@pytest.mark.accumulator
def test_accumulator_add_one():
    accum = Accumulator()       # Arrange: construct accum object
    accum.add()                 # Act: calls accum object ref
    assert accum.count == 1     # Assert: verify count/error

@pytest.mark.accumulator
def test_accumulator_add_three():
    accum = Accumulator()
    accum.add(3)
    assert accum.count == 3

@pytest.mark.accumulator
def test_accumulator_add_twice():
    accum = Accumulator()
    accum.add()
    accum.add()
    assert accum.count == 2

def test_accumulator_cannot_set_count_directly():
    accum = Accumulator()
    with pytest.raises(AttributeError, match=r"can't set attribute") as e:
        accum.count = 10


