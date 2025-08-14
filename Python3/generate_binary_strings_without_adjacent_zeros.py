# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a positive integer n.

    A binary string x is valid if all substrings of x of length 2 contain at
    least one "1".

    Return all valid strings with length n, in any order.
    '''
    # based on hints (give it away really)
    def validStrings(self, n: int) -> List[str]:
        if n == 1:
            return ["0", "1"]
        answer = []
        for s in self.validStrings(n-1):
            if s[-1] == '1':
                answer.append(s + "0")
            answer.append(s + "1")
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 3
        o = ["010","011","101","110","111"]
        self.assertEqual(s.validStrings(i), o)

    def test_two(self):
        s = Solution()
        i = 1
        o = ["0","1"]
        self.assertEqual(s.validStrings(i), o)

    def test_three(self):
        s = Solution()
        i = 4
        o = ["0101","0110","0111","1010","1011","1101","1110","1111"]
        self.assertEqual(s.validStrings(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)