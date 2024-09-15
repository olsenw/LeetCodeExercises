# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given the string s; return the size of the longest substring containing each
    vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must
    appear an even number of times.
    '''
    # passes, but is very slow
    def findTheLongestSubstring_passes(self, s: str) -> int:
        answer = 0
        d = {0:0}
        vowels = {'a':1, 'e':2, 'i':4, 'o':8, 'u':16}
        prefix = [0]
        for i,c in enumerate(s, 1):
            if c in vowels:
                prefix.append(prefix[-1] ^ vowels[c])
            if prefix[-1] not in d:
                d[prefix[-1]] = i
            for j in d:
                if j ^ prefix[-1] == 0 and d[j] != i:
                    answer = max(answer, i - d[j])
                    break
        return answer

    def findTheLongestSubstring(self, s: str) -> int:
        answer = 0
        d = {0:0}
        vowels = {'a':1, 'e':2, 'i':4, 'o':8, 'u':16}
        prefix = 0
        for i,c in enumerate(s, 1):
            if c in vowels:
                prefix ^= vowels[c]
            if prefix not in d:
                d[prefix] = i
            if prefix in d:
                answer = max(answer, i - d[prefix])
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "eleetminicoworoep"
        o = 13
        self.assertEqual(s.findTheLongestSubstring(i), o)

    def test_two(self):
        s = Solution()
        i = "leetcodeisgreat"
        o = 5
        self.assertEqual(s.findTheLongestSubstring(i), o)

    def test_three(self):
        s = Solution()
        i = "aeiou"
        o = 0
        self.assertEqual(s.findTheLongestSubstring(i), o)

    def test_four(self):
        s = Solution()
        i = "aaeeiioouu"
        o = 10
        self.assertEqual(s.findTheLongestSubstring(i), o)

    def test_five(self):
        s = Solution()
        i = "bcbcbc"
        o = 6
        self.assertEqual(s.findTheLongestSubstring(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)