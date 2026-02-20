# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Special binary strings are binary strings with the following two properties:
    * THe number of 0's is equal to the number of 1's.
    * Every prefix of the binary string has at least as many 1's as 0's.

    Given a special binary string s.

    A move consists of choosing two consecutive, non-empty, special substrings
    of s, and swapping them. Two strings are consecutive if the last character
    of the first string is exactly one index before the first character of the
    second string.

    Return the lexicographically largest resulting string possible after
    applying the mentioned operations on the string.
    '''
    # based on solution by shivambansiwal98
    # https://leetcode.com/problems/special-binary-string/solutions/7593016/recursive-divide-conquer-sort-balanced-c-drb6
    def makeLargestSpecial(self, s: str) -> str:
        count = 0
        i = 0
        answer = []
        for j in range(len(s)):
            # line scan, +1 for 1 -1 for 0
            count += 1 if s[j] == '1' else -1
            # segment is special when count is zero
            if count == 0:
                # recurse on segment and find maximized lexicographic
                rec = self.makeLargestSpecial(s[i+1:j])
                # the segment is always wrapped in '1' and '0'
                answer.append('1' + rec + '0')
                # next segment
                i = j + 1
        # sort segments in descending order
        answer.sort(reverse=True)
        return ''.join(answer)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "11011000"
        o = "11100100"
        self.assertEqual(s.makeLargestSpecial(i), o)

    def test_two(self):
        s = Solution()
        i = "10"
        o = "10"
        self.assertEqual(s.makeLargestSpecial(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)