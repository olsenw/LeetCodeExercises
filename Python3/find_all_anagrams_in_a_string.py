# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given two strings s and p, return an array of all the start indices
    of p's anagrams in s. Answer may be returned in any order.

    An anagram is a word or phrase formed by rearranging the letters of
    a different word or phrase, typically using all the original letters
    exactly once.
    '''
    # time limit exceeded on leetcode
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # early bailout if there exists character in p not in s
        if len(set(p) - set(s)):
            return []
        from collections import Counter
        pc = Counter(p)
        ans = []
        # indexes allowing window length p over string s 
        for i in range(0, len(s) - len(p) + 1):
            if pc == Counter(s[i:i+len(p)]):
                ans.append(i)
        return ans

    # works... but slower than like
    def findAnagrams_alt(self, s: str, p: str) -> List[int]:
        from collections import Counter
        pc = Counter(p)
        sc = Counter(s[0:len(p)])
        ans = [0] if pc == sc else []
        # indexes allowing window length p over string s 
        for i in range(1, len(s) - len(p) + 1):
            sc[s[i-1]] -= 1
            sc[s[i+len(p)-1]] += 1
            if pc == sc:
                ans.append(i)
        return ans

    # about average... probably subtle improvements to speed
    def findAnagrams_alt_skips(self, s: str, p: str) -> List[int]:
        from collections import Counter
        pc = Counter(p)
        ans = []
        n = len(s) - len(p) + 1
        i = 0
        while i < n:
            if s[i+len(p)-1] not in pc:
                i = i+len(p)
            if pc == Counter(s[i:i+len(p)]):
                ans.append(i)
                break
            i += 1
        i += 1
        while i < n:
            if s[i-1] == s[i+len(p)-1]:
                ans.append(i)
            else:
                while i < n:
                    if s[i+len(p)-1] not in pc:
                        i = i+len(p)
                    if pc == Counter(s[i:i+len(p)]):
                        ans.append(i)
                        break
                    i += 1
            i += 1
        return ans

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "cbaebabacd"
        c = "abc"
        o = [0,6]
        self.assertEqual(s.findAnagrams(i, c), o)
        self.assertEqual(s.findAnagrams_alt(i, c), o)
        self.assertEqual(s.findAnagrams_alt_skips(i, c), o)

    def test_two(self):
        s = Solution()
        i = "abab"
        c = "ab"
        o = [0,1,2]
        self.assertEqual(s.findAnagrams(i, c), o)
        self.assertEqual(s.findAnagrams_alt(i, c), o)
        self.assertEqual(s.findAnagrams_alt_skips(i, c), o)

    def test_three(self):
        s = Solution()
        i = "abaacbabc"
        c = "abc"
        o = [3,4,6]
        self.assertEqual(s.findAnagrams(i, c), o)
        self.assertEqual(s.findAnagrams_alt(i, c), o)
        self.assertEqual(s.findAnagrams_alt_skips(i, c), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)