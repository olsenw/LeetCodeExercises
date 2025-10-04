# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from itertools import combinations
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

'''
Design the CombinationIterator class:
'''
class CombinationIterator:
    '''
    Initializes the object with a a string characters or sorted distinct
    lowercase English letters and a number combinationLength as arguments.
    '''
    def __init__(self, characters: str, combinationLength: int):
        self.s = characters
        self.n = combinationLength
        self.indices = list(range(combinationLength))
        return

    '''
    Returns the next combination of length combinationLength in lexicographical
    order.
    '''
    def next(self) -> str:
        answer = "".join(self.s[i] for i in self.indices)
        i = len(self.indices) - 1
        self.indices[i] += 1
        while i > 0 and self.indices[i] == len(self.s) - (len(self.indices) - i - 1):
            i -= 1
            self.indices[i] += 1
        for j in range(i + 1, len(self.indices)):
            self.indices[j] = self.indices[j-1] + 1
        return answer

    '''
    Returns true if and only if there exists a next combination.
    '''
    def hasNext(self) -> bool:
        return self.indices[0] <= len(self.s) - self.n

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = CombinationIterator("abc", 2)
        self.assertEqual(s.next(), "ab")
        self.assertEqual(s.hasNext(), True)
        self.assertEqual(s.next(), "ac")
        self.assertEqual(s.hasNext(), True)
        self.assertEqual(s.next(), "bc")
        self.assertEqual(s.hasNext(), False)

    def test_two(self):
        s = CombinationIterator("fiklnuy", 3)
        for a in combinations("fiklnuy", 3):
            self.assertEqual(s.hasNext(), True)
            self.assertEqual(s.next(), "".join(a))
        self.assertEqual(s.hasNext(), False)

if __name__ == '__main__':
    unittest.main(verbosity=2)