# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an integer n, count how many strings of length n can be formed
    under the following rules:
    * Each character is a lower case vowel ("aeiou")
    * Each vowel a may only be followed by an e
    * Each vowel e may only be followed by an a or an i
    * Each vowel i may not be followed by another i
    * Each vowel o may only be followed by an i or a u
    * Each vowel u may only be followed by an a

    Since the answer may be too large, return it modulo 10^9 + 7.
    '''
    def countVowelPermutation_first(self, n: int) -> int:
        do = {c:1 for c in "aeiou"}
        for _ in range(n - 1):
            c = {c:0 for c in "aeiou"}
            for k in do:
                if k == 'a':
                    c[k] = do['e']
                elif k == 'e':
                    c[k] = do['a'] + do['i']
                elif k == 'i':
                    c[k] = do['a'] + do['e'] + do['o'] + do['u']
                elif k == 'o':
                    c[k] = do['i'] + do['u']
                else:
                    c[k] = do['a']
            
            do = c
        return sum(do.values()) % (10**9+7)

    def countVowelPermutation(self, n: int) -> int:
        # a:0 e:1 i:2 o:3 u:4
        dp = [1] * 5
        n -= 1
        while n:
            n -= 1
            dp = [
                dp[1],
                dp[0] + dp[2],
                dp[0] + dp[1] + dp[3] + dp[4],
                dp[2] + dp[4],
                dp[0]
            ]
        return sum(dp) % (10**9+7)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 1
        o = 5
        self.assertEqual(s.countVowelPermutation(i), o)

    def test_two(self):
        s = Solution()
        i = 2
        o = 10
        self.assertEqual(s.countVowelPermutation(i), o)

    def test_three(self):
        s = Solution()
        i = 5
        o = 68
        self.assertEqual(s.countVowelPermutation(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)