# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two integers n and k, return all possible combinations of k numbers
    chosen from the range [1,n].

    Answer may be returned in any order.
    '''
    # incorrect
    def combine_incorrect(self, n: int, k: int) -> List[List[int]]:
        def pick(s,c):
            if c == 1:
                return [[i] for i in range(s,n+1)]
            answer = []
            for i in range(s,n+1-k+1):
                for j in pick(i + 1, c - 1):
                    answer.append([i] + j)
            return answer
        return pick(1,k)

    # works
    # does not return sorted order
    # pretty fast
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 1:
            return [[i] for i in range(1, n+1)]
        answer = []
        for i in range(n,k-1,-1):
            for j in self.combine(i - 1, k - 1):
                answer.append(j + [i])
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 4
        j = 2
        o = [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
        self.assertEqual(s.combine(i,j), o)

    def test_two(self):
        s = Solution()
        i = 1
        j = 1
        o = [[1]]
        self.assertEqual(s.combine(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)