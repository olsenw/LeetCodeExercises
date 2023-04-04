# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s, partition the string into one or more substrings such that
    the characters in each substring are unique. That is, no letter appears in a
    single substring more than once.
    
    Return the minimum number of substrings in such a partition.
    
    Note that each character should belong to exactly one substring in a
    partition.'''
    def partitionString(self, s: str) -> int:
        answer = 1
        t = s[0]
        for c in s[1:]:
            if c in t:
                t = c
                answer += 1
            else:
                t += c
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abacaba"
        o = 4
        self.assertEqual(s.partitionString(i), o)

    def test_two(self):
        s = Solution()
        i = "ssssss"
        o = 6
        self.assertEqual(s.partitionString(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)