# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import bisect
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer n representing the number of nodes in a graph, labeled from
    0 to n - 1.

    Also given an integer array nums of length n and in integer maxDiff.

    An undirected edge exists between nodes i and j if the absolute difference
    between nums[i] and nums[j] is at most maxDiff
    (ie |nums[i] - nums[j]| <= maxDiff).

    Also given a 2D integer array queries. For each queries[i] = [ui,vi], find
    the minimum distance between nodes ui and vi. If no path exists between the
    two nodes, return -1 for that query.

    Return an array answer, where answer[i] is the result of the ith query.

    Note: The edges between the nodes are unweighted.
    '''
    # has basic idea of logic correct
    # but need a more efficient way to do queries (current dp is linear, resulting in total O(n^2))
    def pathExistenceQueries_tle(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        sortedNums = sorted((j,i) for i,j in enumerate(nums))
        groups = [-1] * n
        g = 0
        upper = sortedNums[0][0]
        for k,(j,i) in enumerate(sortedNums):
            if j > upper:
                g += 1
            upper = j + maxDiff
            groups[i] = g
            nums[i] = k
        @cache
        def dp(node:int, target:int) -> int:
            if sortedNums[target][0] <= sortedNums[node][0] + maxDiff:
                return 1
            newNode = bisect.bisect_left(sortedNums, sortedNums[node][0] + maxDiff, key=lambda x: x[0])
            while sortedNums[node][0] + maxDiff < sortedNums[newNode][0]:
                newNode -= 1
            return 1 + dp(newNode, target)
        answer = []
        for i,j in queries:
            if groups[i] != groups[j]:
                answer.append(-1)
                continue
            if i == j:
                answer.append(0)
                continue
            jumps = 1
            # a = bisect.bisect_left(sortedNums, (nums[i],i))
            a = nums[i]
            # b = bisect.bisect_left(sortedNums, (nums[j],j))
            b = nums[j]
            node = min(a,b)
            target = max(a,b)
            # while sortedNums[node][0] + maxDiff < sortedNums[target][0]:
            #     newNode = bisect.bisect_left(sortedNums, sortedNums[node][0] + maxDiff, key=lambda x: x[0])
            #     while sortedNums[node][0] + maxDiff < sortedNums[newNode][0]:
            #         newNode -= 1
            #     node = newNode
            #     jumps += 1
            # answer.append(jumps)
            answer.append(dp(node,target))
        return answer

    # Solution based on VIVEK_KUMAR answer
    # https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/solutions/8387302/sorting-two-pointers-binary-lifting-on-l-qgju/?envType=daily-question&envId=2026-07-10
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        sortedNums = sorted(enumerate(nums), key=lambda x:(x[1],x[0]))
        # nums maps to sorted position in sortedNums
        for j, (i, _) in enumerate(sortedNums):
            nums[i] = j
        
        # represent the number of jumps in orders of power
        LOG = 18
        sparse = [[0] * LOG for _ in range(n)]

        right = 0
        for i in range(n):
            if right < i:
                right = i
            while (
                right + 1 < n and
                sortedNums[right + 1][1] - sortedNums[right][1] <= maxDiff and
                sortedNums[right + 1][1] - sortedNums[i][1] <= maxDiff
            ):
                right += 1
            sparse[i][0] = right
        
        for j in range(1,LOG):
            for i in range(n):
                sparse[i][j] = sparse[sparse[i][j - 1]][j - 1]
        
        answer = []
        for u,v in queries:
            a,b = nums[u],nums[v]
            if a > b:
                a,b = b,a
            if a == b:
                answer.append(0)
                continue

            curr, steps = a, 0
            for j in range(LOG - 1, -1, -1):
                if sparse[curr][j] < b:
                    curr = sparse[curr][j]
                    steps += (1 << j)
            
            answer.append(steps + 1 if sparse[curr][0] >= b else -1)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 5
        j = [1,8,3,4,2]
        k = 3
        l = [[0,3],[2,4]]
        o = [1,1]
        self.assertEqual(s.pathExistenceQueries(i,j,k,l), o)

    def test_two(self):
        s = Solution()
        i = 5
        j = [5,3,1,9,10]
        k = 2
        l = [[0,1],[0,2],[2,3],[4,3]]
        o = [1,2,-1,1]
        self.assertEqual(s.pathExistenceQueries(i,j,k,l), o)

    def test_three(self):
        s = Solution()
        i = 3
        j = [3,6,1]
        k = 1
        l = [[0,0],[0,1],[1,2]]
        o = [0,-1,-1]
        self.assertEqual(s.pathExistenceQueries(i,j,k,l), o)

    def test_four(self):
        s = Solution()
        i = 5
        j = [18,14,8,18,0]
        k = 8
        l = [[1,1],[4,0]]
        o = [0,3]
        self.assertEqual(s.pathExistenceQueries(i,j,k,l), o)

    def test_five(self):
        s = Solution()
        i = 6
        j = [91,92,182,179,127,173]
        k = 51
        l = [[2,3],[5,0],[0,0],[2,0],[0,2],[1,1],[0,4],[0,4],[2,5]]
        l = [[2,0],[0,2]]
        o = [1,2,0,3,3,0,1,1,1]
        o = [3,3]
        self.assertEqual(s.pathExistenceQueries(i,j,k,l), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)