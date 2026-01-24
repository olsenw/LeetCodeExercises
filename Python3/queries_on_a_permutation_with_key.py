# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given the array queries of positive integers between 1 and m, process all
    queries[i] (from i=0 to i=queries.length-1) according to the following
    rules:
    * Start with the permutation P=[1,2,3,...,m]
    * For the current i, find the position of queries[i] in the permutation P
      (indexing from 0) and then move this at the beginning of the permutation
      P. Notice that the position of queries[i] in P is the result for
      queries[i].
    
    Return an array containing the result for the given queries.
    '''
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        answer = []
        d = deque(range(1,m+1))
        for q in queries:
            answer.append(d.index(q))
            d.remove(q)
            d.appendleft(q)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,1,2,1]
        j = 5
        o = [2,1,2,1]
        self.assertEqual(s.processQueries(i,j), o)

    def test_two(self):
        s = Solution()
        i = [4,1,2,2]
        j = 4
        o = [3,1,2,0]
        self.assertEqual(s.processQueries(i,j), o)

    def test_three(self):
        s = Solution()
        i = [7,5,5,8,3]
        j = 8
        o = [6,5,0,7,5]
        self.assertEqual(s.processQueries(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)