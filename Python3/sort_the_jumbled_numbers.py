# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed integer array mapping which represents the mapping rule of
    a shuffled decimal system. mapping[i] = j means digit i should be mapped to
    digit j in this system.

    The mapped value of an integer is the new integer obtained by replacing each
    occurrence of digit i in the integer with mapping[i] for all 0 <= i <= 9.

    Also given another integer array nums. Return the array nums sorted in
    non-decreasing order based on the mapped values of its elements.

    Notes:
    * Elements with the same mapped values should appear in the same relative
      order as in the input.
    * The elements of nums should only be sorted based on their mapped values
      and not be replaced by them.
    '''
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        d = dict()
        for i,j in enumerate(nums):
            if j not in d:
                q = []
                if j == 0:
                    q.append(0)
                while j:
                    q.append(j % 10)
                    j //= 10
                while q:
                    j *= 10
                    j += mapping[q.pop()]
                d[nums[i]] = (j, i)
        return sorted(nums, key=lambda x: d[x])

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [8,9,4,0,2,1,3,5,7,6]
        j = [991,338,38]
        o = [338,38,991]
        self.assertEqual(s.sortJumbled(i,j), o)

    def test_two(self):
        s = Solution()
        i = [0,1,2,3,4,5,6,7,8,9]
        j = [789,456,123]
        o = [123,456,789]
        self.assertEqual(s.sortJumbled(i,j), o)

    def test_three(self):
        s = Solution()
        i = [9,8,7,6,5,4,3,2,1,0]
        j = [0,1,2,3,4,5,6,7,8,9]
        o = [9,8,7,6,5,4,3,2,1,0]
        self.assertEqual(s.sortJumbled(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)