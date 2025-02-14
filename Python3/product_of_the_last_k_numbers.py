# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

'''
Design an algorithm that accepts a stream of integers and retrieves the product
of the last k integers of the stream.

Implement the ProductOfNumbers class:
'''
class ProductOfNumbers_brute_tle:
    '''
    Initializes the object with an empty stream.
    '''
    def __init__(self):
        self.answers = []

    '''
    Appends the integer num to the stream.
    '''
    def add(self, num: int) -> None:
        for i in range(len(self.answers)):
            self.answers[i] *= num
        self.answers.append(num)
    
    '''
    Returns the product of the last k integers in the current list. It is
    assumed that list always has at least k integers in it.
    '''
    def getProduct(self, k: int) -> int:
        return self.answers[-k]


class ProductOfNumber_tle2:
    def __init__(self):
        self.answers = []

    def add(self, num: int) -> None:
        if num == 0:
            self.answers = []
        for i in range(len(self.answers)):
            self.answers[i] *= num
        self.answers.append(num)
    
    def getProduct(self, k: int) -> int:
        return self.answers[-k] if k <= len(self.answers) else 0

# took a while thinking on hints
class ProductOfNumbers:
    def __init__(self):
        self.answers = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.answers = [1]
        else:
            self.answers.append(self.answers[-1] * num)
    
    def getProduct(self, k: int) -> int:
        return self.answers[-1] // self.answers[-k-1] if k < len(self.answers) else 0


class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = ProductOfNumbers()
        s.add(3)
        s.add(0)
        s.add(2)
        s.add(5)
        s.add(4)
        self.assertEqual(s.getProduct(2), 20)
        self.assertEqual(s.getProduct(3), 40)
        self.assertEqual(s.getProduct(4), 0)
        s.add(8)
        self.assertEqual(s.getProduct(2), 32)

if __name__ == '__main__':
    unittest.main(verbosity=2)