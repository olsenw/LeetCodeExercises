# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict, deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    On a 2D plane, there n stones placed at some integer coordinates points.
    Each coordinate point may have at most one stone.

    A stone can be removed if it shares either the same row or the same column
    as another stone that has not been removed.

    Given an array stones of length n where stones[i] = [xi, yi] represents the
    location of the ith stone, return the largest possible number of stones that
    can be removed.
    '''
    # does not consider order of stones removed correctly
    def removeStones_flawed(self, stones: List[List[int]]) -> int:
        rows = defaultdict(set)
        cols = defaultdict(set)
        for x,y in stones:
            rows[x].add(y)
            cols[y].add(x)
        visited = set()
        def dfs(x,y):
            depth = 0
            visited.add((x,y))
            for b in rows[x]:
                if b != y and (x,b) not in visited:
                    depth = max(depth, dfs(x,b) + 1)
            for a in cols[y]:
                if a != x and (a,y) not in visited:
                    depth = max(depth, dfs(a,y) + 1)
            if depth == 0 and len(visited) < len(stones):
                depth = max(dfs(x,y) for x,y in stones if (x,y) not in visited)
            visited.remove((x,y))
            return depth
        return max(dfs(x,y) for x,y in stones)

    def removeStones_slow_flawed(self, stones: List[List[int]]) -> int:
        stones = {(a,b) for a,b in stones}
        def dfs(x,y):
            score = 0
            stones.remove((x,y))
            for a,b in stones:
                # share a row or column and worth one point
                if a == x or b == y:
                    score = max(score, dfs(a,b) + 1)
                # moving to different stone on grid
                else:
                    score = max(score, dfs(a,b))
            stones.add((x,y))
            return score
        return max(dfs(a,b) for a,b in stones)

    # passes but is slow
    # makes use of graph theory to solve
    def removeStones(self, stones: List[List[int]]) -> int:
        # number of possible stones to remove
        score = 0
        # graph O(n^2) time to build
        graph = {(x,y):[] for x,y in stones}
        for x,y in stones:
            for a,b in stones:
                if (x == a) ^ (y == b):
                    graph[(x,y)].append((a,b))
        # find size of disconnected subgraphs
        stones = {(x,y) for x,y in stones}
        while stones:
            s = 0
            # perform bfs
            visit = deque([stones.pop()])
            while visit:
                v = visit.popleft()
                s += 1
                for n in graph[v]:
                    if n in stones:
                        stones.remove(n)
                        visit.append(n)
            # increment stones that can be removed
            score += s - 1
        return score

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
        o = 5
        self.assertEqual(s.removeStones(i), o)

    def test_two(self):
        s = Solution()
        i = [[0,0],[0,2],[1,1],[2,0],[2,2]]
        o = 3
        self.assertEqual(s.removeStones(i), o)

    def test_three(self):
        s = Solution()
        i = [[0,0]]
        o = 0
        self.assertEqual(s.removeStones(i), o)

    def test_four(self):
        s = Solution()
        i = [[0,0],[1,1],[4,4],[2,2],[3,3],[5,5]]
        o = 0
        self.assertEqual(s.removeStones(i), o)

    def test_five(self):
        s = Solution()
        i = [[3,2],[3,1],[4,4],[1,1],[0,2],[4,0]]
        o = 4
        self.assertEqual(s.removeStones(i), o)

    def test_six(self):
        s = Solution()
        i = [[8,3],[6,8],[4,3],[8,0],[2,2],[2,1],[7,4],[8,7],[1,7],[3,7],[8,4]]
        o = 8
        self.assertEqual(s.removeStones(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)