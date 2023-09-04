# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s and an integer array indices of the same length. The string
    s will be shuffled such that the character at the ith position moves to
    indices[i] in the shuffled string.

    Return the shuffled string.
    '''
    def restoreString_passes(self, s: str, indices: List[int]) -> str:
        return ''.join(i[1] for i in sorted(zip(indices, s)))

    def restoreString(self, s: str, indices: List[int]) -> str:
        answer = ["a"] * len(s)
        for a,b in enumerate(indices):
            answer[b] = s[a]
        return ''.join(answer)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "codeleet"
        j = [4,5,6,7,0,2,1,3]
        o = "leetcode"
        self.assertEqual(s.restoreString(i,j), o)

    def test_two(self):
        s = Solution()
        i = "abc"
        j = [0,1,2]
        o = "abc"
        self.assertEqual(s.restoreString(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)