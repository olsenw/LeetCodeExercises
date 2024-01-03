# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Anti-theft security devices are activated inside a bank. Given a 0-indexed
    binary string array bank representing the floor plan of the bank, which is
    an m x n 2D matrix. bank[i] represents the ith row, consisting of '0's and
    '1's. '0' mean the cell is empty, while '1' means the cell has a security
    device.

    There is one laser beam between any two security devices if both conditions
    are met:
    * The two devices are located on two different rows r1 and r2, where
      r1 < r2.
    * For each row i where r1 < i < r2, there are no security devices in the ith
      row.
    
    Laser beams are independent, ie, one beam does not interfere nor join with
    another.

    Return the total number of laser beams in the bank.
    '''
    def numberOfBeams(self, bank: List[str]) -> int:
        answer = 0
        r1 = bank[0].count('1')
        for i in range(1, len(bank)):
            r2 = bank[i].count('1')
            if r2 > 0:
                answer += r1 * r2
                r1 = r2
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["011001","000000","010100","001000"]
        o = 8
        self.assertEqual(s.numberOfBeams(i), o)

    def test_two(self):
        s = Solution()
        i = ["000","111","000"]
        o = 0
        self.assertEqual(s.numberOfBeams(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)