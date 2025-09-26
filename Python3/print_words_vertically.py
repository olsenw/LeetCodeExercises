# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s. Return all the words vertically in the same order in which
    they appear in s.

    Words are returned as a list of strings, complete with spaces when is
    necessary. (Trailing spaces are not allowed).

    Each word would be put on only one column and that in one column there will
    be only one word.
    '''
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        l = max(len(w) for w in s)
        answer = [""] * l
        for w in s:
            i = 0
            for i,c in enumerate(w):
                answer[i] += c
            for j in range(i+1, l):
                answer[j] += " "
        for i in range(l):
            answer[i] = answer[i].rstrip()
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "HOW ARE YOU"
        o = ["HAY","ORO","WEU"]
        self.assertEqual(s.printVertically(i), o)

    def test_two(self):
        s = Solution()
        i = "TO BE OR NOT TO BE"
        o = ["TBONTB","OEROOE","   T"]
        self.assertEqual(s.printVertically(i), o)

    def test_three(self):
        s = Solution()
        i = "CONTEST IS COMING"
        o = ["CIC","OSO","N M","T I","E N","S G","T"]
        self.assertEqual(s.printVertically(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)