# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    def minimumSteps(self, s: str) -> int:
        answer = 0
        i = 0
        for j in range(len(s)):
            if s[j] == '0':
                answer += j - i
                i += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "101"
        o = 1
        self.assertEqual(s.minimumSteps(i), o)

    def test_two(self):
        s = Solution()
        i = "100"
        o = 2
        self.assertEqual(s.minimumSteps(i), o)

    def test_three(self):
        s = Solution()
        i = "0111"
        o = 0
        self.assertEqual(s.minimumSteps(i), o)

    def test_four(self):
        s = Solution()
        i = "111100010"
        o = 17
        self.assertEqual(s.minimumSteps(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)