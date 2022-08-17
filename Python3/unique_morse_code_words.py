# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    International Morse Code defines a standard encoding where each
    letter is mapped to a series of dots and dashes, as follows:
    * 'a' maps to ".-"
    * 'b' maps to "-..."
    * 'c' maps to "-.-."
    * Leetcode has a convenient list that can be copied.

    Given an array of strings words where each word can be written as a
    concatenation of the Morse code of each letter. Return the number of
    different transformations(concatenations) among all words in array.
    '''
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        h = {a:b for a,b in zip("abcdefghijklmnopqrstuvwxyz",[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."])}
        s = set()
        for w in words:
            t = ""
            for c in w:
                t += h[c]
            s.add(t)
        return len(s)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["gin","zen","gig","msg"]
        o = 2
        self.assertEqual(s.uniqueMorseRepresentations(i), o)

    def test_two(self):
        s = Solution()
        i = ["a"]
        o = 1
        self.assertEqual(s.uniqueMorseRepresentations(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)