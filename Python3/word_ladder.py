# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    A transformation sequence from word beginWord to word endWord using
    a dictionary wordList is a sequence of words beginWord -> s1 -> s2
    -> ... -> sk such that:
    * Every adjacent pair of words differs by a single letter.
    * Every si for 1 <= i <= k is in wordList. Note beginWord does not 
      need to be in wordList.
    * sk == endWord

    Given two words, beginWord and endWord, and a dictionary wordList 
    return the number of words in the shortest transformation sequence
    from beginWord to endWord or 0 if no such sequence exists.
    '''
    # time limit exceeded (should work... maybe)
    # creating the graph takes too much time
    def ladderLength_graph_bfs(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # graph (node:edges)
        d = {i:[] for i in range(len(wordList))}
        # node in graph that endWord is located
        end = -1
        # node in graph that beginWord is located
        start = -1
        # generate graph edges O(n^2) time (cause len(word) max of 10)
        for w in range(len(wordList)):
            if endWord == wordList[w]:
                end = w
            if beginWord == wordList[w]:
                start = w
            for x in d:
                c = 0
                for i, j in zip(wordList[w], wordList[x]):
                    if i != j:
                        c += 1
                if c == 1:
                    d[x].append(w)
        # check endword is in wordList
        if end == -1:
            return 0
        # add begin word
        if start == -1:
            l = []
            for x in d:
                c = 0
                for i, j in zip(beginWord, wordList[x]):
                    if i != j:
                        c += 1
                if c == 1:
                    l.append(x)
            if len(l) == 0:
                return 0
            d[len(wordList)] = l
            start = len(wordList)
        # BFS to find shortest path from begin to end
        from collections import deque
        queue = deque([start])
        seen = {start: 0}
        while queue:
            v = queue.popleft()
            if v == end:
                return seen[v] + 1
            for e in d[v]:
                if e not in seen:
                    seen[e] = seen[v] + 1
                    queue.append(e)
        # unable to find a path
        return 0

    # based off of leetcode discusions
    # https://leetcode.com/problems/word-ladder/discuss/
    # basic idea is to generate next queue item on fly instead of
    # creating a full graph
    def ladderLength_bfs(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import deque
        queue = deque([[beginWord, 0]])
        # trying "optimization" where remove visited words
        words = set(wordList)
        alph = "abcdefghijklmnopqrstuvwxyz"
        while queue:
            w, l = queue.popleft()
            if w == endWord:
                return l + 1
            # generate permutations
            for i in range(len(w)):
                for a in alph:
                    p = w[:i] + a + w[i+1:]
                    if p in words:
                        words.remove(p)
                        queue.append([p, l + 1])
        return 0

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "hit"
        j = "cog"
        k = ["hot","dot","dog","lot","log","cog"]
        o = 5
        self.assertEqual(s.ladderLength_graph_bfs(i, j, k), o)
        self.assertEqual(s.ladderLength_bfs(i, j, k), o)

    def test_two(self):
        s = Solution()
        i = "hit"
        j = "cog"
        k = ["hot","dot","dog","lot","log"]
        o = 0
        self.assertEqual(s.ladderLength_graph_bfs(i, j, k), o)
        self.assertEqual(s.ladderLength_bfs(i, j, k), o)

    def test_three(self):
        s = Solution()
        i = "aaa"
        j = "bbb"
        k = ["aaa", "aab", "abb", "bbb"]
        o = 4
        self.assertEqual(s.ladderLength_graph_bfs(i, j, k), o)
        self.assertEqual(s.ladderLength_bfs(i, j, k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)