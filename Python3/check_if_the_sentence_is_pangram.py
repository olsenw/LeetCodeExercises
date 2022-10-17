# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    A pangram is a sentence where every letter of the English alphabet appears
    at least once.
    
    Given a string sentence containing only lowercase English letters, return
    true if sentence is a pangram, or false otherwise.
    '''
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "thequickbrownfoxjumpsoverthelazydog"
        o = True
        self.assertEqual(s.checkIfPangram(i), o)

    def test_two(self):
        s = Solution()
        i = "leetcode"
        o = False
        self.assertEqual(s.checkIfPangram(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)