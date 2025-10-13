# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed string array words, where words[i] consists of lowercase
    English letters.

    In one operation, select any index i such that 0 < i < words.length and
    words[i-1] and words[i] are anagrams, and delete words[i] from words. Keep
    performing this operation as long as it is possible to select an index that
    satisfies the conditions.

    Return words after performing all operations. It can be shown that selecting
    the indices for each operation in any arbitrary order will lead to the same
    result.

    An Anagram is a word or phrase formed by rearranging the letters of a
    different word or phrase using all the original letters exactly once.
    '''
    # removes all anagrams
    def removeAnagrams_fails(self, words: List[str]) -> List[str]:
        answer = []
        s = set()
        for w in words:
            c = "".join(sorted(w))
            if c not in s:
                s.add(c)
                answer.append(w)
        return answer

    def removeAnagrams(self, words: List[str]) -> List[str]:
        answer = []
        last = ""
        for w in words:
            c = "".join(sorted(w))
            if c != last:
                last = c
                answer.append(w)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["abba","baba","bbaa","cd","cd"]
        o = ["abba","cd"]
        self.assertEqual(s.removeAnagrams(i), o)

    def test_two(self):
        s = Solution()
        i = ["a","b","c","d","e"]
        o = ["a","b","c","d","e"]
        self.assertEqual(s.removeAnagrams(i), o)

    def test_three(self):
        s = Solution()
        i = ["a","b","a"]
        o = ["a","b","a"]
        self.assertEqual(s.removeAnagrams(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)