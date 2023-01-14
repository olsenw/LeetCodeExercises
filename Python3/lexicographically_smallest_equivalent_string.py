# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given two strings of the same length s1 and s2 and another string baseStr.

    s1[i] and s2[i] are equivalent characters. (ie if s1 = "abc" and s2 = "cde",
    then 'a' == 'c', 'b' == 'd' and 'c' == 'e')

    Equivalent characters follow the usual rules of any equivalence relation:
    * Reflexivity: 'a' == 'a'.
    * Symmetry: 'a' == 'b' implies 'b' == 'a'.
    * Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'.

    Return the lexicographically smallest equivalent string of baseStr by using
    the equivalency information from s1 and s2.
    '''
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        g = {c: set() for c in "abcdefghijklmnopqrstuvwxyz"}
        for a,b in zip(s1, s2):
            g[a].add(b)
            g[b].add(a)
        @cache
        def bfs(n: str) -> str:
            answer = n
            visited = set()
            queue = deque([n])
            while queue:
                n = queue.popleft()
                if n in visited:
                    continue
                visited.add(n)
                answer = min(answer, n)
                for c in g[n]:
                    queue.append(c)
            return answer
        return "".join(bfs(c) for c in baseStr)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "parker"
        j = "morris"
        k = "parser"
        o = "makkek"
        self.assertEqual(s.smallestEquivalentString(i,j,k), o)
 
    def test_two(self):
        s = Solution()
        i = "hello"
        j = "world"
        k = "hold"
        o = "hdld"
        self.assertEqual(s.smallestEquivalentString(i,j,k), o)
        
    def test_three(self):
        s = Solution()
        i = "leetcode"
        j = "programs"
        k = "sourcecode"
        o = "aauaaaaada"
        self.assertEqual(s.smallestEquivalentString(i,j,k), o)
        

if __name__ == '__main__':
    unittest.main(verbosity=2)