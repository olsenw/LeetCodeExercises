# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s.

    It is possible to perform the following process on s any number of times:
    * Choose an index i in the string such that there is at least one character
      to the left of index i that is equal to s[i], and at least one character
      to the right that is also equal to s[i].
    * Delete the closest character to the left of index i that is equal to s[i].
    * Delete the closest character to the right of index i that is equal to
      s[i].
    
    Return the minimum length of the final string s that can be achieved.
    '''
    def minimumLength_wrong(self, s: str) -> int:
        h = {i:[] for i in "abcdefghijklmnopqrstuvwxyz"}
        for i in range(len(s)):
            h[s[i]].append(i)
        answer = 0
        for c in h:
            answer += len(h[c]) // 3
        return len(s) - (3 * answer)

    def minimumLength(self, s: str) -> int:
        answer = 0
        h = {i:0 for i in "abcdefghijklmnopqrstuvwxyz"}
        for c in s:
            h[c] += 1
            if h[c] == 3:
                h[c] -= 2
                answer += 2
        return len(s) - answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abaacbcbb"
        o = 5
        self.assertEqual(s.minimumLength(i), o)

    def test_two(self):
        s = Solution()
        i = "aa"
        o = 2
        self.assertEqual(s.minimumLength(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)