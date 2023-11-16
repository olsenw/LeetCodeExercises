# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of strings nums containing n unique binary strings each of
    length n, return a binary string of length n that does not appear in nums.
    If there are multiple answers, return any of them.
    '''
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        nums.sort()
        for i in range(n):
            t = f'{i:0{n}b}'
            if nums[i] != t:
                return t
        return f'{n:0{n}b}'

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["01","10"]
        o = "00"
        self.assertEqual(s.findDifferentBinaryString(i), o)

    def test_two(self):
        s = Solution()
        i = ["00","01"]
        o = "10"
        self.assertEqual(s.findDifferentBinaryString(i), o)

    def test_three(self):
        s = Solution()
        i = ["111","011","001"]
        o = "000"
        self.assertEqual(s.findDifferentBinaryString(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)