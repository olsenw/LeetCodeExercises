# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums, return true if any values appears at least
    twice in the array, and return false if every element is distinct.
    '''
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for n in nums:
            if n in s:
                return True
            s.add(n)
        return False

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,1]
        o = True
        self.assertEqual(s.containsDuplicate(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,4]
        o = False
        self.assertEqual(s.containsDuplicate(i), o)

    def test_three(self):
        s = Solution()
        i = [1,1,1,3,3,4,3,2,4,2]
        o = True
        self.assertEqual(s.containsDuplicate(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)