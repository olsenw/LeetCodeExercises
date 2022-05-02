# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an integer array nums, move all the even integers to the
    beginning of that array followed by all the odd integers.

    Return any array that satisfies this condition.
    '''
    def sortArrayByParity_list_concat(self, nums: List[int]) -> List[int]:
        e = []
        o = []
        for i in nums:
            if i % 2:
                o.append(i)
            else:
                e.append(i)
        return e + o

    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda x: x % 2)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,1,2,4]
        o = [2,4,3,1]
        self.assertEqual(s.sortArrayByParity(i), o)

    def test_two(self):
        s = Solution()
        i = [0]
        o = [0]
        self.assertEqual(s.sortArrayByParity(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)