# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a positive integer n.

    Return the maximum product of any two digits in n.

    Note: It is possible to use the same digit twice if it appears more than
    once in n.
    '''
    def maxProduct(self, n: int) -> int:
        heap = [0] * 2
        while n > 0:
            heapq.heappushpop(heap, n % 10)
            n //= 10
        return heap[0] * heap[1]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 31
        o = 3
        self.assertEqual(s.maxProduct(i), o)

    def test_two(self):
        s = Solution()
        i = 22
        o = 4
        self.assertEqual(s.maxProduct(i), o)

    def test_three(self):
        s = Solution()
        i = 124
        o = 8
        self.assertEqual(s.maxProduct(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)