# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

'''
Given an array of points representing integer coordinates of some points
on a 2D place, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhatten
distance between the: |xi - xj| + |yi - yj| where |val| denotes the
absolute value of val.

Return the minimum cost to make all points connected. All points are
connected if there is exactly one simple path between any two points.
'''
# basically find a minimum spanning tree (mst) using Prim's or Kruskal's
# https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/?msclkid=652870ccc50c11ec868d4893a7ed2d38
# https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/?msclkid=6527ec80c50c11eca28d59ec56151382

class Solution:
    # time limit exceeded 65/72 cases
    # O(v^3) where v is number of vertices (3 nested loops)
    def minCostConnectPoints_slow(self, points: List[List[int]]) -> int:
        cost = 0
        visited = [points.pop()]
        while points:
            a,b,c = 0, 0, 10000000
            for x,y in visited:
                for i,j in points:
                    d = abs(x - i) + abs(y - j)
                    if d < c:
                        a,b,c = i,j,d
            visited.append([a,b])
            points.remove([a,b])
            cost += c
        return cost

    # time limit exceeded 65/72 cases
    # O(v^3) where v is number of vertices (3 nested loops)
    def minCostConnectPoints_slow_set(self, points: List[List[int]]) -> int:
        cost = 0
        nodes = {(i,j) for i,j in points[1:]}
        visit = {(points[0][0],points[0][1])}
        while nodes:
            a,b,c = 0,0,10000000
            for x,y in visit:
                for i,j in nodes:
                    d = abs(x - i) + abs(y - j)
                    if d < c:
                        a,b,c = i,j,d
            nodes.remove((a,b))
            visit.add((a,b))
            cost += c
        return cost

    # based on discussion post by zayne-siew
    # https://leetcode.com/problems/min-cost-to-connect-all-points/discuss/1982821/Python-Simple-MST-with-Explanation
    # similar idea to above but much smarter in loops and data storage
    # here a dictionary of points keeps the weight of shortest edge to a
    # given point
    # O(v^2) where v is number of vertices (2 nested loops)
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # graph of all nodes not in tree and smallest edge to mst
        d = {(x,y):10000000 for x,y in points[1:]}
        d[(points[0][0], points[0][1])] = 0
        # running cost of minimum spanning tree
        cost = 0
        # keep going until all nodes have been taken
        while d:
            # take node with smallest edge
            x,y = min(d, key=lambda k: d[k])
            cost += d.pop((x,y))
            # update all nodes with smallest edge to mst
            # in this case check if there is a shorter edge to taken node
            for i,j in d:
                d[(i,j)] = min(d[(i,j)], abs(x-i)+abs(y-j))
        return cost

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0,0],[2,2],[3,10],[5,2],[7,0]]
        o = 20
        self.assertEqual(s.minCostConnectPoints(i), o)

    def test_two(self):
        s = Solution()
        i = [[3,12],[-2,5],[-4,1]]
        o = 18
        self.assertEqual(s.minCostConnectPoints(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)