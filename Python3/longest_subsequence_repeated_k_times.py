# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    Given a string s of length n, and an integer k. Find the longest subsequence
    repeated k times in string s.

    A subsequence is a string that can be derived from another string be
    deleting some or no characters without changing the order of the remaining
    characters.

    A subsequence seq is repeated k times in the string s if seq * k is a
    subsequence of s, where seq * k represents a string constructed by
    concatenating seq k times.

    Return the longest subsequence repeated k times in string s. If multiple
    such subsequences are found, return the lexicographically largest one. If
    there is no such subsequence, return an empty string.
    '''
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        def validate(seq:str) -> bool:
            if len(seq) == 0:
                return True
            seq *= k
            i = 0
            for j in s:
                if seq[i] == j:
                    i += 1
                    if i == len(seq):
                        return True
            return False
        c = Counter(s)
        o = sorted((i for i in c if c[i] >= k), reverse=True)
        def backtrack(seq:str) -> str:
            if not validate(seq):
                return ""
            answer = seq
            for i in o:
                if c[i] > 0:
                    c[i] -= 1
                    a = backtrack(seq + i)
                    if len(a) > len(answer):
                        answer = a
                    elif len(a) == len(answer):
                        answer = max(answer, a)
                    c[i] += 1
            return answer
        answer = backtrack("")
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "letsleetcode"
        j = 2
        o = "let"
        self.assertEqual(s.longestSubsequenceRepeatedK(i,j), o)

    def test_two(self):
        s = Solution()
        i = "bb"
        j = 2
        o = "b"
        self.assertEqual(s.longestSubsequenceRepeatedK(i,j), o)

    def test_three(self):
        s = Solution()
        i = "ab"
        j = 2
        o = ""
        self.assertEqual(s.longestSubsequenceRepeatedK(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)