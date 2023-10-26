# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A magical string s consists of only '1' and '2' and obeys the following
    rules:
    * The string s is magical because concatenating the number of contiguous
      occurrences of characters of characters '1' and '2' generates the string
      itself.
    
    The first few elements of s is s = "1221121221221121122……". If we group the
    consecutive 1's and 2's in s, If the consecutive 1's and 2's are grouped
    together it will be "1 22 11 2 1 22 1 22 11 2 11 22 ......" and the
    occurrences of 1's or 2's in each group are
    "1 2 2 1 1 2 1 2 2 1 2 2 ......". The occurrence sequence is s itself.

    Given an integer n, return the number of 1's in the first n number in the 
    magical string s.
    '''
    # based on leetcode discussion post by Marlen09
    # https://leetcode.com/problems/magical-string/solutions/3281323/481-solution-with-step-by-step-explanation/
    def magicalString(self, n: int) -> int:
        # base case
        if n == 0:
            return 0
        # initial sequence
        magic = [1,2,2]
        index = 2
        # keep appending sequence until require length
        while len(magic) < n:
            # append pattern (funky magic)
            magic += [3 - magic[-1]] * magic[index]
            # note that index does not match length of array
            index += 1
        return magic[:n].count(1)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 6
        o = 3
        self.assertEqual(s.magicalString(i), o)

    def test_two(self):
        s = Solution()
        i = 1
        o = 1
        self.assertEqual(s.magicalString(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)