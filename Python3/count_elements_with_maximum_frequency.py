# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array nums consisting of positive integers.

    return the total frequencies of elements in nums such that those elements
    all have the maximum frequency.

    The frequency of an element is the number of occurrences of that element in
    the array.
    '''
    def maxFrequencyElements(self, nums: List[int]) -> int:
        f = Counter(nums)
        m = max(f.values())
        c = Counter()
        for i in f:
            if f[i] == m:
                c[f[i]] += f[i]
        return max(c.values())

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,2,3,1,4]
        o = 4
        self.assertEqual(s.maxFrequencyElements(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,4,5]
        o = 5
        self.assertEqual(s.maxFrequencyElements(i), o)

    def test_three(self):
        s = Solution()
        i = [10,12,11,9,6,19,11]
        o = 2
        self.assertEqual(s.maxFrequencyElements(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)