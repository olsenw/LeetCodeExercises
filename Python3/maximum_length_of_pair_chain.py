# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of n pairs where pairs[i] = [lefti, righti] and 
    lefti < righti.
    
    A pair p2 = [c,d] follows a pair p1 = [a,b] if b < c. A chain of pairs can
    be formed in this fashion.

    Return the length longest chain which can be formed.

    Not all intervals need to be used. Pairs can be selected in any order.
    '''
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        pairs.sort()
        @cache
        def dp(i):
            answer = 1
            for j in range(i+1, n):
                if pairs[i][1] < pairs[j][0]:
                    answer = max(answer, 1 + dp(j))
            return answer
        return max(dp(i) for i in range(n))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2],[2,3],[3,4]]
        o = 2
        self.assertEqual(s.findLongestChain(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,2],[7,8],[4,5]]
        o = 3
        self.assertEqual(s.findLongestChain(i), o)

    def test_three(self):
        s = Solution()
        i = [[-6,9],[1,6],[8,10],[-1,4],[-6,-2],[-9,8],[-5,3],[0,3]]
        o = 3
        self.assertEqual(s.findLongestChain(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)