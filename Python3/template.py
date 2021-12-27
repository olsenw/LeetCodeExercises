# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    def problem_name(self, arg1: List[int]) -> int:
        return len(arg1)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,4,5]
        o = 5
        self.assertEqual(s.problem_name(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,4,5]
        o = 5
        self.assertEqual(s.problem_name(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)