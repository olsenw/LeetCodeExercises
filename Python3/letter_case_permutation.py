# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s, it is possible to transform every letter individually to
    be lowercase or uppercase to create another string.

    Return a list of all possible strings that can be created. Return the output
    in any order.
    '''
    def letterCasePermutation(self, s: str) -> List[str]:
        answer = [""]
        for c in s:
            temp = []
            for a in answer:
                if c.isalpha():
                    temp.append(a + c.lower())
                temp.append(a + c.upper())
            answer = temp
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "a1b2"
        o = ["a1b2","a1B2","A1b2","A1B2"]
        self.assertEqual(sorted(s.letterCasePermutation(i)), sorted(o))

    def test_two(self):
        s = Solution()
        i = "3z4"
        o = ["3z4","3Z4"]
        self.assertEqual(sorted(s.letterCasePermutation(i)), sorted(o))

if __name__ == '__main__':
    unittest.main(verbosity=2)