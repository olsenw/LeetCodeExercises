# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a non-empty array of integers nums, every element appears
    twice except for one. Find that single one.

    Implement a solution with linear runtime complexity and use only 
    constant extra space.
    '''
    # make use of the power XOR
    # a number XOR intself is always zero, so if XOR whole list the 
    # single unique number will be left
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            ans ^= n
        return ans

    # This fails because the set does not use constant space...
    def singleNumber_dict(self, nums: List[int]) -> int:
        d = set()
        for n in nums:
            if n in d:
                d.remove(n)
            else:
                d.add(n)
        return list(d)[0]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,2,1]
        o = 1
        self.assertEqual(s.singleNumber_dict(i), o)
        self.assertEqual(s.singleNumber(i), o)

    def test_two(self):
        s = Solution()
        i = [4,1,2,1,2]
        o = 4
        self.assertEqual(s.singleNumber_dict(i), o)
        self.assertEqual(s.singleNumber(i), o)

    def test_three(self):
        s = Solution()
        i = [1]
        o = 1
        self.assertEqual(s.singleNumber_dict(i), o)
        self.assertEqual(s.singleNumber(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)