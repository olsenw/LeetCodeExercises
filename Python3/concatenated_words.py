# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an array of strings words (without duplicates), return all the
    concatenated words in the given list of words.

    A concatenated word is defined as a string that is comprised entirely of at
    least two shorter words in the given array.
    '''
    # works because problem constraints (words are 30 characters max)
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        ws = set(words)
        @cache
        def isConcatenate(word):
            s = ""
            for i in range(len(word)):
                s += word[i]
                if s in ws and (word[i+1:] in ws or isConcatenate(word[i+1:])):
                    return True
            return False
        answer = [w for w in words if isConcatenate(w)]
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
        o = ["catsdogcats","dogcatsdog","ratcatdogcat"]
        self.assertEqual(s.findAllConcatenatedWordsInADict(i), o)

    def test_two(self):
        s = Solution()
        i = ["cat","dog","catdog"]
        o = ["catdog"]
        self.assertEqual(s.findAllConcatenatedWordsInADict(i), o)

    def test_three(self):
        s = Solution()
        i = ["cat" * i for i in range(1,10000)]
        o = i[1:]
        self.assertEqual(s.findAllConcatenatedWordsInADict(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)