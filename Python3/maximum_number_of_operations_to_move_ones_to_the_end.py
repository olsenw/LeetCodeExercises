# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a binary string s.

    The following operation can be preformed any number of times:
    * Choose any index i from the string where i + 1 < s.length such that
      s[i] == '1' and s[i + 1] == '0'.
    * Move the character s[i] to the right until it reaches the end of the
      string or another '1'.
    
    Return the maximum number of operations that can be performed.
    '''
    # returns minimum number of operations
    def maxOperations_fails(self, s: str) -> int:
        answer = 0
        last = False
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                last = True
            elif last and s[i] == '1':
                answer += 1
            else:
                last = False
        return answer

    def maxOperations(self, s: str) -> int:
        n = len(s)
        answer = 0
        ones = 0
        for i in range(n-1):
            if s[i] == '1':
                ones += 1
                if s[i+1] == '0':
                    answer += ones
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "1001101"
        o = 4
        self.assertEqual(s.maxOperations(i), o)

    def test_two(self):
        s = Solution()
        i = "00111"
        o = 0
        self.assertEqual(s.maxOperations(i), o)

    def test_three(self):
        s = Solution()
        i = "0010101011101"
        o = 12
        self.assertEqual(s.maxOperations(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)