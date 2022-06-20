# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Trie:
    def __init__(self):
        # self.trie = [None] * 26
        # self.trie = {chr(i):None for i in range(97, 123)}
        self.trie = dict()
    def update(self, word):
        if isinstance(word, str) and word:
            # key = ord(word[0]) - 97
            key = word[0]
            if key not in self.trie:
                self.trie[key] = Trie()
            self.trie[key].update(word[1:])
        # raise TypeError("Only strings with at length > 0 supported.")
    def paths(self, depth = 0):
        if len(self.trie) == 0:
            return depth + 1
        # paths = []
        # for t in self.trie:
        #     paths += self.trie[t].paths(depth + 1)
        # return paths
        return sum(v.paths(depth + 1) for v in self.trie.values())

class Solution:
    '''
    A valid encoding of an array of words is any reference string s and
    array iindices such that:
    * words.length == indices.length
    * The reference string s ends with the '#' character.
    * For each index indices[i], the substring of s starting from
      indices[i] and up to (but not including) the next '#' character is
      equal to words[i].

    Given an array of words, return the length of the shortest reference
    string s possible of any valid encoding of words.
    '''
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = Trie()
        for w in set(words):
            trie.update(w[::-1])
        # paths = trie.paths()
        # return sum(paths) + len(paths)
        return trie.paths()

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["time", "me", "bell"]
        o = 10
        self.assertEqual(s.minimumLengthEncoding(i), o)

    def test_two(self):
        s = Solution()
        i = ["t"]
        o = 2
        self.assertEqual(s.minimumLengthEncoding(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)