# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s consisting only of characters a,b and c.

    Return the number of substrings containing at least one occurrence of all
    these characters a, b and c.
    '''
    def numberOfSubstrings(self, s: str) -> int:
        # based off answer from yesterdays problem
        # https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/description/?envType=daily-question&envId=2025-03-10
        def atLeastK(k:int) -> int:
            answer = 0
            characters = dict()
            start, end = 0,0
            while end < len(s):
                l = s[end]
                if l in characters:
                    characters[l] += 1
                else:
                    characters[l] = 1
                while len(characters) >= 3:
                    answer += len(s) - end
                    l = s[start]
                    if characters[l] > 1:
                        characters[l] -= 1
                    else:
                        del characters[l]
                    start += 1
                end += 1
            return answer
        return atLeastK(3)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abcabc"
        o = 10
        self.assertEqual(s.numberOfSubstrings(i), o)

    def test_two(self):
        s = Solution()
        i = "aaacb"
        o = 3
        self.assertEqual(s.numberOfSubstrings(i), o)

    def test_three(self):
        s = Solution()
        i = "abc"
        o = 1
        self.assertEqual(s.numberOfSubstrings(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)