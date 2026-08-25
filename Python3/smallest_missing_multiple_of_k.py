# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        a = k
        while a in nums:
            a += k
        return a

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [8,2,3,4,6]
        j = 2
        o = 10
        self.assertEqual(s.missingMultiple(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,4,7,10,15]
        j = 5
        o = 5
        self.assertEqual(s.missingMultiple(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)