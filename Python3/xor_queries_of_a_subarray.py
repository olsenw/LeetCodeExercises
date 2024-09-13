# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array arr of positive integers. Also given the array queries where
    queries[i] = [lefti, righti].

    For each query i compute the XOR of elements from lefti to righti (that is,
    arr[lefti] XOR arr[lefti + 1] XOR ... XOR arr[righti]).

    Return an array answer where answer[i] is the answer to the ith query.
    '''
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [0]
        for a in arr:
            prefix.append(a ^ prefix[-1])
        return [prefix[i] ^ prefix[j+1] for i,j in queries]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,3,4,8], [[0,1],[1,2],[0,3],[3,3]]
        o = [2,7,14,8]
        self.assertEqual(s.xorQueries(*i), o)

    def test_two(self):
        s = Solution()
        i = [4,8,2,10], [[2,3],[1,3],[0,0],[0,3]]
        o = [8,0,4,4]
        self.assertEqual(s.xorQueries(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)