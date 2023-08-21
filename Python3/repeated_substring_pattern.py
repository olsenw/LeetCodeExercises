# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s, check if it can be constructed by taking a substring of it
    and appending multiple copies of the substring together.
    '''
    # brute force O(n^2)
    def repeatedSubstringPattern(self, s: str) -> bool:
        pattern = s[0]
        for i in range(1, len(s) // 2 + 1):
            j = i
            while j + len(pattern) <= len(s):
                if pattern != s[j:j+len(pattern)]:
                    break
                j += len(pattern)
            if j == len(s):
                return True
            pattern += s[i]
        return False
    
    # O(n sqrt(n))
    # instead of above only considers valid divisors of length
    # https://leetcode.com/problems/repeated-substring-pattern/editorial/
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n//2 + 1):
            if n % i == 0:
                pattern = s[:i] * (n // i)
                if s == pattern:
                    return True
        return False
    
    # based on string concatenation editorial
    # https://leetcode.com/problems/repeated-substring-pattern/editorial/
    # proof is interesting
    def repeatedSubstringPattern(self, s: str) -> bool:
        t = s + s
        # check if s is a subsequence of t
        return s in t[1:-1]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abab"
        o = True
        self.assertEqual(s.repeatedSubstringPattern(i), o)

    def test_two(self):
        s = Solution()
        i = "aba"
        o = False
        self.assertEqual(s.repeatedSubstringPattern(i), o)

    def test_three(self):
        s = Solution()
        i = "abcabcabcabc"
        o = True
        self.assertEqual(s.repeatedSubstringPattern(i), o)

    def test_four(self):
        s = Solution()
        i = "a"
        o = False
        self.assertEqual(s.repeatedSubstringPattern(i), o)

    def test_five(self):
        s = Solution()
        i = "a" * 100000
        o = True
        self.assertEqual(s.repeatedSubstringPattern(i), o)

    def test_six(self):
        s = Solution()
        i = "a" * 9999 + "b"
        o = False
        self.assertEqual(s.repeatedSubstringPattern(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)