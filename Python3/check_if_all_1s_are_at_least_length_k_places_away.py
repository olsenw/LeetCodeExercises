# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        away = 0
        for n in nums:
            if n == 1:
                if away > 0:
                    return False
                away = k
            else:
                away -= 1
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,0,0,0,1,0,0,1]
        j = 2
        o = True
        self.assertEqual(s.kLengthApart(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,0,0,1,0,1]
        j = 2
        o = False
        self.assertEqual(s.kLengthApart(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)