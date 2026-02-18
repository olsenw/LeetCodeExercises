# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A sentence is a list of words that are separated by a single space with no
    leading or trailing spaces. Each word consists of lowercase and uppercase
    English letters.

    A sentence can be shuffled by appending the 1-indexed word position to each
    word then rearranging the words in sentence.

    Given a shuffled sentence s containing no more than 9 words, reconstruct and
    return the original sentence.
    '''
    def sortSentence(self, s: str) -> str:
        d = {int(w[-1]) - 1 : w[:-1] for w in s.split()}
        return " ".join(d[i] for i in range(len(d)))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "is2 sentence4 This1 a3"
        o = "This is a sentence"
        self.assertEqual(s.sortSentence(i), o)

    def test_two(self):
        s = Solution()
        i = "Myself2 Me1 I4 and3"
        o = "Me Myself and I"
        self.assertEqual(s.sortSentence(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)