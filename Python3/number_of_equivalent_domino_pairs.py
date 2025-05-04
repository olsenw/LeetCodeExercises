# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a list of dominos, dominos[i] = [a,b] is equivalent to
    dominoes[j] = [c,d] if and only if either (a==c and b==d), or
    (a==d and b==c) - that is, one domino can be rotated to be equal to another
    domino.

    Return the number of pairs (i,j) for which o <= i < j < dominos.length, and
    dominos[i] is equivalent to dominoes[j]
    '''
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        c = Counter()
        answer = 0
        for d in dominoes:
            t = tuple(sorted(d))
            if t in c:
                answer += c[t]
            c[t] += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2],[2,1],[3,4],[5,6]]
        o = 1
        self.assertEqual(s.numEquivDominoPairs(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,2],[1,2],[1,1],[1,2],[2,2]]
        o = 3
        self.assertEqual(s.numEquivDominoPairs(i), o)

    def test_three(self):
        s = Solution()
        i = [[1,2],[2,1],[1,2],[1,2],[1,2]]
        o = 10
        self.assertEqual(s.numEquivDominoPairs(i), o)

    def test_four(self):
        s = Solution()
        i = [[1,2],[2,1],[1,2],[1,2],[1,2],[1,2]]
        o = 15
        self.assertEqual(s.numEquivDominoPairs(i), o)

    def test_five(self):
        s = Solution()
        i = [[1,2],[2,1],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2]]
        o = 36
        self.assertEqual(s.numEquivDominoPairs(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)