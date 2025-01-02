# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed array of strings words and a 2D array of integers queries.

    Each query queries[i] = [li, ri] asks to find the number of strings present
    in the range li to ri (both inclusive) of words that start and end with a
    vowel.

    Return an array ans of size queries.length, where ans[i] is the answer to
    the ith query.

    Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.
    '''
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        vowels = "aeiou"
        # s = [1] if words[0][0] in vowels and words[0][-1] in vowels else [0]
        s = [0]
        for w in words:
            s.append(s[-1] + (1 if w[0] in vowels and w[-1] in vowels else 0))
        answer = []
        for l,r in queries:
            answer.append(s[r+1]-s[l])
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["aba","bcb","ece","aa","e"]
        j = [[0,2],[1,4],[1,1]]
        o = [2,3,0]
        self.assertEqual(s.vowelStrings(i,j), o)

    def test_two(self):
        s = Solution()
        i = ["a","e","i"]
        j = [[0,2],[0,1],[2,2]]
        o = [3,2,1]
        self.assertEqual(s.vowelStrings(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)