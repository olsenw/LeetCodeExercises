# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string array words, and an array groups, both arrays having length
    n.

    The hamming distance between two strings of equal length is the number of
    positions at which the corresponding characters are different.

    Select the longest subsequence from an array of indices [0, 1, ..., n-1],
    such that for the subsequence denoted at [i0, i1, ..., ik-1] having length
    k, the following holds:
    * For adjacent indices in the subsequence, their corresponding groups are
      unequal, ie, groups[ij] != groups[ij+1], for each j where 0 < j + 1 < k.
    * words[ij] and words[ij+1] are equal in length, and the hamming distance
      between them is 1, where 0 < j + 1 < k for all indices in the subsequence.
    
    Return a string containing the words corresponding to the indices (in order)
    in the selected subsequence. If there are multiple answer, return any of
    them.
    '''
    # does not account for hamming distance requirement
    def getWordsInLongestSubsequence_fails(self, words: List[str], groups: List[int]) -> List[str]:
        equals = list()
        @cache
        def dp(i:int, j:int) -> list[str]:
            if i == len(equals):
                return []
            answer = dp(i+1, j)
            if equals[i][1] == j:
                return answer
            for k in range(i+1, len(equals)+1):
                a = dp(k, equals[i][1])
                if len(a) + 1 > len(answer):
                    answer = [equals[i][0]] + a
            return answer
        answer = []
        for l in set(len(w) for w in words):
            dp.cache_clear()
            equals = list((w,g) for w,g in zip(words,groups) if len(w) == l)
            a = dp(0,-1)
            if len(a) > len(answer):
                answer = a
        return answer

    def getWordsInLongestSubsequence_bailed(self, words: List[str], groups: List[int]) -> List[str]:
        # @cache
        def hamming(a:str, b:str) -> int:
            if len(a) != len(b):
                return -1
            return sum(i != j for i,j in zip(a,b))
        word = {j:i for i,j in enumerate(words)}
        possible = defaultdict(list)
        n = len(words)
        for i in range(n):
            for j in range(i+1,n):
                if hamming(words[i], words[j]) == 1:
                    possible[words[i]].append(words[j])
        # def dp(i:int, ):
        # return

    # based on hints
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        def hamming(a:str, b:str) -> int:
            if len(a) != len(b):
                return -1
            return sum(i != j for i,j in zip(a,b))
        n = len(words)
        @cache
        def dp(i:int) -> list[str]:
            # just this word
            answer = [words[i]]
            # test if any previous subsequence can be ended with current wor
            for j in range(i-1,-1,-1):
                if hamming(words[i],words[j]) == 1 and groups[i] != groups[j]:
                    a = dp(j)
                    if len(a) + 1 > len(answer):
                        answer = a + [words[i]]
            return answer
        answer = []
        for i in range(n-1,-1,-1):
            a = dp(i)
            if len(a) > len(answer):
                answer = a
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["bab","dab","cab"]
        j = [1,2,2]
        o = ["bab","cab"]
        self.assertEqual(s.getWordsInLongestSubsequence(i,j), o)

    def test_two(self):
        s = Solution()
        i = ["a","b","c","d"]
        j = [1,2,3,4]
        o = ["a","b","c","d"]
        self.assertEqual(s.getWordsInLongestSubsequence(i,j), o)

    def test_three(self):
        s = Solution()
        i = ["baa","ada"]
        j = [1,2]
        o = ["ada"]
        self.assertEqual(s.getWordsInLongestSubsequence(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)