# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    A transformation sequence from word beginWord to word endWord using
    dictionary wordList is a sequence of words
    beginWord -> S1 -> S2 -> ... -> Sk such that:
    * Every adjacent pair of words differs by a single letter.
    * Every Si for 1 <= i <= k is in wordList. Note that beginWord does
      not need to be in wordList.
    * Sk == endWord

    Given two words, beginWord and endWord, and a dictionary wordList,
    return all the shortest transformation sequences from beginWord to
    endWord, or an empty list if no such sequence exists. Each sequence
    should be returned as a list of the words
    [beginWord, S1, S2, ..., Sk].
    '''
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        graph = {w:[] for w in wordList}
        if endWord not in graph:
            return []
        if beginWord not in graph:
            graph[beginWord] = []
        for a in graph:
            for b in graph:
                if a == b:
                    continue
                diff = 0
                for c,d in zip(a,b):
                    if c != d:
                        diff += 1
                        if diff == 2:
                            break
                if diff == 1:
                    graph[a].append(b)
        #print(graph)
        # bfs
        # keep a depth tracker and nodes reached at that depth
        # then back track from end word
        tracker = dict()
        visited = set()
        stack = [beginWord]
        depth = 0
        while stack:
            tracker[depth] = []
            update = []
            for s in stack:
                if s in visited:
                    continue
                visited.add(s)
                tracker[depth].append(s)
                for g in graph[s]:
                    update.append(g)
            if endWord in visited:
                break
            depth += 1
            stack = update
        # back track from depth and end word
        #print(tracker)
        if endWord not in visited:
            return []
        answer = [[endWord]]
        for d in reversed(range(depth)):
            u = []
            for a in answer:
                b = a[0]
                for c in graph[b]:
                    if c in tracker[d]:
                        u.append([c] + a)
            answer = u
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "hit"
        j = "cog"
        k = ["hot","dot","dog","lot","log","cog"]
        o = [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
        self.assertEqual(s.findLadders(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = "hit"
        j = "cog"
        k = ["hot","dot","dog","lot","log"]
        o = []
        self.assertEqual(s.findLadders(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)