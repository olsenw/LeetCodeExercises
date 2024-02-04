# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a list of words, a list of single letters (might be repeating) and a
    list score of every character.

    Return the maximum score of any valid set of words formed by using the given
    letters (words[i] cannot be used two or more times).

    It is not necessary to use all characters in letters and each letter can
    only be used once. Score of letters 'a', 'b', 'c', ..., 'z' is given by
    score[0], score[1], ..., score[25] respectively.
    '''
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        # calculates the score of a given word
        def s(w):
            return sum(score[ord(c) - 97] for c in w)
        # return a tuple of letter counts of iterator
        def t(w):
            letter = [0] * 26
            for i in w:
                letter[ord(i) - 97] += 1
            return tuple(letter)
        # return true if every element in tuple a is greater or equal than tuple b
        def p(a,b):
            return all(i >= j for i,j in zip(a,b))
        # return tuple of each element in b subtracted from each element of a
        def m(a,b):
            return tuple(i - j for i,j in zip(a,b))
        # array of word[i] letter tuple
        n = len(words)
        word = [t(w) for w in words]
        # best score possible for unused words and remaining letter count
        # u = set of used letters (when ith bit set to one means the words[i] been used)
        # l = tuple of characters that can be worked with
        @cache
        def dp(u, l):
            answer = 0
            for i in range(n):
                j = 1 << i
                if not u & j and p(l,word[i]):
                    answer = max(answer, s(words[i]) + dp(u | j, m(l, word[i])))
            return answer
        return dp(0, t(letters))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["dog","cat","dad","good"]
        j = ["a","a","c","d","d","d","g","o","o"]
        k = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
        o = 23
        self.assertEqual(s.maxScoreWords(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = ["xxxz","ax","bx","cx"]
        j = ["z","a","b","c","x","x","x"]
        k = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
        o = 27
        self.assertEqual(s.maxScoreWords(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = ["leetcode"]
        j = ["l","e","t","c","o","d"]
        k = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
        o = 0
        self.assertEqual(s.maxScoreWords(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)