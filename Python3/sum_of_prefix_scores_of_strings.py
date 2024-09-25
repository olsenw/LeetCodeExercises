# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Trie:
    def __init__(self) -> None:
        self.trie = defaultdict(Trie)
        self.count = 0
    def add(self, word):
        curr = self
        for c in word:
            curr = curr.trie[c]
            curr.count += 1
    def sum(self, word):
        answer = 0
        curr = self
        for c in word:
            curr = curr.trie[c]
            answer += curr.count
        return answer

class Solution:
    # brute force hash map
    def sumPrefixScores_brute(self, words: List[str]) -> List[int]:
        c = Counter()
        for w in words:
            for i in range(1,len(w)+1):
                c[w[:i]] += 1
                pass
        answer = []
        for w in words:
            answer.append(sum(c[w[:i]] for i in range(1,len(w)+1)))
        return answer

    # use of Trie data structure
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for w in words:
            trie.add(w)
        return [trie.sum(w) for w in words]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["abc","ab","bc","b"]
        o = [5,4,3,2]
        self.assertEqual(s.sumPrefixScores(i), o)

    def test_two(self):
        s = Solution()
        i = ["abcd"]
        o = [4]
        self.assertEqual(s.sumPrefixScores(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)