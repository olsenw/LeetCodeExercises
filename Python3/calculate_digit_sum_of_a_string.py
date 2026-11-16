# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s consisting of digits and an integer k.

    A round can be completed if the length of s is greater than k. In one round,
    do the following:
    1. Divide s into consecutive groups of size k such that the first k
       characters are in the first group, the next k characters are in the
       second group, and so on. Note that the size of the last group can be
       smaller than k.
    2. Replace each group of s with a string representing the sum of all its
       digits. For example, "346" is replaced with "13" because 3 + 4+ 6 = 13.
    3. Merge consecutive groups together to form a new string. If the length of
       the string is greater than k, repeat from step 1.
    
    Return s after all rounds have been completed.
    '''
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            n = ""
            for i in range(0,len(s),k):
                n += str(sum(int(c) for c in s[i:i+k]))
            s = n
        return s

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "11111222223"
        j = 3
        o = "135"
        self.assertEqual(s.digitSum(i,j), o)

    def test_two(self):
        s = Solution()
        i = "00000000"
        j = 3
        o = "000"
        self.assertEqual(s.digitSum(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)