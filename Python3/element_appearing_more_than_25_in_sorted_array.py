# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array sorted in non-decreasing order, there is exactly one
    integer in the array that occurs more than 25% of the time, return that
    integer.
    '''
    def findSpecialInteger_count(self, arr: List[int]) -> int:
        return Counter(arr).most_common(1)[0][0]

    def findSpecialInteger(self, arr: List[int]) -> int:
        # d,m = divmod(len(arr), 4)
        # target = d + (m > 0)
        target = len(arr) // 4
        curr = arr[0]
        count = 0
        for n in arr:
            if n == curr:
                count += 1
            else:
                curr = n
                count = 1
            if count > target:
                return curr
        return None

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,2,6,6,6,6,7,10]
        o = 6
        self.assertEqual(s.findSpecialInteger(i), o)

    def test_two(self):
        s = Solution()
        i = [1,1]
        o = 1
        self.assertEqual(s.findSpecialInteger(i), o)

    def test_three(self):
        s = Solution()
        i = [1]
        o = 1
        self.assertEqual(s.findSpecialInteger(i), o)

    def test_four(self):
        s = Solution()
        i = [1]
        o = 1
        self.assertEqual(s.findSpecialInteger(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)