# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a string s and array of pairs of indices in the string pairs
    where pairs[i] = [a,b] indicates 2 indices (0-indexed) of the
    string.

    The characters for at a pair of indices can be swapped any number of
    times.

    Return the lexicographically smallest string that s can be changed
    to after using the swaps.
    '''
    # attempt to use leetcode dfs description
    # https://leetcode.com/problems/smallest-string-with-swaps/solution/
    def smallestStringWithSwaps_dfs_fails(self, s: str, pairs: List[List[int]]) -> str:
        # create graph of indexes and edges
        graph = {i:[] for i in range(len(s))}
        for i,j in pairs:
            graph[i].append(j)
            graph[j].append(i)
        # find all components in graph (ie nodes that are connected)
        nodes = {i for i in range(len(s))}
        components = []
        while nodes:
            components.append(set())
            n = nodes.pop()
            components[-1].add(n)
            edges = graph[n]
            while edges:
                m = []
                for e in edges:
                    if e not in components[-1]:
                        nodes.remove(e)
                        components[-1].add(e)
                        m += graph[e]
                edges = m
        # sort the strings that the componets create
        componentStrings = []
        for c in components:
            cs = ""
            for i in c:
                cs += s[i]
            componentStrings.append(sorted(cs))
        # rebuild the string
        s = [""] * len(s)
        for i, j in zip(components,componentStrings):
            for x, y in zip(i,j):
                s[x] = y
        return "".join(s)

    # derived from leetcode dfs solution
    # https://leetcode.com/problems/smallest-string-with-swaps/solution/
    # E is number of edges and V is number vertices
    # O(E + V log V) time
    # O(E + V) space
    def smallestStringWithSwaps_dfs(self, s: str, pairs: List[List[int]]) -> str:
        # create graph of indexes and edges
        graph = {i:[] for i in range(len(s))}
        for i,j in pairs:
            graph[i].append(j)
            graph[j].append(i)
        # variable to return
        ans = [''] * len(s)
        # find components in graph
        visited = [False] * len(s)
        # dfs search
        def dfs(v, i, c):
            visited[v] = True
            i.append(v)
            c.append(s[v])
            for e in graph[v]:
                if not visited[e]:
                    dfs(e, i, c)
        # check if indices have been visited by dfs
        for i in range(len(s)):
            if not visited[i]:
                indices = []
                characters = []
                dfs(i, indices, characters)
                # sort the found indice character pairs
                indices.sort()
                characters.sort()
                # add to answer
                for i,j in zip(indices, characters):
                    ans[i] = j
        return ''.join(ans)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "dcab"
        j = [[0,3],[1,2]]
        o = "bacd"
        self.assertEqual(s.smallestStringWithSwaps(i,j), o)

    def test_two(self):
        s = Solution()
        i = "dcab"
        j = [[0,3],[1,2],[0,2]]
        o = "abcd"
        self.assertEqual(s.smallestStringWithSwaps(i,j), o)

    def test_three(self):
        s = Solution()
        i = "cba"
        j = [[0,1],[1,2]]
        o = "abc"
        self.assertEqual(s.smallestStringWithSwaps(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)