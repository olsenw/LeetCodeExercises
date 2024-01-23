# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

'''
Run-length encoding can be used to encode a sequence of integers. In a
run-length encoded array of even length encoding (0-indexed), for all even i,
encoding[i] tells the number of times that the non-negative integer value
encoding[i + 1] is repeated in the sequence.

For example, the sequence arr = [8,8,8,5,5] can be encoded to be
encoding = [3,8,2,5]. encoding = [3,8,0,9,2,5] and encoding = [2,8,1,8,2,5] are
also valid RLE of arr.

Given a run-length encoded array, design an iterator that iterates through it.

Implement the RLEIterator class:
'''
class RLEIterator:
    '''
    Initializes the object with the array encoded.
    '''
    def __init__(self, encoding: List[int]):
        self.encoding = [[encoding[i+1], encoding[i]] for i in range(0, len(encoding), 2)]
        self.i = 0

    '''
    Exhausts the next n elements and returns the last element exhaysted in this
    way. If there are no elements left to exhaust, return -1 instead.
    '''
    def next(self, n: int) -> int:
        while self.i < len(self.encoding) and n > 0:
            if n > self.encoding[self.i][1]:
                n -= self.encoding[self.i][1]
                self.i += 1
            elif n == self.encoding[self.i][1]:
                self.i += 1
                return self.encoding[self.i - 1][0]
            else:
                self.encoding[self.i][1] -= n
                return self.encoding[self.i][0]
        return -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = RLEIterator([3,8,0,9,2,5])
        self.assertEqual(s.next(2), 8)
        self.assertEqual(s.next(1), 8)
        self.assertEqual(s.next(1), 5)
        self.assertEqual(s.next(2), -1)

if __name__ == '__main__':
    unittest.main(verbosity=2)