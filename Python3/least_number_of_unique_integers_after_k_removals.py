# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from collections import Counter

class Solution:
    '''
    Given an array of integers arr and an integer k, find the least
    number of unique integers after removing exactly k elements.
    '''
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        a = 0
        for i, j in reversed(Counter(arr).most_common()):
            if j <= k:
                k -= j
            else:
                a += 1
        return a

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [5,5,4]
        j = 1
        o = 1
        self.assertEqual(s.findLeastNumOfUniqueInts(i,j), o)

    def test_two(self):
        s = Solution()
        i = [4,3,1,1,3,3,2]
        j = 3
        o = 2
        self.assertEqual(s.findLeastNumOfUniqueInts(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)