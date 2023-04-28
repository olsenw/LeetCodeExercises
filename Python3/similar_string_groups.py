# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Two strings X and Y are similar if it is possible to swap two letters (in
    different positions) of X, such that it equals Y. Two strings X and Y are
    also similar if they are equal.

    For example "tars" and "rats" are similar (swapping at positions 0 and 2),
    and "rats" and "arts" are similar, but "star" is not similar to "tars",
    "rats", or "arts".

    Together, these form two connected groups by similarity: {"tars", "rats",
    "arts"} and {"star"}. Notice that "tars" and "arts" in the same group even
    though they are not similar. Formally, each group is such that a word is in
    the group if and only if it is similar to at least one other word in the
    group.

    Given a list of strings where every string in strs is an anagram of every
    other string in strs. How many groups are there?
    '''
    # editorial pointed out how to make this a graph problem
    def numSimilarGroups(self, strs: List[str]) -> int:
        graph = {i:[] for i in range(len(strs))}
        # check all pairs of words
        for i in range(len(strs)):
            a = strs[i]
            for j in range(i+1,len(strs)):
                b = strs[j]
                # check if similar
                c = 0
                for k in range(len(a)):
                    if a[k] != b[k]:
                        c += 1
                # add edge connecting similar words
                if c == 0 or c == 2:
                    graph[i].append(j)
                    graph[j].append(i)
        # count the number components in the graph
        c = 0
        v = set()
        for i in range(len(strs)):
            if i in v:
                continue
            c += 1
            # breath first search
            q = deque([i])
            while q:
                n = q.popleft()
                if n in v:
                    continue
                v.add(n)
                for j in graph[n]:
                    q.append(j)
        return c

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["tars","rats","arts","star"]
        o = 2
        self.assertEqual(s.numSimilarGroups(i), o)

    def test_two(self):
        s = Solution()
        i = ["omv","ovm"]
        o = 1
        self.assertEqual(s.numSimilarGroups(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)