# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

'''
Helper class that implements a Trie data structure.
'''
class Trie:
    def __init__(self):
        self.t = dict()
        self.i = set()
    def add(self, c, i):
        if c not in self.t:
            self.t[c] = Trie()
        self.t[c].i.add(i)
        return self.t[c]
    def contains(self, c):
        if c in self.t:
            return self.t[c]
        return None

'''
Design and implement a special dictionary with some words in it by a
prefix and a suffix.
'''
class WordFilter:
    '''
    Initializes the object with the words in the dictionary.
    '''
    def __init__(self, words: List[str]):
        self.w = {w:i for i,w in enumerate(words)}
        self.prefix = Trie()
        self.suffix = Trie()
        for w in self.w:
            t = self.prefix
            for c in w:
                t = t.add(c, self.w[w])
            t = self.suffix
            for c in reversed(w):
                t = t.add(c, self.w[w])
        pass

    '''
    Returns the index of the word in the dictionary which has the prefix
    prefix and suffix suffix. If there is more than one valid index,
    return the largest of them. If there is no such word in the
    dictionary, return -1.
    '''
    def f(self, prefix: str, suffix: str) -> int:
        p = self.prefix
        for c in prefix:
            p = p.contains(c)
            if not p:
                return -1
        s = self.suffix
        for c in reversed(suffix):
            s = s.contains(c)
            if not s:
                return -1
        m = p.i & s.i
        if m:
            # return max(m, key=lambda x: len(self.w[x]))
            return max(m)
        return -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = WordFilter(["apple"])
        self.assertEqual(s.f("a", "e"), 0)
    def test_two(self):
        s = WordFilter(["apple", "affffe"])
        self.assertEqual(s.f("a", "e"), 1)
    def test_three(self):
        s = WordFilter(["apple", "affffe"])
        self.assertEqual(s.f("f", "f"), -1)

    def test_four(self):
        s = WordFilter(["cabaabaaaa","ccbcababac","bacaabccba","bcbbcbacaa","abcaccbcaa","accabaccaa","cabcbbbcca","ababccabcb","caccbbcbab","bccbacbcba"])
        a = [["bccbacbcba","a"],["ab","abcaccbcaa"],["a","aa"],["cabaaba","abaaaa"],["cacc","accbbcbab"],["ccbcab","bac"],["bac","cba"],["ac","accabaccaa"],["bcbb","aa"],["ccbca","cbcababac"]]
        o = [9,4,5,0,8,1,2,5,3,1]
        for (i,j),k in zip(a, o):
            self.assertEqual(s.f(i, j), k)

if __name__ == '__main__':
    unittest.main(verbosity=2)