# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed binary string s having an even length.

    A string is beautiful if it's possible to partition it into one or more
    substrings such that:
    * Each substring has an even length.
    * Each substring contains ony 1's or only 0's.

    It it possible to change any character in s to 0 or 1.

    Return the minimum number of changes required to make the string s
    beautiful.
    '''
    # hints give away the solution
    def minChanges(self, s: str) -> int:
        answer = 0
        for i in range(0, len(s), 2):
            if s[i] != s[i+1]:
                answer += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "1001"
        o = 2
        self.assertEqual(s.problem_name(i), o)

    def test_two(self):
        s = Solution()
        i = "10"
        o = 1
        self.assertEqual(s.problem_name(i), o)

    def test_three(self):
        s = Solution()
        i = "0000"
        o = 0
        self.assertEqual(s.problem_name(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)