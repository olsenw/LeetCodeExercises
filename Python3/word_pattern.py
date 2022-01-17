# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a pattern and a string s, find if s follows the same pattern.

    Note follow means a full match, such that there is a bijection 
    between a letter in pattern and a non-empty word in s.
    '''
    def wordPattern(self, pattern: str, s: str) -> bool:
        def word(i):
            j = i
            while j < len(s) and s[j] != ' ':
                j += 1
            return s[i:j]
        w = word(0)
        i = len(w) + 1
        p = 0
        words = {w: pattern[p]}
        patterns = {pattern[p]}
        w = word(i)
        while w:
            i += len(w) + 1
            if p+1 < len(pattern):
                p += 1
            else:
                p = 0
            if w in words:
                if words[w] != pattern[p]:
                    return False
            else:
                if pattern[p] in patterns:
                    return False
                words[w] = pattern[p]
                patterns.add(pattern[p])
            w = word(i)
        if p != len(pattern) - 1:
            return False
        return True

    # this fails the case of pattern = "abba" s = "dog dog dog dog"
    # because word associated with a should not be same as b
    # I disagree because problem does not state this contraint...
    def wordPattern_fails(self, pattern: str, s: str) -> bool:
        def word(i):
            j = i
            while j < len(s) and s[j] != ' ':
                j += 1
            return (i, j - 1)
        words = dict()
        i = 0
        p = 0
        words[pattern[p]] = word(i)
        i = words[pattern[p]][1] + 2
        while i < len(s):
            # next pattern to check
            if p+1 < len(pattern):
                p += 1
            else:
                p = 0
            # check word
            if pattern[p] in words:
                x,y = words[pattern[p]]
                for i in range(i, len(s)):
                    if s[i] == " ":
                        break
                    if x > y or s[i] != s[x]:
                        return False
                    x += 1
                i += 1
            else:
                # new pattern word
                words[pattern[p]] = word(i)
                i = words[pattern[p]][1] + 2
        if p != len(pattern) - 1:
            return False
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        p = "abba"
        i = "dog cat cat dog"
        o = True
        self.assertEqual(s.wordPattern(p, i), o)

    def test_two(self):
        s = Solution()
        p = "abba"
        i = "dog cat cat fish"
        o = False
        self.assertEqual(s.wordPattern(p, i), o)

    def test_three(self):
        s = Solution()
        p = "aaaa"
        i = "dog cat cat dog"
        o = False
        self.assertEqual(s.wordPattern(p, i), o)

    def test_four(self):
        s = Solution()
        p = "abca"
        i = "dog cat fish dog dog cat fish dog"
        o = True
        self.assertEqual(s.wordPattern(p, i), o)

    def test_five(self):
        s = Solution()
        p = "abc"
        i = "dog cat"
        o = False
        self.assertEqual(s.wordPattern(p, i), o)

    def test_six(self):
        s = Solution()
        p = "abba"
        i = "dog dog dog dog"
        o = False
        self.assertEqual(s.wordPattern(p, i), o)

    def test_seven(self):
        s = Solution()
        p = "abba"
        i = "fish whoops helloworld fish"
        o = False
        self.assertEqual(s.wordPattern(p, i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)