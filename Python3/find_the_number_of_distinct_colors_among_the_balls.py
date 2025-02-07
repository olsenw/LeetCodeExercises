# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer limit and a 2D array queries of size n x 2.

    There are limit + 1 balls with distinct labels in the range [0, limit].
    Initially, all balls are uncolored. For every query in queries that is of
    the form [x, y], indicating that the x ball should be marked color y. After
    each query find the number of distinct colors among the balls.

    Return an array result of length n, where result[i] denotes the number of
    distinct colors after the ith query.

    Note that when answering a query, lack of a color will not be considered as
    a color.
    '''
    # errors out on large inputs (too much memory used)
    def queryResults_memory_exceeded(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls = [0] * (limit + 1)
        colors = dict()
        answer = []
        for x,y in queries:
            if balls[x] in colors:
                colors[balls[x]].remove(x)
                if len(colors[balls[x]]) == 0:
                    del colors[balls[x]]
            balls[x] = y
            if y not in colors:
                colors[y] = set()
            colors[y].add(x)
            answer.append(len(colors))
        return answer

    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        # balls = [0] * (limit + 1)
        balls = dict()
        colors = dict()
        answer = []
        for x,y in queries:
            if x in balls and balls[x] in colors:
                colors[balls[x]] -= 1
                if colors[balls[x]] == 0:
                    del colors[balls[x]]
            balls[x] = y
            if y not in colors:
                colors[y] = 0
            colors[y] += 1
            answer.append(len(colors))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 4, [[1,4],[2,5],[1,3],[3,4]]
        o = [1,2,2,3]
        self.assertEqual(s.queryResults(*i), o)

    def test_two(self):
        s = Solution()
        i = 4, [[0,1],[1,2],[2,2],[3,4],[4,5]]
        o = [1,2,2,3,4]
        self.assertEqual(s.queryResults(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)