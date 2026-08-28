# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    Given two strings s and target, each of length n, consisting of lowercase
    English letters.

    Return the lexicographically smallest string that is both a palindromic
    permutation of s and strictly greater than target. If no such permutation
    exists, return an empty string.
    '''
    # backtracking hint for forming palindrome very useful
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        c = Counter(s)
        # impossible to make a palindrome from s
        if sum(c[i] % 2 for i in c) > 1:
            return ""
        center = ""
        cmax = ord(max(i for i in c))
        cmin = ord(min(i for i in c))
        for i in c:
            if c[i] % 2:
                center = i
        def verify(answer:str) -> bool:
            # return any(a > b for a,b in zip(answer,target))
            for a,b in zip(answer, target):
                if a > b:
                    return True
                elif a < b:
                    return False
            return False
        def backtract(prefix:str,lexi:bool) -> str:
            if len(prefix) == n // 2:
                answer = prefix + center + prefix[::-1]
                return answer if verify(answer) else ""
            t = ord(target[len(prefix)]) if not lexi else cmin
            for i in range(t, cmax+1):
                i = chr(i)
                if i in c and c[i] > 1:
                    c[i] -= 2
                    prefix += i
                    a = backtract(prefix, lexi or prefix[-1] > target[len(prefix) - 1])
                    if a != "":
                        return a
                    prefix = prefix[:-1]
                    c[i] += 2
            return ""
        return backtract("",False)

class UnitTesting(unittest.TestCase):
    # def test_one(self):
    #     s = Solution()
    #     i = "baba"
    #     j = "abba"
    #     o = "baab"
    #     self.assertEqual(s.lexPalindromicPermutation(i,j), o)

    # def test_two(self):
    #     s = Solution()
    #     i = "baba"
    #     j = "bbaa"
    #     o = ""
    #     self.assertEqual(s.lexPalindromicPermutation(i,j), o)

    # def test_three(self):
    #     s = Solution()
    #     i = "abc"
    #     j = "abb"
    #     o = ""
    #     self.assertEqual(s.lexPalindromicPermutation(i,j), o)

    # def test_four(self):
    #     s = Solution()
    #     i = "aac"
    #     j = "abb"
    #     o = "aca"
    #     self.assertEqual(s.lexPalindromicPermutation(i,j), o)

    # def test_five(self):
    #     s = Solution()
    #     i = "abb"
    #     j = "bba"
    #     o = ""
    #     self.assertEqual(s.lexPalindromicPermutation(i,j), o)

    def test_siz(self):
        s = Solution()
        i = "aaaabbbb"
        j = "abbaabba"
        o = "baabbaab"
        self.assertEqual(s.lexPalindromicPermutation(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)