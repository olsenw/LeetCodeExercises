# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    Given two strings word1 and word2.

    A string x is called almost equal to y if it is possible to change at most
    one character in x to make it identical to y.

    A sequence of indices seq is called valid if:
    * The indices are sorted in ascending order.
    * Concatenating the characters at these indices in word1 in the same order
      results in a string that is almost equal to word2.

    Return an array of size word2.length representing the lexicographically
    smallest valid sequence of indices. If no such sequence of indices exists,
    return an empty array.

    Note that the answer must represent the lexicographically smallest array,
    not the corresponding string formed by those indices.
    '''
    # does not build sequence correctly
    def validSequence_fails(self, word1: str, word2: str) -> List[int]:
        m = len(word1)
        n = len(word2)
        # hint 1 - longest suffix of word2 in word1 starting at index i
        dp = [0] * (m+1)
        # hint 2 - dp relation
        for i in range(m-1,-1,-1):
            if dp[i+1] < n and word1[i] == word2[n - dp[i+1] - 1]:
                dp[i] = dp[i+1] + 1
            else:
                dp[i] = dp[i+1]
        # hint 3 - greedy select answer
        answer = []
        i = 0
        while i < m:
            if word1[i] == word2[len(answer)]:
                answer.append(i)
            i += 1
            if len(answer) - 1 == dp[i]:
                answer.append(i)
                break
        while i < m and word1[i] != word2[len(answer)]:
            if word1[i] < word1[answer[-1]]:
                answer[-1] = i
            i += 1
        while i < m:
            if word1[i] == word2[len(answer)]:
                answer.append(i)
            i += 1
        return answer if len(answer) == n else []

    # based on leetcode editorial
    # https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/editorial/?envType=daily-question&envId=2026-08-08
    def validSequence(self, word1: str, word2: str) -> List[int]:
        m = len(word1)
        n = len(word2)
        last = [-1] * n
        j = n - 1
        for i in range(m-1,-1,-1):
            if j >= 0 and word1[i] == word2[j]:
                last[j] = i
                j -= 1
        answer = []
        skip = 0
        j = 0
        for i,c in enumerate(word1):
            if j == n:
                break
            if c == word2[j] or skip == 0 and (j == n-1 or i < last[j+1]):
                skip += c != word2[j]
                answer.append(i)
                j += 1
        return answer if j == n else []

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "vbcca"
        j = "abc"
        o = [0,1,2]
        self.assertEqual(s.validSequence(i,j), o)

    def test_two(self):
        s = Solution()
        i = "bacdc"
        j = "abc"
        o = [1,2,4]
        self.assertEqual(s.validSequence(i,j), o)

    def test_three(self):
        s = Solution()
        i = "aaaaaa"
        j = "aaabc"
        o = []
        self.assertEqual(s.validSequence(i,j), o)

    def test_four(self):
        s = Solution()
        i = "abc"
        j = "ab"
        o = [0,1]
        self.assertEqual(s.validSequence(i,j), o)

    def test_five(self):
        s = Solution()
        i = "aaaaaac"
        j = "aaabc"
        o = [0,1,2,3,6]
        self.assertEqual(s.validSequence(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)