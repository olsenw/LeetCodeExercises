# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    Given an array of integers arr of even length n and an integer k.

    Divide the array into exactly n / 2 pairs such that the sum of each pair is
    divisible by k.

    Return True if this is possible or false otherwise.
    '''
    def canArrange(self, arr: List[int], k: int) -> bool:
        c = Counter()
        for i in arr:
            j = i % k
            if c[j] > 0:
                c[j] -= 1
            else:
                c[(k - j) % k] += 1
        return not any(c[i] != 0 for i in c)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,4,5,10,6,7,8,9], 5
        o = True
        self.assertEqual(s.canArrange(*i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,4,5,6], 7
        o = True
        self.assertEqual(s.canArrange(*i), o)

    def test_three(self):
        s = Solution()
        i = [1,2,3,4,5,6], 10
        o = False
        self.assertEqual(s.canArrange(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)