# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a string s, return the number of palindromic substrings in it.

    A string is a palindrome when it reads the same backwards as
    forward.

    A substring is a contiguous sequence of characters within the
    string.
    '''
    # based on solution from jameschien
    # https://leetcode.com/problems/palindromic-substrings/discuss/390727/DP-solution-Step-by-Step!!
    def countSubstrings(self, s: str) -> int:
        # Dynamic programming matrix where lower triangle indicates if
        # characters from index i to index j are a palindrome.
        # Diagonal is all ones because single letters are a palindrome.
        #   A B A B
        # A T
        # B F T
        # A T F T
        # B F T F T
        dp = [[False] * len(s) for _ in range(len(s))]
        a = 0
        for i in range(len(s)):
            for j in range(i, -1, -1):
                # basic condition is outer characters must be same
                if s[i] == s[j]:
                    # basic case of single character along diagonal
                    # looking up if sub sequence was a palindrome
                    if i - j < 2 or dp[i-1][j+1]:
                        a += 1
                        dp[i][j] = True
        return a

    # leetcode solutions sample 104ms code
    # https://leetcode.com/submissions/api/detail/647/python3/104/
    # saved for reference
    # does similar pattern to above, but does not cache results
    def countSubstrings_faster(self, s: str) -> int:
        answer = len(s)
        N = answer
        
        for i in range(N - 1):
            
            left, right = i - 1, i + 1
        
            
            while right < N and s[i] == s[right]:
                right += 1
                answer += 1
                
            
            while left >= 0 and right < N and s[left] == s[right]:
                left -= 1
                right += 1
                answer += 1
        
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abc"
        o = 3
        self.assertEqual(s.countSubstrings(i), o)

    def test_two(self):
        s = Solution()
        i = "aaa"
        o = 6
        self.assertEqual(s.countSubstrings(i), o)

    def test_three(self):
        s = Solution()
        i = "fdsklf"
        o = 6
        self.assertEqual(s.countSubstrings(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)