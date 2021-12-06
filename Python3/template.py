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
    # actual test to run on Solution
    def test_name(self):
        s = Solution()
        self.assertEqual(s.problem_name([1,2,3,4,5]), 5)

if __name__ == '__main__':
    unittest.main(verbosity=2)