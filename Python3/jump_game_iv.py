# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an array of integer arr, you are initially positioned at the 
    first index of the array.

    In one step you can jump from index i to index:
        i+1 where i+1 < arr.length
        i-1 where i-1 >= 0
        j where arr[i] == arr[j] and i != j
    
    Return the minimum number of steps to reach the last index of the 
    array.
    '''
    # First attempt (correct answers... but super slow) is minJumps_slow
    # Got mad and read the solution from leetcode
    # https://leetcode.com/problems/jump-game-iv/solution/
    # O(N) time     visit each node once (clearing graph prevents N^2)
    # O(N) space
    def minJumps(self, arr: List[int]) -> int:
        # values -> indexes that have this value
        graph = dict()
        for i in range(len(arr)):
            if arr[i] in graph:
                graph[arr[i]].append(i)
            else:
                graph[arr[i]] = [i]
        # BFS
        visited = {0}
        layer = [0]
        jumps = 0

        while layer:
            # all the next nodes to visit after this loop
            nextlayer = []

            # visit/check nodes from last iteration
            for n in layer:
                # did we find end
                if n == len(arr) - 1:
                    return jumps
                
                # deal with duplicate values (ie "jumps")
                for g in graph[arr[n]]:
                    if g not in visited:
                        visited.add(g)
                        nextlayer.append(g)
                
                # never visit duplicates again (redundant search)
                graph[arr[n]].clear()

                # update neighbors
                if n-1 not in visited and n-1 >= 0:
                    visited.add(n-1)
                    nextlayer.append(n-1)
                if n+1 not in visited and n+1 < len(arr):
                    visited.add(n+1)
                    nextlayer.append(n+1)
            
            layer = nextlayer
            jumps += 1

    # basically I messed up the BFS search... so super slow
    #   lots of redundant checks of jumps dictionary (ie lack visited list)
    # creating the graph would also take forever... N^2 time... ouch
    def minJumps_slow(self, arr: List[int]) -> int:
        # for given index what other indexes can be reached
        edges = dict()
        # for given value which indexes have that value
        values = dict()
        # generate graph
        for i in range(len(arr)):
            # add index into edge dictionary
            edges[i] = set()
            # see if can "jump" left
            if i - 1 >= 0:
                edges[i].add(i - 1)
            # see if can "jump" right
            if i + 1 < len(arr):
                edges[i].add(i + 1)
            # update values
            if arr[i] in values:
                # update perviously seen indexes with new edge
                for j in values[arr[i]]:
                    edges[j].add(i)
                    edges[i].add(j)
                values[arr[i]].add(i)
            else:
                values[arr[i]] = {i}
        # print()
        # print(values)
        # print(edges)
        del values

        # BFS starting at index zero
        from collections import deque
        jumps = {0:0}
        d = deque()
        d.append(0)
        while d:
            n = d.popleft()
            for e in edges[n]:
                if e in jumps:
                    jumps[e] = min(jumps[e], jumps[n] + 1)
                else:
                    jumps[e] = jumps[n] + 1
                    d.append(e)

        return jumps[len(arr) - 1]

class UnitTesting(unittest.TestCase):
    def test_zero(self):
        s = Solution()
        i = [5,6,5,7]
        o = 2
        self.assertEqual(s.minJumps_slow(i), o)
        self.assertEqual(s.minJumps(i), o)

    def test_one(self):
        s = Solution()
        i = [100,-23,-23,404,100,23,23,23,3,404]
        o = 3
        self.assertEqual(s.minJumps_slow(i), o)
        self.assertEqual(s.minJumps(i), o)

    def test_two(self):
        s = Solution()
        i = [7]
        o = 0
        self.assertEqual(s.minJumps_slow(i), o)
        self.assertEqual(s.minJumps(i), o)

    def test_three(self):
        s = Solution()
        i = [7,6,9,6,9,6,9,7]
        o = 1
        self.assertEqual(s.minJumps_slow(i), o)
        self.assertEqual(s.minJumps(i), o)

    def test_four(self):
        s = Solution()
        i = [7,7,2,1,7,7,7,3,4,1]
        o = 3
        self.assertEqual(s.minJumps_slow(i), o)
        self.assertEqual(s.minJumps(i), o)

    def test_five(self):
        s = Solution()
        i = [7,7,2,1,7,7,7,3,4,1]
        o = 3
        self.assertEqual(s.minJumps_slow(i), o)
        self.assertEqual(s.minJumps(i), o)

    def test_six(self):
        s = Solution()
        i = [7] * (5 * 10**4)
        i.append(11)
        o = 2
        self.assertEqual(s.minJumps(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)