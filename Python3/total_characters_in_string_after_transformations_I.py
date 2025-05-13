# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s and an integer t, representing the number of
    transformations to perform. In one transformation, every character in s is
    replaced according to the following rules:
    * If the character is 'z', replace it with the string "ab".
    * Otherwise, replace it the next character in the alphabet.

    Return the length of the resulting string after exactly t transformations.

    Since the answer may be very large, return it modulo 10**9 + 7.
    '''
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        m = 10**9+7
        @cache
        def dp(c:str,i:int) -> int:
            if ord(c) - ord('a') + i < 26:
                return 1
            t = i - (26 - (ord(c) - ord('a')))
            # return ((dp('a', t) % m) + (dp('b', t) % m)) % m
            return dp('a', t) + dp('b', t)
        answer = 0
        c = Counter(s)
        for i in c:
            a = dp(i,t) * c[i]
            # a = ((dp(i,t) % m) * (c[i] % m)) % m
            answer = answer + a
            # answer = ((answer % m) + (a % m)) % m
        return answer % m

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abcyy"
        j = 2
        o = 7
        self.assertEqual(s.lengthAfterTransformations(i,j), o)

    def test_two(self):
        s = Solution()
        i = "azbk"
        j = 1
        o = 5
        self.assertEqual(s.lengthAfterTransformations(i,j), o)

    def test_three(self):
        s = Solution()
        i = "aaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbccccccccccccccdddddddddddeeeeeeeeffffffffggggghhhiiijjjkkklllmmnnooppqrestuvwxyzzzzzzzzzzzzzzzzz"
        j = 2
        o = 153
        self.assertEqual(s.lengthAfterTransformations(i,j), o)

    def test_four(self):
        s = Solution()
        i = "aaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbccccccccccccccdddddddddddeeeeeeeeffffffffggggghhhiiijjjkkklllmmnnooppqrestuvwxyzzzzzzzzzzzzzzzzz"
        j = 10000
        o = 179166760
        self.assertEqual(s.lengthAfterTransformations(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)