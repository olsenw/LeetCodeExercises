# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from re import search
from turtle import update
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List
from collections import defaultdict

class Solution:
    '''
    Given an array of strings equation that represent relationships between
    variables where each string equations[i] is of length 4 and takes one of two
    different forms: "xi==yi" or "xi!=yi". Here, xi and yi are lowercase letters
    (not necessarily different) that represent one-letter variable names.

    Return true if it is possible to assign integers to variable names so as to
    satisfy all the given equations, or false otherwise.
    '''
    def equationsPossible_fails(self, equations: List[str]) -> bool:
        eq = defaultdict(set)
        nq = defaultdict(set)
        for equation in equations:
            if equation[1] == '!':
                nq[equation[0]].add(equation[-1])
                nq[equation[-1]].add(equation[0])
            else:
                eq[equation[0]].add(equation[-1])
                eq[equation[-1]].add(equation[0])
        for k in eq:
            for v in eq[k]:
                if v in nq[k]:
                    return False
        for k in nq:
            for v in nq[k]:
                if v in eq[k]:
                    return False
        return True

    def equationsPossible_fails_again(self, equations: List[str]) -> bool:
        def bfs(graph, start, target):
            visited = set()
            search = [start]
            while search:
                update = []
                for s in search:
                    if s in visited:
                        continue
                    elif s == target:
                        return True
                    else:
                        visited.add(s)
                        update.extend(graph[s])
                search = update
            return False
        # create a graph of variables
        eq = defaultdict(set)
        nq = defaultdict(set)
        for equation in equations:
            if equation[1] == '!':
                if bfs(eq, equation[0], equation[-1]):
                    return False
                nq[equation[0]].add(equation[-1])
                nq[equation[-1]].add(equation[0])
            else:
                if bfs(nq, equation[0], equation[-1]):
                    return False
                eq[equation[0]].add(equation[-1])
                eq[equation[-1]].add(equation[0])
        return True

    def equationsPossible(self, equations: List[str]) -> bool:
        def bfs(graph, start, target):
            visited = set()
            search = [start]
            while search:
                update = []
                for s in search:
                    if s in visited:
                        continue
                    elif s == target:
                        return True
                    else:
                        visited.add(s)
                        update.extend(graph[s])
                search = update
            return False
        # create a graph of variables
        g = defaultdict(set)
        t = set()
        for e in equations:
            if e[1] == '!':
                t.add((e[0],e[-1]))
            else:
                g[e[0]].add(e[-1])
                g[e[-1]].add(e[0])
        return not any(bfs(g,a,b) for a,b in t)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["a==b","b!=a"]
        o = False
        self.assertEqual(s.equationsPossible(i), o)

    def test_two(self):
        s = Solution()
        i = ["b==a","a==b"]
        o = True
        self.assertEqual(s.equationsPossible(i), o)

    def test_three(self):
        s = Solution()
        i = ["b==a","a==b","c==a"]
        o = True
        self.assertEqual(s.equationsPossible(i), o)

    def test_four(self):
        s = Solution()
        i = ["b==a","a==b","c==a","b!=c"]
        o = False
        self.assertEqual(s.equationsPossible(i), o)

    def test_five(self):
        s = Solution()
        i = ["a==b","b!=c","c==a"]
        o = False
        self.assertEqual(s.equationsPossible(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)