# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of strings words, where each string represents a word
    containing lowercase English letters.

    Also given an integer array weights of length 26, where weights[i]
    represents the weight of the ith lowercase English letter.

    The weight of a word is defined as the sum of the weights of its characters.

    For each word, take its weight modulo 26 and map the result to a lowercase
    English letter using reverse alphabetical order (0 -> 'z', 1 -> 'y', ...,
    25 -> 'a').

    Return the string formed by concatenating the mapped characters for all
    words in  order.
    '''
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        m = {j:i for i,j in enumerate("abcdefghijklmnopqrstuvwxyz")}
        n = {i:j for i,j in enumerate("abcdefghijklmnopqrstuvwxyz"[::-1])}
        answer = ""
        for w in words:
            s = sum(weights[m[c]] for c in w) % 26
            answer += n[s]
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["abcd","def","xyz"]
        j = [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]
        o = "rij"
        self.assertEqual(s.mapWordWeights(i,j), o)

    def test_two(self):
        s = Solution()
        i = ["a","b","c"]
        j = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        o = "yyy"
        self.assertEqual(s.mapWordWeights(i,j), o)

    def test_three(self):
        s = Solution()
        i = ["abcd"]
        j = [7,5,3,4,3,5,4,9,4,2,2,7,10,2,5,10,6,1,2,2,4,1,3,4,4,5]
        o = "g"
        self.assertEqual(s.mapWordWeights(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)