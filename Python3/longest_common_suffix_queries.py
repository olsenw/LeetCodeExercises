# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Trie:
    def __init__(self):
        self.t: Dict[str,Trie] = defaultdict(Trie)
        self.i: List[int] = []
    
    def add(self, word:str, index:int) -> None:
        self.i.append(index)
        if not word:
            return
        self.t[word[-1]].add(word[:-1], index)

    def suffix(self, word:str) -> int:
        if not word:
            return self.i[0]
        if word[-1] not in self.t:
            return self.i[0]
        return self.t[word[-1]].suffix(word[:-1])

class Solution:
    '''
    Given two arrays of strings wordsContainer and wordsQuery.

    For each wordQuery[i], find a string from wordsContainer that has the
    longest common suffix with wordsQuery[i]. If there are two or more strings
    in wordsContainer that share the longest common suffix, find the string that
    is the smallest in length. If there are two or more such strings that have
    the same smallest length, find the one that occurred earlier in
    wordsContainer.

    Return an array of integers ans, where ans[i] is the index of the string in
    wordsContainer that has the longest common suffix with wordsQuery[i].
    '''
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        n = len(wordsContainer)
        wordsOrder = sorted([i for i in range(n)], key=lambda x: (len(wordsContainer[x]), x))
        t = Trie()
        for i in wordsOrder:
            t.add(wordsContainer[i], i)
        answer = []
        for q in wordsQuery:
            answer.append(t.suffix(q))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["abcd","bcd","xbcd"]
        j = ["cd","bcd","xyz"]
        o = [1,1,1]
        self.assertEqual(s.stringIndices(i,j), o)

    def test_two(self):
        s = Solution()
        i = ["abcdefgh","poiuygh","ghghgh"]
        j = ["gh","acbfgh","acbfegh"]
        o = [2,0,2]
        self.assertEqual(s.stringIndices(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)