# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a string array words, return the maximum value of
    length(word[i]) * length(word[j]) where the two words do not share
    common letters. If no such two words exist, return 0.
    '''
    def maxProduct(self, words: List[str]) -> int:
        d = [0] * len(words)
        for i, w in enumerate(words):
            for c in w:
                d[i] |= 1 << (ord(c) - ord('a'))
        a = 0
        for i in range(len(d)):
            for j in range(i + 1, len(d)):
                if not d[i] & d[j]:
                    a = max(a, len(words[i]) * len(words[j]))
        return a

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["abcw","baz","foo","bar","xtfn","abcdef"]
        o = 16
        self.assertEqual(s.maxProduct(i), o)

    def test_two(self):
        s = Solution()
        i = ["a","ab","abc","d","cd","bcd","abcd"]
        o = 4
        self.assertEqual(s.maxProduct(i), o)

    def test_three(self):
        s = Solution()
        i = ["a","aa","aaa","aaaa"]
        o = 0
        self.assertEqual(s.maxProduct(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)