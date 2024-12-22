# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import bisect
from collections import deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed array heights of positive integers, where heights[i]
    represents the height of the ith building.

    If a person is in building i, they can move to any other building j if and
    only if i < j and heights[i] < heights[j].

    Given an array queries where queries[i] = [ai, bi]. On the ith query Alice
    is in building ai while Bob is in building bi.

    Return an array ans where ans[i] is the index of the leftmost building where
    Alice and Bob can meet on the ith query. If Alice and Bob cannot move to a
    common building on query i, set ans[i] to -1.
    '''
    # based on hints
    def leftmostBuildingQueries_fails(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        answer = [-1] * len(queries)
        queries = [[x,y,i] if x < y else [y,x,i] for i,(x,y) in enumerate(queries)]
        queries = sorted(queries, key=lambda x:(-x[1],-x[0]))
        # monotonically decreasing stack [beginning of stack is end of heights]
        mono = []
        for i in range(len(heights)-1,queries[0][1],-1):
            while mono and heights[i] >= mono[-1][0]:
                mono.pop()
            mono.append((heights[i],i))
        for x,y,i in queries:
            # need to find building that both can be in
            while mono and heights[y] >= mono[-1][0]:
                mono.pop()
            # same building, or can move to building y
            if heights[x] <= heights[y]:
                answer[i] = y
            elif mono and heights[x] < mono[-1][0]:
                answer[i] = mono[-1][1]
            mono.append((heights[y],y))
        return answer

    # based on hints
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        answer = [-1] * len(queries)
        queries = [[x,y,i] if x < y else [y,x,i] for i,(x,y) in enumerate(queries)]
        queries = sorted(queries, key=lambda x:(-x[1],-x[0]))
        # monotonically increasing stack (pop/push from front)
        mono = deque([(0,len(heights)-1)])
        for x,y,i in queries:
            for j in range(mono[0][1],y-1,-1):
                while mono and heights[j] >= mono[0][0]:
                    mono.popleft()
                mono.appendleft((heights[j],j))
            # same building, or can move to building y
            if x == y or heights[x] < heights[y]:
                answer[i] = y
                pass
            # need building greater than y
            else:
                j = bisect.bisect(mono,heights[x],key=lambda x:x[0])
                if j < len(mono) and heights[x] < mono[j][0]:
                    answer[i] = mono[j][1]
                pass
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [6,4,8,5,2,7]
        j = [[0,1],[0,3],[2,4],[3,4],[2,2]]
        o = [2,5,-1,5,2]
        self.assertEqual(s.leftmostBuildingQueries(i,j), o)

    def test_two(self):
        s = Solution()
        i = [5,3,8,2,6,1,4,6]
        j = [[0,7],[3,5],[5,2],[3,0],[1,6]]
        o = [7,6,-1,4,6]
        self.assertEqual(s.leftmostBuildingQueries(i,j), o)

    def test_three(self):
        s = Solution()
        i = [1,2,1,2,1,2]
        j = [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[1,0],[1,1],[1,2],[1,3],[1,4],[1,5],[2,0],[2,1],[2,2],[2,3],[2,4],[2,5],[3,0],[3,1],[3,2],[3,3],[3,4],[3,5],[4,0],[4,1],[4,2],[4,3],[4,4],[4,5],[5,0],[5,1],[5,2],[5,3],[5,4],[5,5]]
        o = [0,1,3,3,5,5,1,1,-1,-1,-1,-1,3,-1,2,3,5,5,3,-1,3,3,-1,-1,5,-1,5,-1,4,5,5,-1,5,-1,5,5]
        self.assertEqual(s.leftmostBuildingQueries(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)