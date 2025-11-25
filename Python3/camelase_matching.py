# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of strings queries and a string pattern, return a boolean
    array answer where answer[i] is true if queries[i] matches patterns, and
    false otherwise.

    A query word queries[i] matches pattern if a lowercase English letter can be
    inserted into the pattern so that it equals the query. It is possible to
    insert a character at any position in the pattern or choose to not insert
    any characters at all.
    '''
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        answer = []
        for q in queries:
            i,j = 0,0
            while i < len(q):
                if j < len(pattern) and q[i] == pattern[j]:
                    j += 1
                elif q[i].isupper():
                    break
                i += 1
            answer.append(i == len(q) and j == len(pattern))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
        j = "FB"
        o = [True,False,True,True,False]
        self.assertEqual(s.camelMatch(i,j), o)

    def test_two(self):
        s = Solution()
        i = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
        j = "FoBa"
        o = [True,False,True,False,False]
        self.assertEqual(s.camelMatch(i,j), o)

    def test_three(self):
        s = Solution()
        i = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
        j = "FoBaT"
        o = [False,True,False,False,False]
        self.assertEqual(s.camelMatch(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)