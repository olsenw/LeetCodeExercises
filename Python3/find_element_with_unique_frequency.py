# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter, defaultdict
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums.

    Return an integer denoting the first element (scanning from left to right)
    in nums whose frequency is unique. That is, no other integer appears the
    same number of times in nums. If there is no such element, return -1.
    '''
    def firstUniqueFreq(self, nums: List[int]) -> int:
        c = Counter(nums)
        d = defaultdict(list)
        for i in c:
            d[c[i]].append(i)
        for i in d:
            if len(d[i]) == 1:
                return d[i][0]
        return -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [20,10,30,30]
        o = 30
        self.assertEqual(s.firstUniqueFreq(i), o)

    def test_two(self):
        s = Solution()
        i = [20,20,10,30,30,30]
        o = 20
        self.assertEqual(s.firstUniqueFreq(i), o)

    def test_three(self):
        s = Solution()
        i = [10,10,20,20]
        o = -1
        self.assertEqual(s.firstUniqueFreq(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)