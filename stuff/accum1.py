"""
# This module contains a basic accumulator class.
# Its purpose is to show how to use the pytest framework for testing class
"""

"""
# Fixtures
Fixtures are special functions in pytest lib
that pytest can call before test case function

They are the best way to handle
arrange steps shared by multiple tests
when considering the Arrange-Act-Assert Pattern
"""

#----------------------------------------------------------------------
# Class: Accumulator
#----------------------------------------------------------------------

class Accumulator:

    def __init__(self):
        self._count = 0

    @property
    def count(self):
        return self._count

    def add(self, more=1):
        self._count += more

