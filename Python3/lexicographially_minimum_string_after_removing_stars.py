# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s. It may contain any number of '*' characters. Remove all
    the '*' characters using the following operation:
    * Delete the leftmost '*' and the smallest non-'*' character to its left. If
      there are several smallest characters, delete any of them.
    
    Return the lexicographically smallest resulting string after removing all
    '*' characters.
    '''
    def clearStars(self, s: str) -> str:
        heap = []
        index = 0
        answer = []
        for c in s:
            if c == '*':
                x,y = heapq.heappop(heap)
                answer[-y] = '*'
            else:
                answer.append(c)
                heapq.heappush(heap, (c,-index))
                index += 1
        return "".join(c for c in answer if c != '*')

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "aaba*"
        o = "aab"
        self.assertEqual(s.clearStars(i), o)

    def test_two(self):
        s = Solution()
        i = "abc"
        o = "abc"
        self.assertEqual(s.clearStars(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)