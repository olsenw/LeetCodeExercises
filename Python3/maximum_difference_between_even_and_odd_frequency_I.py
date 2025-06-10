# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    Given a string s consisting of lowercase English letters.

    Find the maximum difference diff = a1 - a2 between the frequency of
    characters a1 and a2 in the string such that:
    * a1 has an odd frequency in the string.
    * a2 has an even frequency in the string.

    Return this maximum difference.
    '''
    def maxDifference(self, s: str) -> int:
        c = Counter(s)
        e,o = [], []
        for i in c:
            if c[i] % 2:
                o.append(i)
            else:
                e.append(i)
        answer = -10**7-9
        for i in e:
            for j in o:
                answer = max(answer, c[j] - c[i])
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "aaaaabbc"
        o = 3
        self.assertEqual(s.maxDifference(i), o)

    def test_two(self):
        s = Solution()
        i = "abcabcab"
        o = 1
        self.assertEqual(s.maxDifference(i), o)

    def test_three(self):
        s = Solution()
        i = "bba"
        o = -1
        self.assertEqual(s.maxDifference(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)