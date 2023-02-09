# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set

class Solution:
    '''
    Given an array of strings ideas that represents a list of names to be used
    in the process of naming a company. The process of naming a company is as
    follows:

    Choose 2 distinct names from ideas, call them ideaA and ideaB.

    Swap the first letters of ideaA and ideaB with each other.

    If both of the new names are not found in the original ideas, then the name
    ideaA ideaB (the concatenation of ideaA and ideaB, separated by a space) is
    a valid company name.

    Otherwise, it is not a valid name.

    Return the number of distinct valid names for the company.
    '''
    def distinctNames(self, ideas: List[str]) -> int:
        ht:Dict[str, Set[str]] = {i:set() for i in "abcdefghijklmnopqrstuvwxyz"}
        for i in ideas:
            ht[i[0]].add(i[1:])
        answer = 0
        for i in range(ord('a'), ord('z') + 1):
            # number to letter
            a = chr(i)
            # nothing so skip
            if len(ht[a]) == 0:
                continue
            # check against every other set
            for j in range(i+1, ord('z') + 1):
                # number to letter
                b = chr(j)
                # nothing so skip
                if len(ht[b]) == 0:
                    continue
                x = len(ht[a].difference(ht[b]))
                y = len(ht[b].difference(ht[a]))
                if x and y:
                    answer += 2 * x * y
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["coffee","donuts","time","toffee"]
        o = 6
        self.assertEqual(s.distinctNames(i), o)

    def test_two(self):
        s = Solution()
        i = ["lack","back"]
        o = 0
        self.assertEqual(s.distinctNames(i), o)

    def test_three(self):
        s = Solution()
        i = ["abcd","bbcd","cbcd","acde","bcde","ccde"]
        o = 0
        self.assertEqual(s.distinctNames(i), o)

    def test_four(self):
        s = Solution()
        i = ["coffee","donuts","time","toffee","lack","back","abcd","bbcd","cbcd","acde","bcde","ccde"]
        o = 62
        self.assertEqual(s.distinctNames(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)