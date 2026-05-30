# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

from sortedcontainers import SortedList

class Solution:
    '''
    There exists an infinite number line, with its origin at 0 and extending
    towards the positive x-axis.

    Given a 2D array queries, which contains two types of queries:
    1. For a query of type 1, queries[i] = [1,x]. Build an obstacle at distance
       x from the origin. It is guaranteed that there is no obstacle at distance
       x when the query is asked.
    2. For a query of type 2, queries[i] = [2, x, sz]. Check if it is possible
       to place a block of size sz anywhere in the range [0, x] on the line,
       such that the block entirely lies in the range [0, x]. A block cannot be
       placed if it intersects with any obstacle, but it may touch it. Note that
       the block is not actually placed. Queries are separate.

    Return a boolean array results, where results[i] is true if it is possible
    to place the block specified in the ith query of type 2, and false
    otherwise.
    '''
    # based on Leetcode editorial
    # https://leetcode.com/problems/block-placement-queries/editorial/?envType=daily-question&envId=2026-05-30

    # init (so that class knows about the variables)
    def __int__(self):
        self.segment = []
        self.st = SortedList()
        self.mx = 5 * 10**5

    def update(self, index:int, value:int, p:int, l:int, r:int) -> None:
        # node value in segment tree
        if l == r:
            self.segment[p] = value
            return
        # mid point of the interval
        mid = (l+r) // 2
        # divide interval at index
        if index <= mid:
            self.update(index, value, p * 2, l, mid)
        else:
            self.update(index, value, p * 2 + 1, mid + 1, r)
        # maximum block size for whole interval
        self.segment[p] = max(self.segment[p * 2], self.segment[p * 2 + 1])

    def query(self, L:int, R:int, p:int, l:int, r:int) -> int:
        if L <= l and r <= R:
            return self.segment[p]
        mid = (l + r) // 2
        answer = 0
        if L <= mid:
            answer = max(answer, self.query(L, R, p*2, l, mid))
        if R > mid:
            answer = max(answer, self.query(L, R, p*2 + 1, mid + 1, r))
        return answer

    def getResults(self, queries: List[List[int]]) -> List[bool]:
        # reset Solution between runs
        self.mx = 5 * 10**5
        self.segment = [0] * (self.mx * 4)
        self.st = SortedList([0, self.mx])
        self.update(self.mx, self.mx, 1, 0, self.mx)
        answer = []

        for q in queries:
            # add an obstacle
            if q[0] == 1:
                x = q[1]
                index = min(len(self.st) - 1, self.st.bisect_right(x))
                r = self.st[index]
                l = self.st[index - 1] if index > 0 else self.st[0]
                self.update(x, x-l, 1, 0, self.mx)
                self.update(r, r-x, 1, 0, self.mx)
                self.st.add(x)
            else:
                x, sz = q[1], q[2]
                index  = min(len(self.st) - 1, self.st.bisect_right(x))
                pre = self.st[0] if index == 0 else self.st[index - 1]
                space = max(x - pre, self.query(0, pre, 1, 0, self.mx))
                answer.append(space >= sz)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2],[2,3,3],[2,3,1],[2,2,2]]
        o = [False,True,True]
        self.assertEqual(s.getResults(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]]
        o = [True,True,False]
        self.assertEqual(s.getResults(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)