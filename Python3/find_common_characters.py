# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string array words, return an array of all character that show up in
    all strings within the words (including duplicates). The answer may be
    returned in any order.
    '''
    # this is wrong (need to include duplicates)
    def commonChars_no_duplicates(self, words: List[str]) -> List[str]:
        s = set('abcdefghijklmnopqrstuvwxyz')
        for w in words:
            s = s.intersection(set(w))
        return list(s)

    def commonChars(self, words: List[str]) -> List[str]:
        c = Counter(words[0])
        for w in words[1:]:
            w = Counter(w)
            for i in c:
                c[i] = min(c[i], w[i])
        return list(c.elements())

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["bella","label","roller"]
        o = ["e","l","l"]
        self.assertEqual(s.commonChars(i), o)

    def test_two(self):
        s = Solution()
        i = ["cool","lock","cook"]
        o = ["c","o"]
        self.assertEqual(s.commonChars(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)