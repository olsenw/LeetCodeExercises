# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums consisting of 2 * n integers.

    Divide nums into n pairs such that:
    * Each element belongs to exactly one pair
    * The elements present in a pair are equal.

    Return true if nums can be divided into n pairs, otherwise return false.
    '''
    def divideArray_set(self, nums: List[int]) -> bool:
        s = set()
        for n in nums:
            if n in s:
                s.remove(n)
            else:
                s.add(n)
        return len(s) == 0

    # faster
    def divideArray(self, nums: List[int]) -> bool:
        c = Counter(nums)
        return all(c[i] % 2 == 0 for i in c)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,2,3,2,2,2]
        o = True
        self.assertEqual(s.divideArray(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,4]
        o = False
        self.assertEqual(s.divideArray(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)