# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums.

    An integer x is special if all occurrences of x in nums appear in a single
    contiguous block.

    Return the number of distinct special integers in nums.
    '''
    def countSpecialIntegers(self, nums: list[int]) -> int:
        last = defaultdict()
        dups = set()
        for i,j in enumerate(nums):
            if j in last and last[j] == i - 1:
                last[j] = i
            elif j in last:
                dups.add(j)
            else:
                last[j] = i
        return len(last) - len(dups)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,2,1]
        o = 1
        self.assertEqual(s.countSpecialIntegers(i), o)

    def test_two(self):
        s = Solution()
        i = [3,3,1,2,2,1]
        o = 2
        self.assertEqual(s.countSpecialIntegers(i), o)

    def test_three(self):
        s = Solution()
        i = [66,65,66,66,66]
        o = 1
        self.assertEqual(s.countSpecialIntegers(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)